#include <ros/ros.h>
#include <ros/package.h>
#include <tf/transform_listener.h>
#include <pcl_ros/transforms.h>

#include <boost/shared_ptr.hpp>

#include <pcl_conversions/pcl_conversions.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/io/vtk_lib_io.h>
#include <pcl/surface/organized_fast_mesh.h>
#include <pcl/common/centroid.h>
#include <pcl/common/projection_matrix.h>
#include <pcl/io/pcd_io.h>
#include <pcl/surface/gp3.h>

#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/point_cloud_conversion.h>
#include "std_msgs/String.h"
#include "geometry_msgs/Pose.h"

#include "cluster_extractor.h"
#include "scene_segmenter/XylophonePose.h"


pcl::PCDWriter writer;
namespace scene_segmenter_node
{
    class SceneSegmenterNode
    {
        private:
            ros::NodeHandle node_handle;
            ros::ServiceServer service;
            ros::Subscriber pointCloudSubscriber;
            void pointCloudMessageCallback(const sensor_msgs::PointCloud2::ConstPtr &msg);
            bool service_callback( scene_segmenter::XylophonePose::Request &req,
                      scene_segmenter::XylophonePose::Response &res );
            geometry_msgs::Pose current_pose;
            sensor_msgs::PointCloud2 current_cloud;

        public:
            SceneSegmenterNode();
    };

    SceneSegmenterNode::SceneSegmenterNode(): node_handle("")
    {
        pointCloudSubscriber = node_handle.subscribe("/head_mount_kinect/depth/points", 10, &SceneSegmenterNode::pointCloudMessageCallback, this);
        std::cout<<"update cloud";

        //service
        service = node_handle.advertiseService("get_xylophone_pose", &SceneSegmenterNode::service_callback, this);

        ros::spin();
        ROS_INFO("scene_segmenter_node ready");
    }


    bool SceneSegmenterNode::service_callback(  scene_segmenter::XylophonePose::Request &req,
                      scene_segmenter::XylophonePose::Response &res ){

        std::cout<<"receive call"<<std::endl;

        //transform cloud to world coordinate
        tf::TransformListener listener;
        tf::StampedTransform transform;
        sensor_msgs::PointCloud2 cloud_out;
        //listener.waitForTransform("/base_link", current_cloud.header.frame_id, current_cloud.header.stamp, ros::Duration(0.5));
        //listener.waitForTransform("/base_link", current_cloud.header.frame_id, ros::Time::now(), ros::Duration(0.5));
        //listener.lookupTransform("/base_link", current_cloud.header.frame_id, ros::Time::now(), transform);
        //pcl_ros::transformPointCloud("/base_link", current_cloud, cloud_out, listener);
        //listener.transformPointCloud("/base_link",ptcld1,convertedPtcld1);
        //listener.lookupTransform("/base_link", now+ros::Duration(3.0),
        //  current_cloud.header.frame_id, current_cloud.header.stamp,
        //  "/base_link", transform);
     
        //listener.transformPointCloud("/base_link", transform, now+ros::Duration(3.0), ptcld1,convertedPtcld1);
        //new!
        //Eigen::Matrix4f eigen_transform;
        //pcl_ros::transformAsMatrix(transform, eigen_transform);
        //pcl_ros::transformPointCloud(eigen_transform, current_cloud, cloud_out);

        sensor_msgs::PointCloud ptcld1;
        sensor_msgs::PointCloud2 ptcld2;
        // convert pc2 to pc
        sensor_msgs::convertPointCloud2ToPointCloud(current_cloud,ptcld1);

        sensor_msgs::PointCloud convertedPtcld1;

        ros::Time now = ros::Time::now();
        listener.waitForTransform("/base_link", current_cloud.header.frame_id, current_cloud.header.stamp, ros::Duration(3.0));  
        listener.lookupTransform("/base_link", current_cloud.header.frame_id, current_cloud.header.stamp+ros::Duration(2.0), transform);

        ptcld1.header.stamp = current_cloud.header.stamp+ros::Duration(2.0);
        listener.transformPointCloud("/base_link", ptcld1, convertedPtcld1);

        sensor_msgs::PointCloud2 convertedMessagePointCloud;
        sensor_msgs::convertPointCloudToPointCloud2(convertedPtcld1, ptcld2);

        //cloud msg to cloud     
        pcl::PCLPointCloud2::Ptr cloud (new pcl::PCLPointCloud2());
        pcl_conversions::toPCL(ptcld2, *cloud);

        //extract clusters
        ClusterExtractor *clusterExtractor = new ClusterExtractor();
        clusterExtractor->setCloud(cloud);
        clusterExtractor->computeClusters();
        std::vector<pcl::PointCloud<pcl::PointXYZ>::Ptr> cloudClusters = clusterExtractor->getCloudClusters();
        delete clusterExtractor;

        //publish clusters
        geometry_msgs::Pose pose;
        pose.orientation.w = 1.0;
        
        int max_size = 0;
        int idx = 0;
        bool find_object = false;
        for(int i = 0; i < cloudClusters.size(); i++) {
            pcl::PointCloud<pcl::PointXYZ>::Ptr cloudCluster (cloudClusters.at(i));
            if (cloudCluster->size() > max_size)
            {
                max_size = cloudCluster->size();
                idx = i;
                find_object = true;
                
            }
std::stringstream ss;
                ss<< "cloud_cluster_"<< i<<".pcd";
                writer.write<pcl::PointXYZ> (ss.str(), *cloudCluster, false);
            
        }//end of cluster list loop
        
        if(find_object == true) {
                pcl::PointCloud<pcl::PointXYZ>::Ptr cloudCluster (cloudClusters.at(idx));

                pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_xyz (new pcl::PointCloud<pcl::PointXYZ>());
                pcl::copyPointCloud(*cloudCluster,*cloud_xyz);

                Eigen::Vector4f centroid (0.f, 0.f, 0.f, 1.f);
                pcl::compute3DCentroid (*cloudCluster, centroid); 
                centroid.w () = 1.f;
                pose.position.x = centroid.x();
                pose.position.y = centroid.y();
                pose.position.z = centroid.z();
                std::cout<<"x: "<<pose.position.x<<" y: "<<pose.position.y<<" z: "<<pose.position.z<<std::endl;
            //std::stringstream ss;
            //ss<< "cloud_cluster_"<< idx<<".pcd";
            //writer.write<pcl::PointXYZ> (ss.str(), *cloudCluster, false);
            current_pose = pose; 
        }

        res.pose = current_pose;
        return true;

    }//end of service_allback

    void SceneSegmenterNode::pointCloudMessageCallback(const sensor_msgs::PointCloud2::ConstPtr &msg)
    {
        if(!msg) return;
        current_cloud = *msg;
        std::cout<<"update cloud"<<std::endl;

    }//end of pointCloudMessageCallback
}


int main(int argc, char **argv) 
{

    ros::init(argc, argv, "scene_segmenter_node");
    scene_segmenter_node::SceneSegmenterNode node;

    return 0;
}
