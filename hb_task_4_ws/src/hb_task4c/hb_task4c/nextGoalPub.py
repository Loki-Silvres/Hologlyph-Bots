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
        self.get_logger().info("Publisher Node is now active.")

        self.publish_goal_1 = self.create_publisher(Goal, 'hb_bot_1/goal', 10)
        self.publish_goal_2 = self.create_publisher(Goal, 'hb_bot_2/goal', 10)
        self.publish_goal_3 = self.create_publisher(Goal, 'hb_bot_3/goal', 10)
        
        self.timer = self.create_timer(5.0, self.publish_shapes)

    def publish_shapes(self):

        tri_points = [[300, 100], [400, 100], [300, 200], [300, 100]]
        rectangle_points = [[200, 300], [400, 300], [400, 400], [200, 400], [200, 300]]
        hex_points = [[200, 150], [175, 200], [125, 200], [100, 150], [125, 100], [175, 100],[200, 150]]


        shape1_x, shape1_y, shape1_theta  = generate_triangle(tri_points,)
        shape2_x, shape2_y, shape2_theta  = generate_rectangle(rectangle_points,)
        shape3_x, shape3_y, shape3_theta  = generate_hexagon(hex_points,)

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

        self.publish_goal_1.publish(msg_bot_1)
        self.publish_goal_2.publish(msg_bot_2)
        self.publish_goal_3.publish(msg_bot_3)


def generate_hexagon(points):
    
    num_points = 60
    points = np.array(points)
    x, y = points[:,0], points[:,1]
    theta = 0.0
    
    x_left = np.linspace(x[0], x[1], num_points // 6)
    y_left = np.linspace(y[0], y[1], num_points // 6)
    x_top = np.linspace(x[1], x[2], num_points // 6)
    y_top = np.linspace(y[1], y[2], num_points // 6)
    x_right = np.linspace(x[2], x[3], num_points // 6)
    y_right = np.linspace(y[2], y[3], num_points // 6)
    x_bottom = np.linspace(x[3], x[4], num_points // 6)
    y_bottom = np.linspace(y[3], y[4], num_points // 6)
    x_5 = np.linspace(x[4], x[5], num_points // 6)
    y_5 = np.linspace(y[4], y[5], num_points // 6)
    x_6 = np.linspace(x[5], x[6], num_points // 6)
    y_6 = np.linspace(y[5], y[6], num_points // 6)
    
    x = np.concatenate((x_left, x_top, x_right, x_bottom, x_5, x_6))
    y = np.concatenate((y_left, y_top, y_right, y_bottom, y_5, y_6))
    # x = np.concatenate((x_left, x_top))
    # y = np.concatenate((y_left, y_top))

    # return x_left.tolist(), y_left.tolist(), theta
    return x.tolist(), y.tolist(), theta

def generate_triangle(points):

    num_points = 100
    points = np.array(points)
    x, y = points[:,0], points[:,1]
    theta = 0.0

    x_right = np.linspace(x[0], x[1], num_points // 3)
    y_right = np.linspace(y[0], y[1], num_points // 3)
 
    x_bottom = np.linspace(x[1], x[2], num_points // 3)
    y_bottom = np.linspace(y[1], y[2], num_points // 3)

    x_left = np.linspace(x[2], x[3], num_points // 3)
    y_left = np.linspace(y[2], y[3], num_points // 3)
    
    x = np.concatenate(( x_right, x_bottom, x_left))
    y = np.concatenate(( y_right, y_bottom, y_left))
    # print(x.tolist(), y.tolist())
    return x.tolist(), y.tolist(), theta

def generate_rectangle(points):
    
    num_points = 150
    points = np.array(points)
    x, y = points[:,0], points[:,1]
    theta = 0.0
    
    x_left = np.linspace(x[0], x[1], num_points // 4)
    y_left = np.linspace(y[0], y[1], num_points // 4)
    x_top = np.linspace(x[1], x[2], num_points // 4)
    y_top = np.linspace(y[1], y[2], num_points // 4)
    x_right = np.linspace(x[2], x[3], num_points // 4)
    y_right = np.linspace(y[2], y[3], num_points // 4)
    x_bottom = np.linspace(x[3], x[4], num_points // 4)
    y_bottom = np.linspace(y[3], y[4], num_points // 4)
    
    x = np.concatenate((x_left, x_top, x_right, x_bottom))
    y = np.concatenate((y_left, y_top, y_right, y_bottom))
    
    return x.tolist(), y.tolist(), theta

def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()

    rclpy.spin(service_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

#######################################     DO NOT MODIFY THIS  FILE     ##########################################
