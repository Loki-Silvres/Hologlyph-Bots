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
################### IMPORT MODULES #######################
import rclpy
from rclpy.node import Node

# Import the required modules
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist, Pose2D
from cv_bridge import CvBridge
import cv2 as cv
import cv2.aruco as aruco
import numpy as np
##############################################################

bot_x, bot_y, bot_theta = 0.0, 0.0, 0.0

class ArUcoDetector(Node):

    def __init__(self):
        super().__init__('ar_uco_detector')
        self.get_logger().info("Feedback has been started.")

        # Subscribe the topic /camera/image_raw

        self.img_sub = self.create_subscription(Image, 
                                    '/camera/image_raw', 
                                    self.image_callback, 
                                    10)
        self.aruco = aruco.ArucoDetector(aruco.getPredefinedDictionary(aruco.DICT_4X4_1000),
                            aruco.DetectorParameters())
        self.bridge = CvBridge()

        self.det_ar_pub_1 = self.create_publisher(Pose2D,
                                                '/detected_aruco_1', 
                                                10)
        self.det_ar_pub_2 = self.create_publisher(Pose2D,
                                                '/detected_aruco_2', 
                                                10)
        self.det_ar_pub_3 = self.create_publisher(Pose2D,
                                                '/detected_aruco_3', 
                                                10)
        self.timer_time = 2
        self.timer1 = self.create_timer(self.timer_time, self.show_pose_callback1)
        self.show_pose1 = False
        self.timer2 = self.create_timer(self.timer_time, self.show_pose_callback2)
        self.show_pose2 = False
        self.timer3 = self.create_timer(self.timer_time, self.show_pose_callback3)
        self.show_pose3 = False

    def get_pose(self, bot_corners):
        
        bot_pos = np.sum(bot_corners,axis = 0)/4
        bot_x ,bot_y = bot_pos.astype('float')
        bot_top = bot_corners[1] - bot_corners[0]
        bot_top_vec = bot_top/np.linalg.norm(bot_top)
        bot_theta = np.arccos(bot_top_vec[0]).astype('float') 
        if(bot_top_vec[1]>0):
            bot_theta = 2 * np.pi - bot_theta           

        bot_pose = Pose2D()
        bot_pose.x = bot_x 
        bot_pose.y = bot_y 
        bot_pose.theta = bot_theta

        return bot_pose

    def image_callback(self, msg: Image):

        #convert ROS image to opencv image

        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        #Detect Aruco marker

        corners, ids, reject = self.aruco.detectMarkers(cv_image)
        aruco.drawDetectedMarkers(cv_image, corners, ids, [0,0,255])

        # cv.imshow('win', cv_image)
        # cv.waitKey(0)

        top_left = [20,20]
        top_right = [480,20]
        bottom_left = [20,480]
        bottom_right = [480, 480]
        id_to_object = {8:'top_left', 
                        10:'top_right', 
                        4:'bottom_left', 
                        12:'bottom_right', 
                        1:'hb_bot_1', 
                        2:'hb_bot_2',
                        3:'hb_bot_3'}

        corners = np.array(corners)
        ids = np.array(ids)
        
        if(np.sum(ids==1) > 0):

            bot_pose = self.get_pose(corners[ids==1][0])
            self.det_ar_pub_1.publish(bot_pose)
            if self.show_pose1:
                self.get_logger().info(f"bot 1: x:{bot_pose.x}, y:{bot_pose.y}, theta:{bot_pose.theta:.3f}")
                self.show_pose1 = False

        if(np.sum(ids==2) > 0):

            bot_pose = self.get_pose(corners[ids==2][0])
            self.det_ar_pub_2.publish(bot_pose)
            if self.show_pose2:
                self.get_logger().info(f"bot 2: x:{bot_pose.x}, y:{bot_pose.y}, theta:{bot_pose.theta:.3f}")
                self.show_pose2 = False

        if(np.sum(ids==3) > 0):

            bot_pose = self.get_pose(corners[ids==3][0])
            self.det_ar_pub_3.publish(bot_pose)
            if self.show_pose3:
                self.get_logger().info(f"bot 3: x:{bot_pose.x}, y:{bot_pose.y}, theta:{bot_pose.theta:.3f}")
                self.show_pose3 = False
        
    def show_pose_callback1(self):
        self.show_pose1 = True
    def show_pose_callback2(self):
        self.show_pose2 = True
    def show_pose_callback3(self):
        self.show_pose3 = True

def main(args=None):
    rclpy.init(args=args)

    aruco_detector = ArUcoDetector()

    rclpy.spin(aruco_detector)

    aruco_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
