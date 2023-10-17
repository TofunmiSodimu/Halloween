#!/usr/bin/env python3

## Publish std_msgs/Strings messages


import rospy
from std_msgs.msg import String

def caller():
    pub = rospy.Publisher('speech', String, queue_size=10)
    rospy.init_node('caller', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        state = "intro"
        rospy.loginfo(state)
        pub.publish(state)
        rate.sleep()
        state = "outro"
        rospy.loginfo(state)
        pub.publish(state)

if __name__ == '__main__':
    try:
        caller()
    except rospy.ROSInterruptException:
        pass
