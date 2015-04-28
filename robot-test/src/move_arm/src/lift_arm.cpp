#include <iostream>
#include "arm.h"

int main(int argc, char **argv)
{

  ros::init(argc, argv, "move_arm_example");
  ros::NodeHandle node_handle;


  Arm arm(node_handle, "left_arm");//put "left_arm" or "right_arm"

  arm.lift_arm(0.38, 0.6, 0.9);

  return 0;
}
