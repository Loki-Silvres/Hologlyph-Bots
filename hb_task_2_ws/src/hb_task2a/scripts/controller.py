#! /usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Hologlyph Bots (HB) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 2A of Hologlyph Bots (HB) Theme (eYRC 2023-24).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''


# Team ID:		1523
# Author List:		Alok Raj, Atul Kumar, Aman Anand, Siddharth Gorai
# Filename:		feedback.py
# Functions:
#			[ Comma separated list of functions in this file ]
# Nodes:		Add your publishing and subscribing node


################### IMPORT MODULES #######################

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Wrench
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose2D
import time
import math
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal     
import numpy as np        

# You can add more if required
##############################################################


# Initialize Global variables

pose_x = 0.0
pose_y = 0.0
pose_theta = 0.0

################# ADD UTILITY FUNCTIONS HERE #################

##############################################################


# Define the HBController class, which is a ROS node
class HBController(Node):
    def __init__(self):
        super().__init__('hb_controller')
        self.get_logger().info('Controller has been started.')
        # Initialze Publisher and Subscriber
        # NOTE: You are strictly NOT-ALLOWED to use "cmd_vel" or "odom" topics in this task
	    #	Use the below given topics to generate motion for the robot.
	    #   /hb_bot_1/rear_wheel_force,
	    #   /hb_bot_1/right_wheel_force,
	    #   /hb_bot_1/left_wheel_force

        self.det_ar_sub = self.create_subscription(Pose2D,
                                                   '/detected_aruco',
                                                   self.get_pose_callback,
                                                   10)
        self.left_force_pub = self.create_publisher(Wrench,
                                             '/hb_bot_1/left_wheel_force',
                                             10)
        self.right_force_pub = self.create_publisher(Wrench,
                                             '/hb_bot_1/right_wheel_force',
                                             10)
        self.rear_force_pub = self.create_publisher(Wrench,
                                             '/hb_bot_1/rear_wheel_force',
                                             10)
        
        # For maintaining control loop rate.
        self.rate = self.create_rate(100)
        self.Kp_lin_high = 4
        self.Kp_lin_low = 1
        self.Kp_lin_x = self.Kp_lin_high
        self.Kp_lin_y = self.Kp_lin_high
        self.Ki_lin = 5e-2
        self.Kd_lin = 1e-2
        self.Kp_ang = 100.0
        self.Ki_ang = 1
        self.Kd_ang = 5.0
        self.prev_error_x = 0.0
        self.prev_error_y = 0.0
        self.prev_error_theta = 0.0
        self.integral_x = 0.0
        self.integral_y = 0.0
        self.integral_theta = 0.0


        # client for the "next_goal" service
        self.cli = self.create_client(NextGoal, 'next_goal')      
        self.req = NextGoal.Request() 
        self.index = 0

    
    # Method to create a request to the "next_goal" service
    def send_request(self, request_goal):
        self.req.request_goal = request_goal
        self.future = self.cli.call_async(self.req)

    def inverse_kinematics(self, vx, vy, vtheta):
        ############ ADD YOUR CODE HERE ############

        # INSTRUCTIONS & HELP : 
        #	-> Use the target velocity you calculated for the robot in previous task, and
        #	Process it further to find what proportions of that effort should be given to 3 individuals wheels !!
        #	Publish the calculated efforts to actuate robot by applying force vectors on provided topics
        ############################################

        matrix = np.array([[-1.0, -1.732/3, 1.0],[-1.0, 1.732/3, 1.0],[2.0, 0.0, 1.0]])
        v1,v2,v3 = matrix @ np.array([[vx],[vy],[vtheta]])
        return v1, v2, v3
    
    def get_pose_callback(self, msg: Pose2D):
        global pose_x
        global pose_y
        global pose_theta
        pose_x = msg.x - 250
        pose_y = 250 - msg.y
        pose_theta = msg.theta

def main(args=None):
    rclpy.init(args=args)
    
    # Create an instance of the HBController class
    hb_controller = HBController()
   
    # Send an initial request with the index from ebot_controller.index
    hb_controller.send_request(hb_controller.index)
    
    prev_goal_x = 0.0
    prev_goal_y = 0.0


    # Main loop
    while rclpy.ok():

        # Check if the service call is done
        if hb_controller.future.done():
            try:
                # response from the service call
                response = hb_controller.future.result()
            except Exception as e:
                hb_controller.get_logger().infselfo(
                    'Service call failed %r' % (e,))
            else:
                #########           GOAL POSE             #########

                x_goal      = response.x_goal
                y_goal      = response.y_goal
                theta_goal  = response.theta_goal

                if pose_x >200 or pose_y >200:
                    x_goal      = 0.0
                    y_goal      = 0.0
                    theta_goal  = 0.0

                hb_controller.flag = response.end_of_list
                # hb_controller.get_logger().info(f"x_goal:{prev_goal_x},y_goal:{prev_goal_y}, theta_goal:{theta_goal}")
                # hb_controller.get_logger().info(f"pose_x:{pose_x},pose_y:{pose_y}, pose_theta:{pose_theta}")
                hb_controller.get_logger().info(f"x_goal:{prev_goal_x:.2f},y_goal:{prev_goal_y:.2f}")
                hb_controller.get_logger().info(f"pose_x:{pose_x:.2f},pose_y:{pose_y:.2f}\n")
                prev_goal_y = y_goal
                prev_goal_x = x_goal

                ####################################################
                
                # Calculate Error from feedback

                error_x = x_goal - pose_x
                error_y = y_goal - pose_y

                if abs(error_x) <= 2:
                    print('low error in x')
                    # hb_controller.Kp_lin_x = hb_controller.Kp_lin_low
                else:
                    hb_controller.Kp_lin_x = hb_controller.Kp_lin_high
                if abs(error_y) <= 2:
                    print('low error in y')
                    # hb_controller.Kp_lin_y = hb_controller.Kp_lin_low
                else:
                    hb_controller.Kp_lin_y = hb_controller.Kp_lin_high

                error_theta = theta_goal - pose_theta

                hb_controller.integral_x += error_x
                hb_controller.integral_y += error_y
                hb_controller.integral_theta += error_theta

                derv_x = error_x - hb_controller.prev_error_x
                derv_y = error_y - hb_controller.prev_error_y
                derv_theta = error_theta - hb_controller.prev_error_theta

                
                if abs(error_x) <=2 and abs(error_y) <=2:
                    print( error_x, error_y, error_theta, hb_controller.integral_x, derv_x )


                # Change the frame by using Rotation Matrix (If you find it required)

                # Calculate the required velocity of bot for the next iteration(s)
                
                vel_x = hb_controller.Kp_lin_x * error_x
                vel_y = hb_controller.Kp_lin_y * error_y
                vel_theta = hb_controller.Kp_ang * error_theta 

                vel_x += hb_controller.Ki_lin * hb_controller.integral_x + hb_controller.Kd_lin * derv_x
                vel_y += hb_controller.Ki_lin * hb_controller.integral_y + hb_controller.Kd_lin * derv_y
                vel_theta += hb_controller.Ki_ang * hb_controller.integral_theta + hb_controller.Kd_ang * derv_theta

                print(f'vel_x = {hb_controller.Kp_lin_x * error_x:.3f} + {hb_controller.Ki_lin * hb_controller.integral_x:.3f} + {hb_controller.Kd_lin * derv_x:.3f}')
                print(f'vel_y = {hb_controller.Kp_lin_y * error_y:.3f} + {hb_controller.Ki_lin * hb_controller.integral_y:.3f} + {hb_controller.Kd_lin * derv_y:.3f}')
                print(f'vel_w = {hb_controller.Kp_ang * error_theta:.3f} + {hb_controller.Ki_ang * hb_controller.integral_theta:.3f} + {hb_controller.Kd_ang * derv_theta:.3f}\n')



                hb_controller.prev_error_x = error_x
                hb_controller.prev_error_y = error_y
                hb_controller.prev_error_theta = error_theta

                # Find the required force vectors for individual wheels from it.(Inverse Kinematics)

                fr = Wrench()
                fb = Wrench()
                fl = Wrench()
                vl, vr, vb = hb_controller.inverse_kinematics(vel_x, vel_y, vel_theta)
                fl.force.y = vl[0]
                fr.force.y = vr[0]
                fb.force.y = vb[0]

                # Apply appropriate force vectors
                
                hb_controller.left_force_pub.publish(fl)
                hb_controller.right_force_pub.publish(fr)
                hb_controller.rear_force_pub.publish(fb)
                # print(fl.force.y,fr.force.y,fb.force.y)

                # Modify the condition to Switch to Next goal (given position in pixels instead of meters)
                
                ############     DO NOT MODIFY THIS       #########
                hb_controller.index += 1
                if hb_controller.flag == 1 :
                    hb_controller.index = 0
                hb_controller.send_request(hb_controller.index)
                ####################################################
        
        # Spin once to process callbacks
        rclpy.spin_once(hb_controller)
    
    # Destroy the node and shut down ROS
    hb_controller.destroy_node()
    rclpy.shutdown()

# Entry point of the script
if __name__ == '__main__':
    main()
