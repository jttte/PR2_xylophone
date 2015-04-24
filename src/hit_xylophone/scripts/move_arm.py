#!/usr/bin/env python
'''
import rospy


if __name__ == '__main__':

    #initialize the node
    rospy.init_node('pickup_object', anonymous=True)

    #sleep for a moment while everything starts up
    rospy.sleep(1.0)

    # your code here:
    rospy.loginfo("Try to pick up the cup through python script!")

'''

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
    
     
       
if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('test_arm_node');
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("left_arm")
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.57
    pose_target.position.x = 0.7
    pose_target.position.y = 0.2
    pose_target.position.z = 0.8
    group.set_pose_target(pose_target)
    myplan = group.plan()
    group.execute(myplan)



'''
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('test_arm_node');
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("left_arm")
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.57
    pose_target.position.x = 0.7
    pose_target.position.y = 0
    pose_target.position.z = 0.8
    group.set_pose_target(pose_target)
    myplan = group.plan()
    group.execute(myplan)
'''




















