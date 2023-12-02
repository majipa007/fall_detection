# Fall Detection using Pose Landmarks

This project utilizes [MediaPipe](https://mediapipe.dev/) and OpenCV to detect whether a person is standing or has fallen down based on their keypoints extracted from the MediaPipe Pose module. The program analyses the keypoint landmarks obtained from a webcam or surveillance camera feed to determine a person's posture.

## Overview

The Python code in this repository employs the MediaPipe Pose module to:

- Capture frames from a camera source (webcam or surveillance camera).
- Process the frames to identify human poses and landmarks.
- Calculate the dual and single axis distance between specific body parts (optional functionality).
- Determine if a person is standing or has fallen down based on predefined criteria.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

## Usage

1. Clone this repository to your local machine.
2. Install the necessary dependencies.
3. Run the `main.py` script.




