#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header


class TrajectoryDrawer(Node):
    def __init__(self):
        super().__init__("trajectory_drawer")

        self.odom_sub_ = self.create_subscription(Odometry, "/bumperbot_controller/odom", self.odomCallback, 10)
        self.trajectory_pub_ = self.create_publisher(Path, "bumperbot_controller/trajectory", 10)

        self.poses_stamped_ = []
    
    def odomCallback(self, odom_msg):
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = "odom"

        pose_stamped = PoseStamped()
        pose_stamped.header = header
        pose_stamped.pose = odom_msg.pose.pose
        self.poses_stamped_.append(pose_stamped)

        self.publishTrajectory()
    
    def publishTrajectory(self):
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = "odom"
    
        msg = Path()
        msg.header = header
        msg.poses = self.poses_stamped_
        self.trajectory_pub_.publish(msg)

def main():
    rclpy.init()
    node = TrajectoryDrawer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()