#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class pose_sub(Node):
    def __init__(self):
        super().__init__('pose_subcriber')
        self.pose = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
    

    def pose_callback(self, msg: Pose):
        self.get_logger().info("("+str(msg.x)+ ", "+str(msg.y)+ ")")

def main(args = None):
    rclpy.init(args = args)
    node = pose_sub()
    rclpy.spin(node)
    rclpy.shutdown()