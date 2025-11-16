#ifndef SIMPLE_TURTLESIM_KINEMATICS
#define SIMPLE_TURTLESIM_KINEMATICS

#include <rclcpp/rclcpp.hpp>
#include <turtlesim/msg/pose.hpp>


class SimpleTurtlesimKinematics : public rclcpp::Node
{
public:
    SimpleTurtlesimKinematics(const std::string & name);

private:
    void turtle1PoseCallback(const turtlesim::msg::Pose & pose);
    void turtle2PoseCallback(const turtlesim::msg::Pose & pose);

    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr turtle1_pose_sub_;
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr turtle2_pose_sub_;

    turtlesim::msg::Pose last_turtle1_pose_;
    turtlesim::msg::Pose last_turtle2_pose_;
};

#endif