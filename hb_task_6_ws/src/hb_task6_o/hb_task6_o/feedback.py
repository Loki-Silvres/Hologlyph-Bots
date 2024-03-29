#! /usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Hologlyph Bots (HB) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 6 original of Hologlyph Bots (HB) Theme (eYRC 2023-24).
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
import yaml
##############################################################


with open(r"/home/lokisilvres/eyrc_hb/Protein1x_NVCTI_cam_calib/ost.yaml", 'r') as file:
    data = yaml.safe_load(file)

# print(data)

camera_matrix = np.array(data['camera_matrix']['data']).reshape((3, 3))
distortion_coefficients = np.array(data['distortion_coefficients']['data'])

bot_x, bot_y, bot_theta = 0.0, 0.0, 0.0
top_left = [0,0]
top_right = [500,0]
bottom_left = [0,500]
bottom_right = [500, 500]
flag  = False
points = []
image = 0
# cv.namedWindow('tracer')


class ArUcoDetector(Node):

    def __init__(self):
        super().__init__('ar_uco_detector')
        self.get_logger().info("Feedback has been started.")

        # Subscribe the topic /camera/image_raw

        self.img_sub = self.create_subscription(Image, 
                                    '/camera1/image_raw', 
                                    self.image_callback, 
                                    10)
        self.aruco = aruco.ArucoDetector(aruco.getPredefinedDictionary(aruco.DICT_4X4_1000),
                            aruco.DetectorParameters())
        self.bridge = CvBridge()

        self.det_ar_pub_1 = self.create_publisher(Pose2D,
                                                '/pen1_pose', 
                                                10)
        self.det_ar_pub_2 = self.create_publisher(Pose2D,
                                                '/pen2_pose', 
                                                10)
        self.det_ar_pub_3 = self.create_publisher(Pose2D,
                                                '/pen3_pose', 
                                                10)
        self.timer_time = 0.01
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
    
    def get_pose_1(self, bot_corners):
        
        bot_pos = np.sum(bot_corners,axis = 0)/4
        bot_x ,bot_y = bot_pos.astype('float')
        bot_top = bot_corners[1] - bot_corners[0]
        bot_top_vec = bot_top/np.linalg.norm(bot_top)
        bot_theta = np.arccos(bot_top_vec[0]).astype('float') 
        if(bot_top_vec[1]>0):
            bot_theta = 2 * np.pi - bot_theta           

        pose_x = bot_x - 250
        pose_y = 250 - bot_y
        pose_theta = bot_theta

        radial_distance = np.linalg.norm(np.array([pose_x, pose_y]))
        cosine = pose_x/radial_distance
        sine = pose_y/radial_distance
        reduction_factor = 0.94            # nearly perfect at 0.94 for bot height 13 cm
        reduction_exponent = 1             # 1
        radial_correction = reduction_factor ** reduction_exponent
        pose_x = radial_distance * cosine * radial_correction
        pose_y = radial_distance * sine * radial_correction
        if pose_theta > np.pi:
            pose_theta-=2*np.pi

        bot_x = pose_x + 250
        bot_y = 250 - pose_y 
        bot_theta = pose_theta


        bot_pose = Pose2D()
        bot_pose.x = bot_x
        bot_pose.y = bot_y 
        bot_pose.theta = bot_theta

        return bot_pose
    
    def get_pose_2(self, bot_corners):
        
        bot_pos = np.sum(bot_corners,axis = 0)/4
        bot_x ,bot_y = bot_pos.astype('float')
        bot_top = bot_corners[1] - bot_corners[0]
        bot_top_vec = bot_top/np.linalg.norm(bot_top)
        bot_theta = np.arccos(bot_top_vec[0]).astype('float') 
        if(bot_top_vec[1]>0):
            bot_theta = 2 * np.pi - bot_theta           

        pose_x = bot_x - 250
        pose_y = 250 - bot_y
        pose_theta = bot_theta

        radial_distance = np.linalg.norm(np.array([pose_x, pose_y]))
        cosine = pose_x/radial_distance
        sine = pose_y/radial_distance
        reduction_factor = 0.95            # nearly perfect at 0.94 for bot height 13 cm
        reduction_exponent = 1             # 1
        radial_correction = reduction_factor ** reduction_exponent
        pose_x = radial_distance * cosine * radial_correction
        pose_y = radial_distance * sine * radial_correction
        if pose_theta > np.pi:
            pose_theta-=2*np.pi

        bot_x = pose_x + 250
        bot_y = 250 - pose_y 
        bot_theta = pose_theta

        bot_pose = Pose2D()
        bot_pose.x = bot_x
        bot_pose.y = bot_y 
        bot_pose.theta = bot_theta

        return bot_pose
    
    def get_pose_3(self, bot_corners):
        
        bot_pos = np.sum(bot_corners,axis = 0)/4
        bot_x ,bot_y = bot_pos.astype('float')
        bot_top = bot_corners[1] - bot_corners[0]
        bot_top_vec = bot_top/np.linalg.norm(bot_top)
        bot_theta = np.arccos(bot_top_vec[0]).astype('float') 
        if(bot_top_vec[1]>0):
            bot_theta = 2 * np.pi - bot_theta           

        pose_x = bot_x - 250
        pose_y = 250 - bot_y
        pose_theta = bot_theta

        radial_distance = np.linalg.norm(np.array([pose_x, pose_y]))
        cosine = pose_x/radial_distance
        sine = pose_y/radial_distance
        reduction_factor = 0.93            # nearly perfect at 0.94 for bot height 13 cm
        reduction_exponent = 1             # 1
        radial_correction = reduction_factor ** reduction_exponent
        pose_x = radial_distance * cosine * radial_correction
        pose_y = radial_distance * sine * radial_correction
        if pose_theta > np.pi:
            pose_theta-=2*np.pi

        bot_x = pose_x + 250
        bot_y = 250 - pose_y 
        bot_theta = pose_theta


        bot_pose = Pose2D()
        bot_pose.x = bot_x
        bot_pose.y = bot_y 
        bot_pose.theta = bot_theta

        return bot_pose

    def drawCircle(self, color = [0,0,255]):

        global points
        global image

        # print(points)
        for pt in points:
            pt = np.array(pt).astype('int')
            image = cv.circle(image, (pt[0], pt[1]), 
                      radius= 1, color= color, 
                      thickness=-1,lineType=cv.LINE_4)
    def image_callback(self, msg: Image):

        #convert ROS image to opencv image

        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv_image = cv.undistort(cv_image, camera_matrix, distortion_coefficients)

        #Detect Aruco marker

        corners, ids, reject = self.aruco.detectMarkers(cv_image)
        # aruco.drawDetectedMarkers(cv_image, corners, ids, [0,0,255])

        global top_left
        global top_right
        global bottom_left
        global bottom_right 
        global flag
        global points
        global image
        
        top_left_ = [0,0]
        top_right_ = [500,0]
        bottom_left_ = [0,500]
        bottom_right_ = [500, 500]
        new_coord = np.float32([top_left_, top_right_, bottom_right_, bottom_left_])
        id_to_object = {8:'top_left', 
                        10:'top_right', 
                        4:'bottom_left', 
                        12:'bottom_right', 
                        1:'hb_bot_1', 
                        2:'hb_bot_2',
                        3:'hb_bot_3'}

        if(ids is not None and (8 in ids and 12 in ids and 10 in ids and 4 in ids) and flag!= True):
            corners = np.array(corners)
            ids = np.array(ids)
            top_left = corners[ids == 8][-1][0]
            bottom_right = corners[ids == 12][-1][2]
            top_right = corners[ids == 10][-1][1]
            bottom_left = corners[ids == 4][-1][3]
            flag = True
        
        if flag :
            current_coord = np.float32([top_left, top_right, bottom_right, bottom_left])
            matrix = cv.getPerspectiveTransform(current_coord, new_coord)
            cv_image = cv.warpPerspective(cv_image, matrix, (500, 500))
            
            # print(top_left)

            corners, ids, reject = self.aruco.detectMarkers(cv_image)
            # image = aruco.drawDetectedMarkers(cv_image, corners, ids, [0,0,255])
            aruco.drawDetectedMarkers(cv_image, corners, ids, [0,0,255])
            # cv.imshow('win', cv_image)
            # cv.waitKey(1)

            corners = np.array(corners)
            ids = np.array(ids)
            if(np.sum(ids==1) > 0):

                bot_pose = self.get_pose_1(corners[ids==1][0])
                self.det_ar_pub_1.publish(bot_pose)
                # points.append([bot_pose.x,bot_pose.y])
                # self.drawCircle(color = [0,0,255])

                if self.show_pose1:
                    self.get_logger().info(f"bot 1: x:{bot_pose.x}, y:{bot_pose.y}, theta:{bot_pose.theta:.3f}")
                    self.show_pose1 = False

            if(np.sum(ids==2) > 0):

                bot_pose = self.get_pose_2(corners[ids==2][0])
                self.det_ar_pub_2.publish(bot_pose)
                # points.append([bot_pose.x,bot_pose.y])
                # self.drawCircle(color = [0,255,0])

                if self.show_pose2:
                    self.get_logger().info(f"bot 2: x:{bot_pose.x}, y:{bot_pose.y}, theta:{bot_pose.theta:.3f}")
                    self.show_pose2 = False

            if(np.sum(ids==3) > 0):

                bot_pose = self.get_pose_3(corners[ids==3][0])
                self.det_ar_pub_3.publish(bot_pose)
                # points.append([bot_pose.x,bot_pose.y])
                # self.drawCircle(color = [255,0,0])
                if self.show_pose3:
                    self.get_logger().info(f"bot 3: x:{bot_pose.x}, y:{bot_pose.y}, theta:{bot_pose.theta:.3f}")
                    self.show_pose3 = False
            # cv.imshow('tracer', image)
            # cv.waitKey(1)
        
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
