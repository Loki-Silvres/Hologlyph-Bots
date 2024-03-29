#! /usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Hologlyph Bots (HB) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 5B of Hologlyph Bots (HB) Theme (eYRC 2023-24).
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
from geometry_msgs.msg import Twist, Pose2D
from std_msgs.msg import Bool
import time
import math
import numpy as np 
from my_robot_interfaces.msg import Goal, Shape

pose_x = 0.0
pose_y = 0.0
pose_theta = 0.0

class HBController(Node):
    def __init__(self):
        super().__init__('hb_controller_2')
        self.get_logger().info("hb_controller_2 has been started.")

        # Initialise the required variables

        self.bot_2_x = []
        self.bot_2_y = []
        self.bot_2_theta = 0.0

        # Initialze Publisher and Subscriber
        # NOTE: You are strictly NOT-ALLOWED to use "cmd_vel" or "odom" topics in this task
	    #	Use the below given topics to generate motion for the robot.
	    #   /hb_bot_1/left_wheel_force,
	    #   /hb_bot_1/right_wheel_force,
	    #   /hb_bot_1/left_wheel_force

        self.det_ar_sub = self.create_subscription(Pose2D,
                                                   '/pen2_pose',
                                                   self.get_pose_callback,
                                                   10)
        self.pen_down_publisher = self.create_publisher(Bool,
                                                   '/pen2_down',
                                                   10)
        self.mtr_spd_publisher = self.create_publisher(Twist,
                                                   '/cmd_vel_2',
                                                   10)
        
        self.next_index_timer = self.create_timer(0.5, self.next_index_callback)

        
        #Similar to this you can create subscribers for hb_bot_2 and hb_bot_3
        self.subscription = self.create_subscription(
            Goal,  
            'hb_bot_2/goal',  
            self.goalCallBack,  # Callback function to handle received messages
            10  # QoS profile, here it's 10 which means a buffer size of 10 messages
        )  

        self.subscription  # Prevent unused variable warning

        # For maintaining control loop rate.
        self.index = 0
        self.goal_flag = False
        self.vel_lim = 70
        self.finish_flag = False

        # self.rate = self.create_rate(100, self.get_clock())
        self.Kp_lin_high = 5                   # 3
        self.Kp_lin_low = 1
        self.Kp_lin_x = self.Kp_lin_high
        self.Kp_lin_y = self.Kp_lin_high
        self.Ki_lin = 1e-4 * 0 
        self.Kd_lin = 1e-3 * 0 
        self.Kp_ang = 13                       # 13
        self.Ki_ang = 1e-3 * 0 
        self.Kd_ang = 1e-2 * 0 
        self.prev_error_x = 0.0
        self.prev_error_y = 0.0
        self.prev_error_theta = 0.0
        self.integral_x = 0.0
        self.integral_y = 0.0
        self.integral_theta = 0.0
        

    def inverse_kinematics(self, vx, vy, vtheta):
        
        matrix = np.array([ [-3.33333333e-01 ,-5.77367206e-01  ,1.92678227e+00],
                            [-3.33333333e-01  ,5.77367206e-01  ,1.92678227e+00],
                            [ 6.66666667e-01 ,-2.65364284e-17  ,1.92678227e+00]])
        
        v1,v2,v3 = matrix @ np.array([[  vx  ],
                                      [  vy  ],
                                      [vtheta]])
        return v1[0], v2[0], v3[0]
    def rotation_matrix(self, vx, vy):
        matrix = np.array([[ np.cos(pose_theta), np.sin(pose_theta)],
                           [-np.sin(pose_theta), np.cos(pose_theta)]])
        v1, v2 = matrix @ np.array([[vx],
                                    [vy]])
        return v1[0], v2[0]

    def goalCallBack(self, msg):
        if not self.goal_flag:
            self.bot_2_x = msg.x 
            self.bot_2_y = msg.y
            self.bot_2_theta = msg.theta
            self.goal_flag = True
    
    def get_pose_callback(self, msg: Pose2D):
        global pose_x
        global pose_y
        global pose_theta
        pose_x = msg.x - 250
        pose_y = 250 - msg.y
        pose_theta = msg.theta

        radial_distance = np.linalg.norm(np.array([pose_x, pose_y]))
        cosine = pose_x/radial_distance
        sine = pose_y/radial_distance
        reduction_factor = 0.96     # good enough at 0.96 for bot height 13.3 cm
        reduction_exponent = 1      # 1
        radial_correction = reduction_factor ** reduction_exponent
        pose_x = radial_distance * cosine * radial_correction
        pose_y = radial_distance * sine * radial_correction
        if pose_theta > np.pi:
            pose_theta-=2*np.pi
            # pose_theta=-pose_theta

    def next_index_callback(self):
        if self.goal_flag == True:
            bool_msg = Bool()
            if(self.index>=50):

                bool_msg.data = True            
            bool_msg.data = False     # Comment this out to use pen
            self.index+=1
            if self.index >= len(self.bot_2_x): 
                self.index = 0
                bool_msg.data = False
                self.finish_flag = True
            self.pen_down_publisher.publish(bool_msg)



def main(args=None):
    rclpy.init(args=args)
    
    hb_controller = HBController()

    prev_goal_x = 0.0
    prev_goal_y = 0.0
    
    time.sleep(1)

    # Main loop
    while rclpy.ok():
        try:
            print(hb_controller.index)
            x_goal      = hb_controller.bot_2_x[hb_controller.index]
            # x_goal      = 50
            y_goal      = hb_controller.bot_2_y[hb_controller.index]
            # y_goal      = 50
            theta_goal  = hb_controller.bot_2_theta
            # theta_goal  = 1
            # if theta_goal > np.pi:
            #     theta_goal -= 2 * np.pi

        except Exception as e:
            hb_controller.get_logger().warn(
                    'Service call failed %r' % (e,))
        else:
            # hb_controller.get_logger().info(f"x_goal:{prev_goal_x:.2f},y_goal:{prev_goal_y:.2f},theta_goal:{theta_goal:.3f}")
            # hb_controller.get_logger().info(f"pose_x:{pose_x:.2f},pose_y:{pose_y:.2f},pose_theta:{pose_theta:.3f}\n")
            print(f"x_goal:{prev_goal_x:.2f},y_goal:{prev_goal_y:.2f},theta_goal:{theta_goal:.3f}")
            print(f"pose_x:{pose_x:.2f},pose_y:{pose_y:.2f},pose_theta:{pose_theta:.3f}\n")
            prev_goal_y = y_goal
            prev_goal_x = x_goal

            error_x = x_goal - pose_x
            error_y = y_goal - pose_y

            # if abs(error_x) <= 2:
            #     print('low error in x')
                # hb_controller.Kp_lin_x = hb_controller.Kp_lin_low
            # else:
            #     hb_controller.Kp_lin_x = hb_controller.Kp_lin_high
            # if abs(error_y) <= 2:
            #     print('low error in y')
                # hb_controller.Kp_lin_y = hb_controller.Kp_lin_low
            # else:
            #     hb_controller.Kp_lin_y = hb_controller.Kp_lin_high

            error_theta = theta_goal - pose_theta

            hb_controller.integral_x += error_x
            hb_controller.integral_y += error_y
            hb_controller.integral_theta += error_theta

            derv_x = error_x - hb_controller.prev_error_x
            derv_y = error_y - hb_controller.prev_error_y
            derv_theta = error_theta - hb_controller.prev_error_theta

            if abs(error_x) <=2 and abs(error_y) <=2:
                print('low error')
                # print( error_x, error_y, error_theta, hb_controller.integral_x, derv_x )

            # Change the frame by using Rotation Matrix (If you find it required)

            error_x, error_y = hb_controller.rotation_matrix(error_x, error_y) 

            # Calculate the required velocity of bot for the next iteration(s)
            
            vel_x = hb_controller.Kp_lin_x * error_x
            vel_y = hb_controller.Kp_lin_y * error_y
            vel_theta = hb_controller.Kp_ang * error_theta 

            vel_x += hb_controller.Ki_lin * hb_controller.integral_x + hb_controller.Kd_lin * derv_x
            vel_y += hb_controller.Ki_lin * hb_controller.integral_y + hb_controller.Kd_lin * derv_y
            vel_theta += hb_controller.Ki_ang * hb_controller.integral_theta + hb_controller.Kd_ang * derv_theta

            # print(f'vel_x = {hb_controller.Kp_lin_x * error_x:.3f} + {hb_controller.Ki_lin * hb_controller.integral_x:.3f} + {hb_controller.Kd_lin * derv_x:.3f}')
            # print(f'vel_y = {hb_controller.Kp_lin_y * error_y:.3f} + {hb_controller.Ki_lin * hb_controller.integral_y:.3f} + {hb_controller.Kd_lin * derv_y:.3f}')
            # print(f'vel_w = {hb_controller.Kp_ang * error_theta:.3f} + {hb_controller.Ki_ang * hb_controller.integral_theta:.3f} + {hb_controller.Kd_ang * derv_theta:.3f}\n')

            hb_controller.prev_error_x = error_x
            hb_controller.prev_error_y = error_y
            hb_controller.prev_error_theta = error_theta

            # if vel_x > hb_controller.vel_lim or vel_y > hb_controller.vel_lim:
            #     norm = np.linalg.norm([vel_x,vel_y,vel_theta])
            #     vel_x *= hb_controller.vel_lim/norm
            #     vel_y *= hb_controller.vel_lim/norm
            #     vel_theta *= hb_controller.vel_lim/norm

            # Find the required force vectors for individual wheels from it.(Inverse Kinematics)

            vl, vr, vb = hb_controller.inverse_kinematics(vel_x, vel_y, vel_theta)
            # print(vl,vr,vb)
            norm = 0
            if abs(vl) > hb_controller.vel_lim or abs(vr) > hb_controller.vel_lim or abs(vb) > hb_controller.vel_lim  :
                norm = np.linalg.norm([vl,vr,vb])
                vl *= hb_controller.vel_lim/norm
                vr *= hb_controller.vel_lim/norm
                vb *= hb_controller.vel_lim/norm

                # print(f'vel_x = {hb_controller.Kp_lin_x * error_x / norm:.3f} + {hb_controller.Ki_lin * hb_controller.integral_x / norm:.3f} + {hb_controller.Kd_lin * derv_x / norm:.3f}')
                # print(f'vel_y = {hb_controller.Kp_lin_y * error_y / norm:.3f} + {hb_controller.Ki_lin * hb_controller.integral_y / norm:.3f} + {hb_controller.Kd_lin * derv_y / norm:.3f}')
                # print(f'vel_w = {hb_controller.Kp_ang * error_theta / norm:.3f} + {hb_controller.Ki_ang * hb_controller.integral_theta / norm:.3f} + {hb_controller.Kd_ang * derv_theta / norm:.3f}\n')

                print()
            
            else:
                print(f'vel_x = {hb_controller.Kp_lin_x * error_x:.3f} + {hb_controller.Ki_lin * hb_controller.integral_x:.3f} + {hb_controller.Kd_lin * derv_x:.3f}')
                print(f'vel_y = {hb_controller.Kp_lin_y * error_y:.3f} + {hb_controller.Ki_lin * hb_controller.integral_y:.3f} + {hb_controller.Kd_lin * derv_y:.3f}')
                print(f'vel_w = {hb_controller.Kp_ang * error_theta:.3f} + {hb_controller.Ki_ang * hb_controller.integral_theta:.3f} + {hb_controller.Kd_ang * derv_theta:.3f}\n')

            motors = Twist()
            motors.linear.x = vl
            motors.linear.y = vr
            motors.linear.z = vb

            # Apply appropriate force vectors
            
            hb_controller.mtr_spd_publisher.publish(motors)

        # Spin once to process callbacks
        # hb_controller.rate.sleep()
        
        time.sleep(0.01)
        rclpy.spin_once(hb_controller)
        if hb_controller.finish_flag:
            break
    pen_down_msg = Bool()
    pen_down_msg.data = False
    hb_controller.pen_down_publisher.publish(pen_down_msg)
    
    # Destroy the node and shut down ROS
    hb_controller.destroy_node()
    rclpy.shutdown()

# Entry point of the script
if __name__ == '__main__':
    main()
