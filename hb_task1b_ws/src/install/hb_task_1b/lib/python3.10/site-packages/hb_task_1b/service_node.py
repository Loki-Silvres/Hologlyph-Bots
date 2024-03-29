#######################################     DO NOT MODIFY THIS  FILE     ##########################################

import rclpy
from rclpy.node import Node           
from std_msgs.msg import String
from my_robot_interfaces.srv import NextGoal             
import numpy as np
import random
import time
x = None
y = None
theta = None


class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')
        self.service = self.create_service(
            NextGoal, 'next_goal', self.next_goal_callback)
        self.publish_shape = self.create_publisher(String, '/shape', 10)
        self.flag = 0
        self.PI =  3.14
        self.shape_list = []
        self.logger_flag = 1

    def next_goal_callback(self, request, response):
        msg = String()

        goal_request = request.request_goal
        if request.request_goal < len(self.shape_list[1][0]):
            x = self.shape_list[1][0][(request.request_goal)]
            y = self.shape_list[1][1][(request.request_goal)]
            self.flag = 0
        else:
            self.flag = 1

        x = self.shape_list[1][0][(request.request_goal-1)]
        y = self.shape_list[1][1][(request.request_goal-1)]
        
        msg.data = self.shape_list[0]
        self.publish_shape.publish(msg)
        
        response.x_goal = x
        response.y_goal = y
        response.theta_goal = 0.0
        response.end_of_list = self.flag
        # self.get_logger().info(f"Received request: {request.request_goal}")
        if self.logger_flag == 1:
            self.get_logger().info("Service started...")
            self.logger_flag = 0
        time.sleep(1)
        return response

def generate_random_value(min_value=1, max_value=5):
    return random.randint(min_value, max_value)

def generate_rectangle(width=6, height=4, x_center=0, y_center=0, theta=0):
    half_width = width / 2
    half_height = height / 2
    x = np.array([-half_width, half_width, half_width, -half_width, -half_width])
    y = np.array([-half_height, -half_height, half_height, half_height, -half_height])
    # Apply rotation
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)
    x = x_center + x_rot
    y = y_center + y_rot
    return x.tolist(), y.tolist(), theta

def generate_triangle(side_length=6, x_center=0, y_center=0, theta=0):
    half_length = side_length / 2
    x = np.array([0, side_length, half_length, 0])
    y = np.array([0, 0, side_length * np.sqrt(3) / 2, 0])
    # Apply rotation
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)
    x = x_center + x_rot
    y = y_center + y_rot
    return x.tolist(), y.tolist(), theta

def generate_square(side_length=5, x_center=0, y_center=0, theta=0):
    half_length = side_length / 2
    x = np.array([-half_length, half_length, half_length, -half_length, -half_length])
    y = np.array([-half_length, -half_length, half_length, half_length, -half_length])
    # Apply rotation
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)
    x = x_center + x_rot
    y = y_center + y_rot
    return x.tolist(), y.tolist(), theta

def generate_infinity(x_center=0, y_center=0, scale=1, theta=0):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = x_center + scale * 2 * np.sin(t)
    y = y_center + scale * np.sin(2 * t)
    return x.tolist(), y.tolist(), theta

def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()
    shape_functions = ["generate_square", "generate_triangle", "generate_rectangle"]
    random_shape_function_name = random.choice(shape_functions)

    if random_shape_function_name == "generate_rectangle":
        shape_data = generate_rectangle()
    elif random_shape_function_name == "generate_square":
        shape_data = generate_square()
    elif random_shape_function_name == "generate_triangle":
        shape_data = generate_triangle()

    service_node.shape_list = [random_shape_function_name, shape_data]
    rclpy.spin(service_node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
###################################################################################################################
