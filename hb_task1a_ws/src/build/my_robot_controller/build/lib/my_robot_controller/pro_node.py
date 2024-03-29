#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class Eight(Node):
    def __init__(self):
        super().__init__('Eight') # Node name
        self.get_logger().info('Hello from Alok')


def main(args = None):
    rclpy.init(args = args)
    node = Eight() 
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()

