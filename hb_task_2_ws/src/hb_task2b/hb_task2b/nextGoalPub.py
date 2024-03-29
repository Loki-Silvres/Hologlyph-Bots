#######################################     DO NOT MODIFY THIS  FILE     ##########################################

import numpy as np
import matplotlib.pyplot as plt
from my_robot_interfaces.srv import NextGoal             
import rclpy
from rclpy.node import Node  
import random
import time
from my_robot_interfaces.msg import Goal           
from my_robot_interfaces.msg import Shape           


class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')

        self.publish_goal_1 = self.create_publisher(Goal, 'hb_bot_1/goal', 10)
        self.publish_goal_2 = self.create_publisher(Goal, 'hb_bot_2/goal', 10)
        self.publish_goal_3 = self.create_publisher(Goal, 'hb_bot_3/goal', 10)
        
        self.timer = self.create_timer(5.0, self.publish_shapes)

    def publish_shapes(self):

        tri_side_length = np.random.randint(50, 90)
        sq_side_length  = np.random.randint(50, 90)
        dec_side_length = np.random.randint(50, 80)

        tri_theta = np.random.uniform(0, 2*np.pi)
        sq_theta  = np.random.uniform(0, 2*np.pi)
        dec_theta = np.random.uniform(0, 2*np.pi)

        shape1_x, shape1_y, shape1_theta  = generate_triangle(tri_side_length, 300, 200, tri_theta, 100)
        shape2_x, shape2_y, shape2_theta  = generate_square(sq_side_length, 150, 250, sq_theta, 100)
        shape3_x, shape3_y, shape3_theta  = generate_decagon(dec_side_length, 320, 380, dec_theta, 100)

        msg_bot_1 = Goal()
        msg_bot_2 = Goal()
        msg_bot_3 = Goal()

        msg_bot_1.bot_id = 1
        msg_bot_1.x = shape1_x
        msg_bot_1.y = shape1_y
        msg_bot_1.theta = shape1_theta

        msg_bot_2.bot_id = 2
        msg_bot_2.x = shape2_x
        msg_bot_2.y = shape2_y
        msg_bot_2.theta = shape2_theta

        msg_bot_3.bot_id = 3
        msg_bot_3.x = shape3_x
        msg_bot_3.y = shape3_y
        msg_bot_3.theta = shape3_theta

        # msg_shape_info = Shape()
        # msg_shape_info.shape_dimension = [tri_side_length, sq_side_length, dec_side_length]
        # msg_shape_info.shape_theta = [tri_theta, sq_theta, dec_theta]

        self.publish_goal_1.publish(msg_bot_1)
        self.publish_goal_2.publish(msg_bot_2)
        self.publish_goal_3.publish(msg_bot_3)


def generate_decagon(side_length, x_center, y_center, theta, num_points):
    angles = np.linspace(0, 2 * np.pi, 11, endpoint=True) + theta
    x_vertices = x_center + side_length * np.cos(angles)
    y_vertices = y_center + side_length * np.sin(angles)
    
    x_points = np.linspace(x_vertices[-1], x_vertices[0], num_points)
    y_points = np.linspace(y_vertices[-1], y_vertices[0], num_points)
    
    x_interp = np.interp(np.linspace(0, 1, num_points), np.linspace(0, 1, 11), x_vertices)
    y_interp = np.interp(np.linspace(0, 1, num_points), np.linspace(0, 1, 11), y_vertices)
    
    return x_interp.tolist(), y_interp.tolist(), theta

def generate_triangle(side_length, x_center, y_center, theta, num_points):

    height = (np.sqrt(3) / 2) * side_length
    
    x_vertices = np.array([0, side_length / 2, -side_length / 2, 0])
    y_vertices = np.array([height / 2, -height / 2, -height / 2, height / 2])
    
    x_rot = x_vertices * np.cos(theta) - y_vertices * np.sin(theta)
    y_rot = x_vertices * np.sin(theta) + y_vertices * np.cos(theta)
    
    x = x_center + x_rot
    y = y_center + y_rot
    
    x_left = np.linspace(x[2], x[0], num_points // 3)
    y_left = np.linspace(y[2], y[0], num_points // 3)
    x_right = np.linspace(x[0], x[1], num_points // 3)
    y_right = np.linspace(y[0], y[1], num_points // 3)
    x_bottom = np.linspace(x[1], x[2], num_points // 3)
    y_bottom = np.linspace(y[1], y[2], num_points // 3)
    
    x = np.concatenate((x_left, x_right[1:], x_bottom[1:]))
    y = np.concatenate((y_left, y_right[1:], y_bottom[1:]))
    
    return x.tolist(), y.tolist(), theta

def generate_square(side_length, x_center, y_center, theta, num_points):
    half_length = side_length / 2
    
    x_vertices = np.array([-half_length, half_length, half_length, -half_length, -half_length])
    y_vertices = np.array([-half_length, -half_length, half_length, half_length, -half_length])
    
    x_rot = x_vertices * np.cos(theta) - y_vertices * np.sin(theta)
    y_rot = x_vertices * np.sin(theta) + y_vertices * np.cos(theta)
    
    x = x_center + x_rot
    y = y_center + y_rot
    
    x_left = np.linspace(x[3], x[0], num_points // 4)
    y_left = np.linspace(y[3], y[0], num_points // 4)
    x_top = np.linspace(x[0], x[1], num_points // 4)
    y_top = np.linspace(y[0], y[1], num_points // 4)
    x_right = np.linspace(x[1], x[2], num_points // 4)
    y_right = np.linspace(y[1], y[2], num_points // 4)
    x_bottom = np.linspace(x[2], x[3], num_points // 4)
    y_bottom = np.linspace(y[2], y[3], num_points // 4)
    
    x = np.concatenate((x_left, x_top[1:], x_right[1:], x_bottom[1:]))
    y = np.concatenate((y_left, y_top[1:], y_right[1:], y_bottom[1:]))
    
    return x.tolist(), y.tolist(), theta



def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()

    rclpy.spin(service_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

#######################################     DO NOT MODIFY THIS  FILE     ##########################################
