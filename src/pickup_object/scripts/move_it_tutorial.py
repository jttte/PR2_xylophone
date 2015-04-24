#!/usr/bin/env python
import os
import sys
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s",data.data)

def listener():
    rospy.init_node('test_node')
    rospy.Subscriber("/head_mount_kinect/depth/points", String, callback)
    rospy.spin()

if __name__=="__main__":
    listener()


    #pc = rospy.Publisher ('scene_cloud', String, queue_size=10)
    #rospy.init_node ('scene_cloud', anonymous=True)
    #rate = rospy.Rate(2) #2hz

    #print 'starting scene broadcast server'
