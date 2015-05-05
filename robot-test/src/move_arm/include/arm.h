#include <moveit/move_group_interface/move_group.h>
#include <iostream>

class Arm{
private:
  ros::NodeHandle nh_;
  moveit::planning_interface::MoveGroup arm_;
  tf::TransformListener listener_;

public:
  //Action client initialization
  Arm(ros::NodeHandle &nh, String l_r){
    nh_ = nh;
	arm_("left_arm");
  }

  ~Arm(){
  }

  lift_arm(float x, float y, float z) {
	geometry_msgs::Pose goal_end_effector_pose;
  	goal_end_effector_pose.orientation.w = 0;
  	goal_end_effector_pose.position.x = x;
  	goal_end_effector_pose.position.y = y;
  	goal_end_effector_pose.position.z = z;
  	arm_.setPoseTarget(goal_end_effector_pose);
	arm_.asyncMove();
}

