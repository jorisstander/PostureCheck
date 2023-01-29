# PostureCheck

This is the final project for the subject 'Datascience for IoT'. With the help of OpenCV and its documentation on poor posture detection, it has been possible to create and modify examples to a working live-feed poor posture detection program. By adding a live-feed, SMS notification service, and changes in the code, this prototype will notify you via SMS whenever your posture has been poor for 3 minutes.

## Demo

## Process Outline
Since I spend a lot of time behind my PC, it is important I keep an eye out on my posture. This is where I got the idea to create something to solve this issue for myself. I started looking at possible solutions and came across the term body pose tracking very quickly. This is for example used for yoga to check if a pose is done correctly, or during workouts to make sure exercises are performed correctly. This was a perfect technology for my idea and so I started reading up on body pose tracking. 

### MediaPipe vs Yolov7
While reading i came across the names MediaPipe and Yolov7, and decided to use MediaPipe in the end because of the results I found in this [video](https://www.youtube.com/watch?v=hCJIU0pOl5g&ab_channel=LearnOpenCV). 

### OpenCV
When I was looking for MediaPipe tutorials that included poor posture, I found this page on [OpenCV](https://learnopencv.com/building-a-body-posture-analysis-system-using-mediapipe) that used the technology i wanted, and had a perfect tutorial about the idea I wanted to create. The plan was to get it working on my PC and then move it on the raspberry pi and test it out there. The tutorial was great, but it was focused on video inputs like an mp4 or a mov file. I wanted a live-feed with my webcam and so i started adding code to the tutorial to get it up and running. This was done by adding a while loop and checking if there is someone in the frame. 

### Twilio 
I decided to add a SMS service to the code so that you get notified when needed. After comparing a few SMS services, I choose Twilio since it had a free trial and a balance to try out with.

### Moving the project to the raspberry PI
Till now it went pretty smoothly, but the installation on the raspberry pi was definitely harder than expected. After trying to install the python packages, I found out quickly that some of these were not compatible with the Raspberry pi OS, and found out I had to install a different version of the OS called Buster. After installing this OS I got everything installed. 

### Running the program on the raspberry pi 
When I ran it for the first time, I unfortunatly saw that the frame rate on the camera was very bad. Also there wasa problem with the time of having a bad posture. Normally you would receive a SMS after 10 seconds, but these 10 seconds took almost a whole minute. I figured out that the function to get the FPS of openCV does not work on a live-feed and will always return 30 fps. Which means that it calculates the time with 30 fps while sometimes the FPS was actually 5. This made the time go 6 times slower in the program. This problem was in the end fixed by calculating the FPS myself for every frame. 

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
