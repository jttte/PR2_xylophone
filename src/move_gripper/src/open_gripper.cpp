#include "gripper.h"
#include <ros/ros.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "simple_gripper");
  ros::NodeHandle nh;

  left_Gripper gripper(nh);

  gripper.open();

  return 0;
}
