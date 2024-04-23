# IMAGPRO-Video-Color-Blind-Simulator

Our color blindness simulator is a  that accurately replicates how people with color vision deficiencies perceive videos. Unlike static image simulations, our simulator provides a comprehensive and immersive experience for understanding colorblindness. It focuses on three main types of color blindness, which are protanomaly, deuteranomaly, and tritanomal. It also simulates in two levels of severity, 0.5 and 1.0. This was developed using the DaltonLens python library and OpenCV. 

## Installation
1. Install Python: Make sure you have Python installed on your system. You can download and install Python from here.
2. Install Required Packages: Run the following commands in your terminal to install the required Python packages:

![image](https://github.com/ErnestLontoc/IMAGPRO-Video-Color-Blind-Simulator/assets/104815584/bd85955c-1c2f-4ab2-bb35-31d8beeed326)


## Usage
1. Clone the Repository: Clone this repository to your local machine or download the script file (color_blindness_simulator.py).
2. Prepare Your Video: Ensure you have a valid .mp4 video file that you want to simulate for color blindness.
3. Change the path file or directory in the script to your desired path file
4. Run the Script: Open a terminal window and navigate to the directory where the script is located. Run the following command:
![image](https://github.com/ErnestLontoc/IMAGPRO-Video-Color-Blind-Simulator/assets/104815584/75a91f84-7856-40b0-a1fb-a1b4c483c2cc)
5. Follow the Prompts: The script will prompt you to enter the type of colorblindness (1 for Protanomaly, 2 for Deuteranomaly, 3 for Tritanomaly) and the intensity level (1 for 0.5, 2 for 1.0).
6. Wait for Processing: The script will simulate the color blindness effects on each frame of the video. This may take some time depending on the length and complexity of the video.
7. View the Output: Once the simulation is complete, you can find the simulated video (CBVideo.mp4) in the same directory as the script.
8. Optional: Add Audio: If you want to add audio to the simulated video, follow the prompts at the end of the script. The final video with audio will be saved as OutputWithAudio.mp4.
