#!/usr/bin/env python3
## A node for the robot's spoken interaction with the kids on Halloween day

import rospy
from std_msgs.msg import String
from gtts import gTTS
import playsound
import random

def callback(data):
    state = data.data
    rospy.loginfo(rospy.get_caller_id() + "Speaking to children now because I heard %s", state)

    if state == 'intro':
        intro()
    elif state == 'outro':
        outro()

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("speech",String,callback)
    rospy.spin()

def intro():
    #  Greetings for the robot to say
    intro = ['Hello, would you like some candy?']

    #  randomly pick intro to play
    msg = random.choice(intro)
    tts = gTTS(text=msg, lang='en')
    path = './intro.mp3'
    tts.save(path)
    playsound.playsound(path, True)

def outro():
    #  Greetings for the robot to say
    outro = ['Have a SPOOKTACULAR Halloween!','May your candy last you at least til Christmas!','Hope your Halloween is full of more treats than tricks!','Have a boooo-tiful Halloween!',
        'Happy Halloween to the cutest pumpkin in the patch.','Happy Halloween and enjoy that sugar rush tonight!']

    #  randomly pick outro to play
    msg = random.choice(outro)
    tts = gTTS(text=msg, lang='en')
    path = './outro.mp3'
    tts.save(path)
    playsound.playsound(path, True)

if __name__ == '__main__':
        listener()
