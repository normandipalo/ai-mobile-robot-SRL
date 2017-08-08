#!/usr/bin/env python
from time import *
import nxt.locator
from nxt.motor import *
from nxt.sensor import *
#import getch



#Here I define some motion primitives for the robot.

def evade_right(b):
    
    #for _ in range(4):
    turn_right(b,360)
    time.sleep(1)

    go_forward(b,800)
    time.sleep(1)
    #for _ in range(4):
    turn_left(b,360)
    time.sleep(1)

def evade_left(b):
    
   # for _ in range(4):
    turn_left(b,360)
    time.sleep(1)
    go_forward(b,800)
    time.sleep(1)
    #for _ in range(4):
    turn_right(b,360)
    time.sleep(1)


def go_forward(b, degrees):
    #INPUT: brick b, degrees to go ahead
    power=100
    if degrees<0:
        degrees=-degrees
        power=-power
    #motorl = SynchronizedMotors(b, PORT_A)
    motorr = Motor(b, PORT_B)
    motorl = Motor(b, PORT_C)
    motors = SynchronizedMotors(motorl, motorr, 1)
    motors.turn(power, degrees, brake=False)   
# motorr.turn(power, degrees, timeout=1000)
   # motorl.turn(power, degrees, timeout=1000)


def turn_right(b, degrees):
    #INPUT: brick b, degrees to go ahead
    power=100
    if degrees<0:
        degrees=-degrees
        power=-power
    #motorl = SynchronizedMotors(b, PORT_A)
    motorr = Motor(b, PORT_B)
    motorl = Motor(b, PORT_C)
    motors = SynchronizedMotors(motorl, motorr, 100)
    motors.turn(power, degrees, brake=False)   
# motorr.turn(power, degrees, timeout=1000)


# motorl.

def turn_left(b, degrees):
    #INPUT: brick b, degrees to go ahead
    power=-100
    if degrees<0:
        degrees=-degrees
        power=-power
    #motorl = SynchronizedMotors(b, PORT_A)
    motorr = Motor(b, PORT_B)
    motorl = Motor(b, PORT_C)
    motors = SynchronizedMotors(motorr, motorl, 100)
    motors.turn(power, degrees, brake=False)   


def brake(b):
    #INPUT: brick b, degrees to go ahead
    
    motorr = Motor(b, PORT_B)
    motorl = Motor(b, PORT_C)
    motors = SynchronizedMotors(motorr, motorl, 1)
    motors.brake()  

b = nxt.locator.find_one_brick()
k=0 


#Obstacle avoidance with landmark following. The robot reads from the center.txt file that specfies the angle of the
#landmark with respect to the saggital axis of the robot. It allignes with it every 4 steps, expecting the file to be
#updated in background.

while(1):

    if k%4==0:
        with open("/Users/normand/Desktop/center.txt", "r") as file:
                try:
                    cntx=file.readline()
                    cntx=int(cntx.split()[0])
                    print(int(cntx))
                 #   file.write("0")
                    if cntx>0:
                        turn_left(b,int(cntx))
                    else:
                        turn_right(b,int(cntx))
                except Exception as e:
                    print(e)

        with open("/Users/normand/Desktop/center.txt", 'w') as file:
                    file.write("0")

    
    distr=Ultrasonic(b, PORT_1).get_sample()
    distc=Ultrasonic(b, PORT_2).get_sample()
    distl=Ultrasonic(b, PORT_3).get_sample()
    print("distanze {} {} {}: ".format(distl,distc,distr))

    k+=1


    if distc>35 and distl>35 and distr>35:
        print("forward")
        go_forward(b,100)
        time.sleep(0.3)

    if distc>35 and distl<35:
        print("right")
        turn_left(b,180)
        time.sleep(0.3)

    if distc>35 and distr<35:
        print("left")
        turn_right(b,180)
        time.sleep(0.3)

    if distc<35 and distr>35:
        print("evade right")
        evade_left(b)

    
    if distc<35 and distl>35:
        print("evade left")
        evade_right(b)    

    if distc<35 and distl<35 and distr<35:
        print("evade right")
        evade_right(b) 


    time.sleep(0.5)


