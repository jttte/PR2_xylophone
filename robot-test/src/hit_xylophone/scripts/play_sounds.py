#!/usr/bin/env python
import sys
import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

"""
The generate_sound function is used to play passed in note, and result in the voice in speaker.
note: the note number of the note. Techinicially, each note number shoud have different voice assoicate with it.

Attention: the audio file that was palyed by ros must in the format of "*.wav"
sound_play node should be setup at first
command: roslaunch sound_play soundplay_node.launch

This function should be called when the hit xylphone action was finished, implies it should be called in move_actions.py
"""

def generate_sound(note):
    rospy.init_node('play', anonymous = True)
    soundhandle = SoundClient()
    rospy.sleep(1)
    soundhandle.playWave('/home/cl3295/robot-test/src/sound_play/sounds/note_1.wav')
    rospy.sleep(1)


if __name__ == '__main__':
	generate_sound(1)
