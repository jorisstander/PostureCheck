# PostureCheck

This is the final project for the subject 'Datascience for IoT'. With the help of OpenCV and its documentation on poor posture detection, it has been possible to create and modify examples to a working live-feed poor posture detection program. By adding a live-feed, SMS notification service, and changes in the code, this prototype will notify you via SMS whenever your posture has been poor for 3 minutes.

## Demo

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
