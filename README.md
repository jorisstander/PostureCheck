# PostureCheck

This is the final project for the subject 'Datascience for IoT'. With the help of OpenCV and its documentation on poor posture detection, it has been possible to create and modify examples to a working live-feed poor posture detection program. By adding a live-feed, SMS notification service, and changes in the code, this prototype will notify you via SMS whenever your posture has been poor for 3 minutes.

## Demo

https://user-images.githubusercontent.com/25158146/215510505-edc1ff39-2027-44c7-8737-72e7b663e1f8.mp4

## Process Outline
As I spend significant time on my computer, it's crucial for me to maintain good posture. This led me to come up with an idea to solve this problem for myself. I began exploring potential solutions and came across the concept of body pose tracking. It is commonly used in yoga to ensure proper alignment in poses and during workouts to ensure exercises are done correctly. This technology was an ideal fit for my idea, and so I delved deeper into researching body pose tracking.

### MediaPipe vs Yolov7
During my research on body pose tracking, I encountered the names MediaPipe and Yolov7. After reviewing the results, I ultimately decided to use MediaPipe, as I found it to be more suitable for my project after watching a [video](https://www.youtube.com/watch?v=hCJIU0pOl5g&ab_channel=LearnOpenCV) on it. 

### OpenCV
While searching for MediaPipe tutorials that addressed poor posture, I discovered a page on [OpenCV](https://learnopencv.com/building-a-body-posture-analysis-system-using-mediapipe) that utilized the technology I desired and provided an excellent tutorial for the concept I aimed to create. My plan was to first implement it on my PC, and then later move it to a Raspberry Pi. The tutorial was excellent, but it was designed for video inputs such as mp4 or mov files. I wanted a live-feed using my webcam, so I began modifying the tutorial's code to accommodate this.

### Twilio 
I decided to incorporate an SMS service into the code so that it would send notifications when necessary. After evaluating various SMS services, I chose Twilio, as it offered a free trial and a credit balance to test with.

### Moving the project to the raspberry PI
So far, the project had progressed smoothly, but installing it on the Raspberry Pi proved to be more challenging than anticipated. Upon attempting to install the required python packages, I quickly discovered that some of them were not compatible with the existing Raspberry Pi OS. I then learned that I had to install a different version of the OS, called Raspbian Buster, in order to proceed. After installing this OS, all necessary packages were successfully installed.

### Running the program on the raspberry pi 
When I first ran the program, I unfortunately discovered that the camera's frame rate was very poor. Additionally, there was an issue with the duration of poor posture. Typically, a SMS would be sent after 10 seconds, however, this 10 seconds was taking almost a full minute. I discovered that the function to get the FPS of OpenCV does not work on a live-feed and will always return 30 fps. This meant that the program was calculating the time with 30 fps, even when the actual FPS was much lower, such as 5. This caused the time to be 6 times slower in the program. I was able to fix this problem by calculating the FPS for each frame individually.

## Requirements
* Raspberry Pi 4
* Webcam or camera for Raspberry Pi
* Phone number for receiving text messages
* Twilio trial account
* Raspbian Buster OS
* Python v3.7.3 or above
## Installation

It is recommended to use a virtual environment for your python packages. You also **NEED** Raspbian Buster OS.

1. Install OpenCV by running `pip install opencv-python` check out this [installation guide](https://littlebirdelectronics.com.au/guides/165/set-up-opencv-on-raspberry-pi-4) if you have errors

2. Install mediapipe for Raspberry Pi by running `pip install mediapipe-rpi4`

3. Install Twilio by running `pip install twilio`

## Configuration
Now that we have installed all the packages, we only have to change a few parameters in the code.

There are the 2 scripts in this program:
- main.py ( in this file you can find all the calculations and UI code for this program)
- sms.py ( in this file you can setup your sms service to get notified)

You have to change a few things in sms.py to make this work. These values are commented with #Todo. For more info on this check out [Twilio](https://www.twilio.com).

Note: if you have 2 cameras on your pc, you might need to change a value in main.py. Change the value from 0 to 1, if this is still not working try 2, 3 and so on.

Line 45: `cap = cv2.VideoCapture(0)`

## Usage

Now that everything is set up, you can run the program. Make sure you have your camera plugged in, and position yourself in front of the camera with a perfect side view. 

Run the script using the command `python posture_detection.py`
The script will begin monitoring the side-view of a person and will calculate the neck and torso inclination. If poor body posture is detected, a text message will be sent to the configured phone number after a certain amount of time.

## Note
Make sure to use the compatible version of the packages with your python version. For more info about the code, check out the comments in the code.

## Conclusion
This project uses Mediapipe and OpenCV to detect poor body posture and alert the user via text message. By using a Raspberry Pi and a webcam, the project is able to monitor the side-view of a person and calculate the neck and torso inclination in real-time.

## References

- [OpenCV tutorial on poor posture](https://learnopencv.com/building-a-body-posture-analysis-system-using-mediapipe/)
- [Installation OpenCV raspberry pi](https://littlebirdelectronics.com.au/guides/165/set-up-opencv-on-raspberry-pi-4)
- [Twilio installation video](https://www.youtube.com/watch?v=ywH2rsL371Q&ab_channel=Indently)
- [Yolov7 vs MediaPipe](https://www.youtube.com/watch?v=hCJIU0pOl5g&ab_channel=LearnOpenCV)
- [Tutorial about AI hand Pose estimation](https://www.youtube.com/watch?v=vQZ4IvB07ec&ab_channel=NicholasRenotte)
- [installation mediapipe raspberry pi](https://stackoverflow.com/questions/67410495/how-to-install-and-use-mediapipe-on-raspberry-pi-4)
- [Time problem because of low FPS - 1](https://www.youtube.com/watch?app=desktop&v=1A7f2c8PAZ8&ab_channel=ZubayerHossain)
- [Time problem because of low FPS - 2](https://www.geeksforgeeks.org/python-displaying-real-time-fps-at-which-webcam-video-file-is-processed-using-opencv/)
