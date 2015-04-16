#include "gripper.h"
#include <ros/ros.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "simple_gripper");
  ros::NodeHandle nh;

  Gripper gripper(nh);

  gripper.close();

  return 0;
}
