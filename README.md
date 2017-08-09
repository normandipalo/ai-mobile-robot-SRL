## AI-enhanced Mobile Robot for TESP 2017 (Work in progress)

Code for the robot developed with the Tohoku Space Robotics Lab during the Tohoku Engineering Summer Program 2017.

Tested on a MacBook, OS X 10.11.6.

To use the Object Detection, you need to download the Tensorflow models repository (https://github.com/tensorflow/models). Then, place obj_recogn_chatbot.py inside models/object_detection.

All the nxt files require Python 2, while all the others require Python 3.

Here you can find a Medium post that briefly explains my experience at TESP2017 and the development of the robot. https://medium.com/towards-data-science/what-ive-learned-from-studying-robotics-in-japan-for-two-weeks-bd252961853f

![alt text](https://github.com/normandipalo/ai-mobile-robot-SRL/blob/master/images/Schermata%202017-08-08%20alle%2010.38.24.png?raw=true?raw=true)

## How to use

The 3 nxt files are the one that actually command the Lego Mindstorm Microcontroller. Remote control and obstacle avoidance are standalone programs, and you can run them on Python 2 to control the robot.
The landmark following file reads from a center.txt file the angle at which the landmark is with respect to the robot. This angle is given by a computer vision software (landmark write in this case) that should run in parallel. While this is not the cleanest and most efficient solution, I had a very short time to implement all the parts so I adopted this kind of solution. 
In case you want to use the object recognition with the chatbot, you'll need an api.ai account and respective client token to insert in the code, and also a Telegram chatbot. You will also need the telepot and apiai libraries for Python 3.
