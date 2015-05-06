#include <moveit/move_group_interface/move_group.h>
#include <iostream>

int main(int argc, char **argv)
{

  ros::init(argc, argv, "move_arm_example");
  ros::NodeHandle node_handle;


  moveit::planning_interface::MoveGroup l_arm_move_group("left_arm");


  geometry_msgs::Pose goal_end_effector_pose;
  goal_end_effector_pose.orientation.w = 0;
  goal_end_effector_pose.position.x = 0.7;
  goal_end_effector_pose.position.y = 0.0;
  goal_end_effector_pose.position.z = 1;
  l_arm_move_group.setPoseTarget(goal_end_effector_pose);

  // plan the motion and then move the group to the sampled target 
  l_arm_move_group.asyncMove();

  return 0;
}
