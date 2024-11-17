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
top_left = [20,20]
top_right = [480,20]
bottom_left = [20,480]
bottom_right = [480, 480]
id_to_corner = {8:'top_left', 10:'top_right', 4:'bottom_left', 12:'bottom_right', 1:'hb_bot'}

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

        self.det_ar_pub = self.create_publisher(Pose2D,
                                                '/detected_aruco', 
                                                10)
        # self.timer = self.create_timer(0.5, self.show_pose_callback)
        # self.show_pose = False 

    def image_callback(self, msg: Image):

        #convert ROS image to opencv image

        cv_image = self.bridge.imgmsg_to_cv2(msg)
        # _,cv_image = cv.threshold(cv_image,100,200,cv.THRESH_BINARY)
        # cv.imshow('re',cv_image)
        # cv.waitKey(0)
        # cv_image = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
        #Detect Aruco marker

        corners, ids, reject = self.aruco.detectMarkers(cv_image)
        # aruco.drawDetectedMarkers(cv_image, corners, ids, [0,0,255])
        # cv.imshow('re',cv_image)
        # cv.waitKey(0)
        corners = np.array(corners)
        ids = np.array(ids)

        if(1 in ids):

            bot_corners = corners[ids==1][0]
            bot_pos = np.sum(bot_corners,axis = 0)/4
            bot_x ,bot_y = bot_pos.astype('float')
            bot_top = bot_corners[1] - bot_corners[0]
            bot_top_vec = bot_top/np.linalg.norm(bot_top)
            bot_theta = np.arccos(bot_top_vec[0]).astype('float') 
            if(bot_top_vec[1]>0):
                bot_theta=-bot_theta            

            # Publish the bot coordinates to the topic  /detected_aruco

            bot_pose = Pose2D()
            bot_pose.x = bot_x 
            bot_pose.y = bot_y 
            bot_pose.theta = bot_theta
            self.det_ar_pub.publish(bot_pose)
            # if self.show_pose:
            #     self.get_logger().info(f"x:{bot_x}, y:{bot_y}, theta:{bot_theta:.3f}")
            #     self.show_pose = False
        
    # def show_pose_callback(self):
    #     self.show_pose = True

def main(args=None):
    rclpy.init(args=args)

    aruco_detector = ArUcoDetector()

    rclpy.spin(aruco_detector)

    aruco_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
