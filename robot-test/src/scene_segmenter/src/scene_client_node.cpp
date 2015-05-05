#include <ros/ros.h>
#include <ros/package.h>

#include <sensor_msgs/PointCloud2.h>
#include "std_msgs/String.h"
#include "geometry_msgs/Pose.h"


#include "scene_segmenter/XylophonePose.h"

#include "move_base.h"
#include "math.h"


int main(int argc, char **argv)
{
  float des_x = 2.18;
  float des_y = 0;


  ros::init(argc, argv, "get_xylophone_pose_node");
  ros::NodeHandle nh;
  ros::ServiceClient client = nh.serviceClient<scene_segmenter::XylophonePose>("get_xylophone_pose");

  scene_segmenter::XylophonePose srv;
  int iteration = 2;
  while(iteration>0) {
    if (client.call(srv))
    {

        ROS_INFO("get service");
        std::cout<<"get pose x: "<<srv.response.pose.position.x<<" y: "<<srv.response.pose.position.y<<" z: "<<srv.response.pose.position.y<<std::endl;
    } else {
        ROS_ERROR("Failed to call service get_xylophone_pose");
        return 1;
    }
    std::cout<<"start to move"<<std::endl;
    ros::init(argc, argv, "robot_driver");
    RobotDriver driver(nh);
    if(srv.response.pose.position.y < des_y) {
        driver.turnOdom(true, M_PI/2);
        driver.driveForwardOdom(des_y-srv.response.pose.position.y);
        driver.turnOdom(false, M_PI/2);
    } else if (srv.response.pose.position.y > des_y) {
        driver.turnOdom(false, M_PI/2);
        driver.driveForwardOdom(srv.response.pose.position.y-des_y);
        driver.turnOdom(true, M_PI/2);
    }
    if(srv.response.pose.position.x > des_x) {
        driver.driveForwardOdom(srv.response.pose.position.x-des_x);
    } 

    iteration--;
  }//end of while


  return 0;
}
