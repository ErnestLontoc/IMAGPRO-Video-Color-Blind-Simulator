import os
import cv2
import moviepy.editor as mp
import time
from daltonlens import simulate
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array
from tqdm import tqdm


def is_valid_mp4(file_path):
    """
    Check if the file path points to a valid .mp4 file.
    """
    if os.path.isfile(file_path) and file_path.lower().endswith('.mp4'):
        return True
    else:
        return False

def extract_frames_from_video(input_video_path):
    video = VideoFileClip(input_video_path)
    frames = []

    for frame in video.iter_frames():
        frames.append(frame)

    video.close()

    return frames

def apply_simulation(images):
    simulator = simulate.Simulator_Machado2009()
    simulated_images = []
    
    while True:
        try:
            colorblind_type = int(input("Please enter your colorblind type (1 for Protanomaly, 2 for Deuteranomaly, 3 for Tritanomaly): "))
            if colorblind_type in [1, 2, 3]:
                break
            else:
                print("Please enter a valid input (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid integer.")
    
    while True:
        try:
            intensity_choice = int(input("Please enter the intensity level (1 for 0.5, 2 for 1.0): "))
            if intensity_choice in [1, 2]:
                intensity = 0.5 if intensity_choice == 1 else 1.0
                break
            else:
                print("Please enter a valid input (1 or 2).")
        except ValueError:
            print("Please enter a valid integer.")
    
    print("Simulating each image...")
    for image in tqdm(images, desc="Simulating images", unit="image"):
        if colorblind_type == 1: 
            simulated_image = simulator.simulate_cvd(image, simulate.Deficiency.PROTAN, severity=intensity)
        elif colorblind_type == 2: 
            simulated_image = simulator.simulate_cvd(image, simulate.Deficiency.DEUTAN, severity=intensity)
        elif colorblind_type == 3: 
            simulated_image = simulator.simulate_cvd(image, simulate.Deficiency.TRITAN, severity=intensity)
        simulated_images.append(simulated_image)
    print("Image simulation complete.")
    
    return simulated_images

def convert_to_bgr(images):
    bgr_images = []
    for image in images:
        # Convert RGB to BGR
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        bgr_images.append(bgr_image)
    return bgr_images

def reconstruct_video(images, frame_rate):
    height, width, _ = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter(r"C:\\Users\\DuanneCruz\\Downloads\\CBVideo.mp4", fourcc, frame_rate, (width, height))

    for image in images:
        output_video.write(image)

    output_video.release()

def get_video_info(input_video_path):
    video = VideoFileClip(input_video_path)

    num_frames = int(video.duration * video.fps)

    frame_rate = video.fps

    video.close()

    return num_frames, frame_rate

def extract_audio(input_video_path):
    mp3_file = r"C:\\Users\\DuanneCruz\\Downloads\\InputAudio.mp3"

    video_clip = VideoFileClip(input_video_path)

    audio_clip = video_clip.audio

    audio_clip.write_audiofile(mp3_file)

    audio_clip.close()
    video_clip.close()

    print("Audio extraction successful!")
    
    return mp3_file

def main(input_video_path):
    if not is_valid_mp4(input_video_path):
        print("Please provide a valid .mp4 file.")
        return
    
    num_frames, frame_rate = get_video_info(input_video_path)
    print("Number of frames:", num_frames)
    print("Frame rate:", frame_rate, "fps")
    print("")
    
    print("Extracting audio from input video...")
    mp3_file = extract_audio(input_video_path)
    print("Audio extraction complete.")
    print("")
    
    print("Splitting video into frames...")
    input_images = extract_frames_from_video(input_video_path)
    print("Splitting complete.")
    print("")
    
    simulated_images = apply_simulation(input_images)
    print("")
    
    print("Converting images from RGB to BGR")
    bgr_images = convert_to_bgr(simulated_images)
    print("Image conversion complete.")
    print("")
    
    print("Reconstructing video using images...")
    reconstruct_video(bgr_images, frame_rate)
    print("Reconstructing complete")
    
    return mp3_file

if __name__ == "__main__":
    start_time = time.time()
    input_video_path = r"C:\\Users\\DuanneCruz\\Downloads\\Nature.mp4"
    output_video_path = r"C:\\Users\\DuanneCruz\\Downloads\\CBvideo.mp4"
    mp3_file = main(input_video_path)
    
    if mp3_file:
        video_clip = VideoFileClip(output_video_path)
        orig_clip = VideoFileClip(input_video_path)
        audio_clip = AudioFileClip(mp3_file)
        print("Setting audio to modified video")
        final_clip = video_clip.set_audio(audio_clip)
        final_clip = clips_array([[orig_clip], [final_clip]])
        final_clip.write_videofile(r"C:\\Users\\DuanneCruz\\Downloads\\OutputWithAudio.mp4")
        print("All processes complete.")
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
