#!/usr/bin/env python
import os
import sys
import rospy
from roslib import message
import sensor_msgs.point_cloud2 as pc2

def callback(data):
    rospy.loginfo("I heard data")

def cloud_listener():
    rospy.init_node('point_cloud')
    rospy.Subscriber("/head_mount_kinect/depth/points", PointCloud2, callback)
    rospy.spin()

if __name__=="__main__":
    cloud_listener()
    command_listener()

    #pc = rospy.Publisher ('scene_cloud', String, queue_size=10)
    #rospy.init_node ('scene_cloud', anonymous=True)

    #print 'starting scene broadcast server'
