#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class Eight(Node):
    def __init__(self):
        self.count= 1
        super().__init__('Eight') # Node name
        self.create_timer(1.0, self.timer_callback)
        
    def  timer_callback(self):
        self.get_logger().info('Yo!'+str(self.count))
        self.count+=1
    


def main(args = None):
    rclpy.init(args = args)
    node = Eight() 
    rclpy.spin(node)   # enables callbacks 
    rclpy.shutdown()

if __name__ == '__main__':
    main()

