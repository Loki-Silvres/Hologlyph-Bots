import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import math
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal

global pose_x
global pose_y
global pose_theta

class HBTask1BController(Node):
   def __init__(self):
        super().__init__('hb_task1b_controller')
        self.get_logger().info('hb_task1b_controller has been started.')
        self.cmd_vel_pub = self.create_publisher(Twist,'/cmd_vel',10)
        self.odom_sub = self.create_subscription(Odometry,'/odom',self.bot_pose,10)
        
        # Initialze Publisher and Subscriber
        # We'll leave this for you to figure out the syntax for
        # initialising publisher and subscriber of cmd_vel and odom respectively

        # Declare a Twist message
        self.vel = Twist()
        # Initialise the required variables to 0
        self.vel.linear.x = 0.0
        self.vel.linear.y = 0.0
        self.vel.angular.z = 0.0
        # For maintaining control loop rate.
        self.rate = self.create_rate(1000)
        # Initialise variables that may be needed for the control loop
        # For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
        # and also Kp values for the P Controller
        self.x_goal = 0.0
        self.y_goal = 0.0
        self.theta_goal = 0.0
        self.Kp = 1.1   
        # self.Ki = 1e-2
        self.flag = 0
        # self.sum_error_x = 0.
        # self.sum_error_y = 0.
        # self.sum_error_theta = 0.

        # client for the "next_goal" service
        self.cli = self.create_client(NextGoal, '/next_goal')      
        self.send_request = NextGoal.Request() 
        self.index = 0
        self.send_request.request_goal = self.index
        self.future = self.cli.call_async(self.send_request)
   def bot_pose(self,msg: Odometry):
       global pose_x
       global pose_y
       global pose_theta
       pose_x = msg.pose.pose.position.x
       pose_y = msg.pose.pose.position.y
       rot_coord = msg.pose.pose.orientation
       (roll,pitch,pose_theta)=euler_from_quaternion([rot_coord.x, rot_coord.y, rot_coord.z, rot_coord.w])

def main(args=None):
    global pose_x
    global pose_y
    global pose_theta
    rclpy.init(args=args)
    
    # Create an instance of the EbotController class
    ebot_controller = HBTask1BController()
    # Send an initial request with the index from ebot_controller.index
    # ebot_controller.send_request.request_goal = ebot_controller.index
    # ebot_controller.future = ebot_controller.cli.call_async(ebot_controller.send_request)
    
    # Main loop
    while rclpy.ok():
    
        # Check if the service call is done
        if ebot_controller.future.done():
            ebot_controller.get_logger().info('done.')
            try:
                # response from the service call
                response = ebot_controller.future.result()
            except Exception as e:
                ebot_controller.get_logger().infselfo(
                    'Service call failed %r' % (e,))
            else:
                #########           GOAL POSE             #########
                x_goal      = response.x_goal
                y_goal      = response.y_goal
                theta_goal  = response.theta_goal
                ebot_controller.flag = response.end_of_list
                ebot_controller.get_logger().info(f"x_goal:{x_goal}, y_goal:{y_goal}, theta_goal:{theta_goal}")
                ebot_controller.get_logger().info(f"pose_x:{pose_x}, pose_y:{pose_y}, pose_theta:{pose_theta}")
                ####################################################

                # Find error (in x, y and theta) in global frame
                # the /odom topic is giving pose of the robot in global frame
                # the desired pose is declared above and defined by you in global frame
                # therefore calculate error in global frame
                error_x = x_goal - pose_x
                error_y = y_goal - pose_y
                error_theta = theta_goal - pose_theta

                # ebot_controller.sum_error_x+= error_x
                # ebot_controller.sum_error_y+= error_x
                # ebot_controller.sum_error_theta+= error_theta

                # (Calculate error in body frame)
                # But for Controller outputs robot velocity in robot_body frame, 
                # i.e. velocity are define is in x, y of the robot frame, 
                # Notice: the direction of z axis says the same in global and body frame
                # therefore the errors will have have to be calculated in body frame.
                # 
                # This is probably the crux of Task 1, figure this out and rest should be fine.

                # Finally implement a P controller 
                # to react to the error with velocities in x, y and theta.
                velocity = ebot_controller.vel
                velocity.linear.x = ebot_controller.Kp * error_x #+ ebot_controller.Ki * ebot_controller.sum_error_x
                velocity.linear.y = ebot_controller.Kp * error_y #+ ebot_controller.Ki * ebot_controller.sum_error_y
                velocity.angular.z = ebot_controller.Kp * error_theta #+ ebot_controller.Ki * ebot_controller.sum_error_theta
                ebot_controller.cmd_vel_pub.publish(velocity)
                # Safety Check
                # make sure the velocities are within a range.
                # for now since we are in a simulator and we are not dealing with actual physical limits on the system 
                # we may get away with skipping this step. But it will be very necessary in the long run.


                #If Condition is up to you
                
                ############     DO NOT MODIFY THIS       #########
                ebot_controller.index += 1
                if ebot_controller.flag == 1 :
                    ebot_controller.index = 0
                ebot_controller.send_request.request_goal = ebot_controller.index
                ####################################################

                ebot_controller.send_request.request_goal = ebot_controller.index
                ebot_controller.future = ebot_controller.cli.call_async(ebot_controller.send_request)
        # Spin once to process callbacks
        rclpy.spin_once(ebot_controller)
    
    # Destroy the node and shut down ROS
    ebot_controller.destroy_node()
    # rclpy.spin()
    rclpy.shutdown()

if __name__ == '__main__':
        main()
