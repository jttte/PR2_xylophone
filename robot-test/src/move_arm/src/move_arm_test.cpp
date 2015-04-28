#include <moveit/move_group_interface/move_group.h>
#include <iostream>

int main(int argc, char **argv)
{

  ros::init(argc, argv, "move_arm_example");
  ros::NodeHandle node_handle;


  moveit::planning_interface::MoveGroup l_arm_move_group("left_arm");


  // as an example, we can set a random target
  //l_arm_move_group.setRandomTarget();


  //but here is how to set a specific pose goal
  // right arm ?
  // 0.28 0.70 1.0
  geometry_msgs::Pose goal_end_effector_pose;
  goal_end_effector_pose.orientation.w = 1.0;
  goal_end_effector_pose.position.x = 1;
  goal_end_effector_pose.position.y = 1;
  goal_end_effector_pose.position.z = 0;
  l_arm_move_group.setPoseTarget(goal_end_effector_pose);


  // plan the motion and then move the group to the sampled target 
  l_arm_move_group.move();

  ros::shutdown();


  return 0;
}
