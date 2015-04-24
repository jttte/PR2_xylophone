#!/usr/bin/env python


import roslib
from pr2_controllers_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import rospy



class Arm:
	def __init__(self, arm_name):
	#arm_name should be l_arm or r_arm
		self.name = arm_name
		self.jta = actionlib.SimpleActionClient('/'+arm_name+'_controller/joint_trajectory_action',
                                                    JointTrajectoryAction)
		rospy.loginfo('Waiting for joint trajectory action')
		self.jta.wait_for_server()
		rospy.loginfo('Found joint trajectory action!')

	def move(self, angles):
		goal = JointTrajectoryGoal()
		char = self.name[0] #either 'r' or 'l'
		goal.trajectory.joint_names = [char+'_shoulder_pan_joint',
						char+'_shoulder_lift_joint',
						char+'_upper_arm_roll_joint',
						char+'_elbow_flex_joint',
						char+'_forearm_roll_joint',
						char+'_wrist_flex_joint',
						char+'_wrist_roll_joint']
		point = JointTrajectoryPoint()
		point.positions = angles
		point.time_from_start = rospy.Duration(3)
		goal.trajectory.points.append(point)
		self.jta.send_goal_and_wait(goal)


'''
This function is used to move shouler along y direction. the effect joint is *_shoulder_pan_joint
arguments:
arm: specify which arm your are control on, should be either 'l_arm' or 'r_arm'
shoulder_pos: specify the goal position of the shoulder, leagal range for left_shoulder [-0.564, 2.1353]
'''
def move_shoudler_pan(arm, shoulder_pos):
    rospy.init_node('arm_signal_node')
    arm = Arm(arm)
    #control  *_shoulder_pan_joint
    points = [shoulder_pos, 0.23, 0.1, -0.5, -3.14, -0.1, 0.1]
    arm.move(points)
    #points = [0.1, 0.1, 0.1, -0.5, -3.14, -0.1, 0.1]
    arm.move(points)


'''
This function is used to shake wrist to hit xylophone. the effect joint is *_wrist_flex_joint
arguments:
arm: specify which arm your are control on, should be either 'l_arm' or 'r_arm'
shoulder_pos: specify the shoulder position.
waist_pos: specify the goal position of the waist, leagal range for left/right wrist [-2.0, -0.1]
Note: to use this range, the *_forearm_roll_joint should be set to -3.14 at first.
'''
def move_arm_wrist(arm, shoulder_pos, wrist_pos):
    rospy.init_node('arm_signal_node')
    arm = Arm(arm)
    #control *_wrist_flex_joint
    points = [shoulder_pos, 0.23, 0.1, -0.5, -3.14, wrist_pos, 0.1]
    arm.move(points)
    points = [shoulder_pos, 0.23, 0.1, -0.5, -3.14, -0.1, 0.1]
    arm.move(points)


'''
if __name__ == '__main__':
	rospy.init_node('lift_right_arm_tester')
	main()
'''