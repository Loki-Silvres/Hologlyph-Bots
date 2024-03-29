#! /usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Hologlyph Bots (HB) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 2B of Hologlyph Bots (HB) Theme (eYRC 2023-24).
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
from geometry_msgs.msg import Wrench, Pose2D
from nav_msgs.msg import Odometry
import time
import math
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal     
import numpy as np  
from my_robot_interfaces.msg import Goal             

pose_x = 0.0
pose_y = 0.0
pose_theta = 0.0

class HBController(Node):
    def __init__(self):
        super().__init__('hb_controller_1')
        self.get_logger().info('Controller 1 has been started.')

        # Initialise the required variables
        self.bot_1_x = []
        self.bot_1_y = []
        self.bot_1_theta = 0.0

        # Initialze Publisher and Subscriber
        # NOTE: You are strictly NOT-ALLOWED to use "cmd_vel" or "odom" topics in this task
	    #	Use the below given topics to generate motion for the robot.
	    #   /hb_bot_1/left_wheel_force,
	    #   /hb_bot_1/right_wheel_force,
	    #   /hb_bot_1/left_wheel_force

        self.det_ar_sub = self.create_subscription(Pose2D,
                                                   '/detected_aruco_1',
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
        
        #Similar to this you can create subscribers for hb_bot_2 and hb_bot_3
        self.subscription = self.create_subscription(
            Goal,  
            'hb_bot_1/goal',  
            self.goalCallBack,  # Callback function to handle received messages
            10  # QoS profile, here it's 10 which means a buffer size of 10 messages
        )  

        self.subscription  # Prevent unused variable warning

        # For maintaining control loop rate.
        self.rate = self.create_rate(100)
        self.Kp_lin_high = 2
        self.Kp_lin_low = 1
        self.Kp_lin_x = self.Kp_lin_high
        self.Kp_lin_y = self.Kp_lin_high
        self.Ki_lin = 1e-2
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

    def inverse_kinematics(vx, vy, vtheta):
        ############ ADD YOUR CODE HERE ############

        # INSTRUCTIONS & HELP : 
        #	-> Use the target velocity you calculated for the robot in previous task, and
        #	Process it further to find what proportions of that effort should be given to 3 individuals wheels !!
        #	Publish the calculated efforts to actuate robot by applying force vectors on provided topics
        ############################################
        matrix = np.array([[-1.0, -1.732/3, 1.0],[-1.0, 1.732/3, 1.0],[2.0, 0.0, 1.0]])
        v1,v2,v3 = matrix @ np.array([[vx],[vy],[vtheta]])
        return v1, v2, v3

    def goalCallBack(self, msg):
        self.bot_1_x = msg.x
        self.bot_1_y = msg.y
        self.bot_1_theta = msg.theta

    def get_pose_callback(self, msg: Pose2D):
        global pose_x
        global pose_y
        global pose_theta
        pose_x = msg.x - 250
        pose_y = 250 - msg.y
        pose_theta = msg.theta

def main(args=None):
    rclpy.init(args=args)
    
    hb_controller = HBController()
       
    # Main loop
    while rclpy.ok():

        # Spin once to process callbacks
        hb_controller.get_logger().info(hb_controller.rate)
        rclpy.spin_once(hb_controller)
    
    # Destroy the node and shut down ROS
    hb_controller.destroy_node()
    rclpy.shutdown()

# Entry point of the script
if __name__ == '__main__':
    main()
