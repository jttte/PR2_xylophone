#!/usr/bin/env python

import sys
import roslib
import rospy
import actionlib

from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from pr2_controllers_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint



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
note_number: the number of the note that was played

Note: to use this range, the *_forearm_roll_joint should be set to -3.14 at first.
'''
def move_arm_wrist(arm, shoulder_pos, wrist_pos, note_number):
    rospy.init_node('arm_signal_node')
    arm = Arm(arm)
    #control *_wrist_flex_joint
    points = [shoulder_pos, 0.23, 0.1, -0.5, -3.14, wrist_pos, 0.1]
    arm.move(points)
    generate_sound(note_number)
    points = [shoulder_pos, 0.23, 0.1, -0.5, -3.14, -0.1, 0.1]
    arm.move(points)




"""
The generate_sound function is used to play passed in note, and result in the voice in speaker.
arguments:
note: the note number of the note. Techinicially, each note number shoud have different voice assoicate with it.

Attention:
1. the audio file that was palyed by ros must in the format of "*.wav"
2. sound_play node should be setup at first. Command: roslaunch sound_play soundplay_node.launch

This function should be called when the hit xylphone action was finished, implies it should be called in move_actions.py
"""

def generate_sound(note_number):
    #Since it was called in move_arm_wrist. A nodes called arm_signal_node has already been called, no need to initiate a    new node at here
    #rospy.init_node('play', anonymous = True)

    #the sounds dictionary for coorelating notes with wav file
    sounds_dict = []
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_1.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_2.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_3.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_4.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_5.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_6.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_7.wav')
    sounds_dict.append('/home/cl3295/robot-test/src/sound_play/sounds/note_1.wav')

    soundhandle = SoundClient()
    soundhandle.playWave(sounds_dict[note_number-1])
    



'''
if __name__ == '__main__':
	rospy.init_node('lift_right_arm_tester')
	main()
'''
