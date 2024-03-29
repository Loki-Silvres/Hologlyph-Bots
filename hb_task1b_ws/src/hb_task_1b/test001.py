import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import math
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal

class HBTask1BController(Node):
   def __init__(self):
        super().__init__('test')
        
        # client for the "next_goal" service
        self.cli = self.create_client(NextGoal, '/next_goal')      
        self.send_request = NextGoal.Request() 
        self.index = 0
        self.future = self.cli.call(self.send_request)
        rclpy.spin_until_future_complete('test', self.future)
        if self.future.done():
             self.response = self.future.result()
             self.get_logger.warn(self.response)
   
#    def send_request(self, index):
#         # Send a request to the "next_goal" service
#         self.req.index = index
#         self.future = self.cli.call_async(self.req)
def main(args=None):
    rclpy.init(args=args)
    rclpy.spin()
    
    rclpy.shutdown()

if __name__ == '__main__':
        main()
