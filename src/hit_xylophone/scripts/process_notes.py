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



class NotesReader:
	#this is the array for mapping note to shoulder joint position. pose(note_number) = pos_dict[note_number - 1]
	pos_dict = [0.25, 0.15, 0, -0.15, 0.15, 0, -0.15, -0.25]

	#select the right arm acoording to the note
	def selectArm(self, note):
		if note < 5: 
			return 'l_arm'
		else:
			return 'r_arm'

	#convert note into right shoulder joint position
	def convertToPose(self, note):
		return self.pos_dict[note-1]


	#read notes frome simple text file
	def readSimpleText(self, file_name):
		notes_array = []
		with open(file_name) as f:
			for note in f:
				notes_array.append(int(note))
		return notes_array


if __name__ == '__main__':
	file_name = 'test.txt'
	reader = NotesReader()
	notes = reader.readSimpleText(file_name)
	item = 0
	for item in notes:
		arm = reader.selectArm(item)
		shoulder_pose = reader.convertToPose(item)
		move_actions.move_shoudler_pan(arm, shoulder_pose)
		move_actions.move_arm_wrist(arm, shoulder_pose, -0.7)

	
	'''
	for item in notes:
		print item
		print reader.selectArm(item)
		print reader.convertToPose(item)
	'''
