# PostureCheck

This is the final project for Datascience for Iot.

## How to Setup?

Make sure you have **pip** installed!

First of all we need to install and create a virtual environment. You can do this by using the following code:

`python3 -m pip install --user virtualenv`

After installing it we have to create the environment. Make sure you are in your project folder. So for example in a folder called PostureCheck.

`python3 -m venv venv`

This will create a folder called venv. Now we have to start up the virtual environment by typing:

`venv\Scripts\activate`

Now that we have a virtual environment we can install the requirements. You can find the requirements.txt in this repository. To run this file, type in cmd the following command:

`pip install -r requirements.txt`

Now that we have installed all the packages and created our own virtual environment, we only have to change a few parameters in the code.

There are the 2 scripts in this program:
- main.py ( in this file you can find all the calculations and UI code for this program)
- sms.py ( in this file you can setup your sms service to get notified)

You have to change a few things in sms.py to make this work. These values are commented with #Todo. For more info on this check out [Twilio](https://www.twilio.com).

Note: if you have 2 cameras on your pc, you might need to change a value in main.py. Change the value from 0 to 1, if this is still not working try 2, 3 and so on.

Line 45: `cap = cv2.VideoCapture(0)`

## How to run?

Now that everything is set up, you can run the program. Make sure you have your camera plugged in, and position yourself in front of the camera with a perfect side view. 

open cmd in your root folder and type `python3 main.py`

after having a bad posture for 3 min you will get notified with an sms.


