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
import matplotlib.pyplot as plt
##############################################################

bot_x, bot_y, bot_theta = 0.0, 0.0, 0.0
image = None
points = []
cv.namedWindow('bots')

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

        self.flag = True

    def get_pose(self, bot_corners):
        
        global bot_x
        global bot_y
        global bot_theta

        bot_pos = np.sum(bot_corners,axis = 0)/4
        bot_x ,bot_y = bot_pos.astype('int')
        bot_top = bot_corners[1] - bot_corners[0]
        bot_top_vec = bot_top/np.linalg.norm(bot_top)
        bot_theta = np.arccos(bot_top_vec[0]).astype('float') 
        if(bot_top_vec[1]>0):
            bot_theta = 2 * np.pi - bot_theta           

    def drawCircle(self):

        global points
        global image
        for pt in points:
            image = cv.circle(image, (pt[0], pt[1]), 
                      radius= 0, color= [0,0,255], 
                      thickness=-1,lineType=cv.LINE_4)
        # pointss = np.array(points)
        # plt.plot(pointss[:,0],pointss[:,1],marker = '*')
        # plt.show()
        

    def image_callback(self, msg: Image):

        global image
        global bot_x
        global bot_y
        global bot_theta
        global points

        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        corners, ids, reject = self.aruco.detectMarkers(cv_image)
        image = aruco.drawDetectedMarkers(cv_image, corners, ids, [0,0,255])

        corners = np.array(corners)
        ids = np.array(ids)
        
        if(np.sum(ids==1) > 0):

            self.get_pose(corners[ids==1][0])
            points.append((bot_x, bot_y))
            self.drawCircle()
            
        if(np.sum(ids==2) > 0):

            self.get_pose(corners[ids==2][0])
            points.append((bot_x, bot_y))
            self.drawCircle()
            
            
        if(np.sum(ids==3) > 0):
            
            self.get_pose(corners[ids==3][0])
            points.append((bot_x, bot_y))
            self.drawCircle()

        cv.imshow('bots', image)
        cv.waitKey(1)

def main(args=None):
    rclpy.init(args=args)

    aruco_detector = ArUcoDetector()

    rclpy.spin(aruco_detector)

    aruco_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
