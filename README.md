#PR2 with Xylophone
## Final Project of COMS 6998-03 HUMANOID ROBOTS, SPRING 2015, Columbia University


## Instructions

The following lines will not work unless ROS is properly installed.  

```bash
$ cd PR2_xylophone
$ catkin_make
$ source devel/setup.bash
```

### Initialize
First, bring up Gazebo, Moveit and the PR2
```bash
$ roslaunch system_launch pr2_gazebo_moveit.launch
```

### Approach xylophone
Manually move PR2 to a place further behind, then run the instructions below. PR2 will move back to the hitting position.
```bash
$ rosrun scene_segmenter scene_segmenter_node
```
open another terminal, run:
```bash
$ rosrun scene_segmenter scene_client_node
```

### Play xylophone

run:
```bash
$ cd src/hit_xylophone/scripts/
$ rosrun hit_xylophone precess_notes.py
```

PR2 will play the notes on test.txt

### Pick Up object

The coordinates are all hard-coded. If you wish to use this script, change the numbers in pickup_stck.py to match the position of your object.
run:
```bash
$ rosrun pickup_object pickup_stick.py
```