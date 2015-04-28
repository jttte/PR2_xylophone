#!/usr/bin/env python

import sys
import roslib
from pr2_controllers_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import rospy
import move_leftshoulder
import lift_leftwaist
import move_actions
import process_notes



'''
def main():
    arm = Arm('l_arm')
    points = [0.1, 0.1, 0.1, 0.1, -3.14, -1.2, 0.1]
    arm.move(points)
    points = [0.1, 0.1, 0.1, -0.5, -3.14, -0.1, 0.1]
    arm.move(points)
    #arm.move([0.1]*7)
    #arm.move([-0.1]*7)
'''
     
       
if __name__ == '__main__':
    file_name = 'test.txt'
    reader = NotesReader()
    notes = reader.readSimpleText(file_name)
    item = 0
    for item in notes:
		#print item
        arm = reader.selectArm(item)
        shoulder_pose = reader.convertToPose(item)
        move_actions.move_shoudler_pan(arm, shoulder_pose)
        move_actions.move_arm_wrist(arm, shoulder_pose, -1.2)


'''    
    move_actions.move_shoudler_pan('l_arm', 0.3)
    move_actions.move_arm_wrist('l_arm', 0.3, -1.2)
    move_actions.move_shoudler_pan('l_arm', 0.15)
    move_actions.move_arm_wrist('l_arm', 0.15, -1.2)
    move_actions.move_shoudler_pan('l_arm', 0)
    move_actions.move_arm_wrist('l_arm', 0, -1.2)
    move_actions.move_shoudler_pan('l_arm', -0.15)
    move_actions.move_arm_wrist('l_arm', -0.15, -1.2)

    move_actions.move_shoudler_pan('r_arm', 0)
    move_actions.move_arm_wrist('r_arm', 0, -1.2)
    move_actions.move_shoudler_pan('r_arm', -0.15)
    move_actions.move_arm_wrist('r_arm', -0.15, -1.2)
    move_actions.move_shoudler_pan('r_arm', -0.3)
    move_actions.move_arm_wrist('r_arm', -0.3, -1.2)
    move_actions.move_shoudler_pan('r_arm', -0.45)
    move_actions.move_arm_wrist('r_arm', -0.45, -1.2)
'''

    
    #rospy.init_node('lift_right_arm_tester')
    #move_leftshoulder.main()
    #lift_leftwaist.main()
