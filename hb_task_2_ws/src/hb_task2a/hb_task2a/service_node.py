
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
import matplotlib.pyplot as plt

class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')
        self.service = self.create_service(
            NextGoal, 'next_goal', self.next_goal_callback)
        self.publish_shape = self.create_publisher(String, '/shape', 10)
        self.flag = 0
        self.PI =  3.141592
        self.shape_list = []
        self.logger_flag = 1
        self.shape_list = []
        self.logger_flag = 1
        self.x_values = []
        self.y_values = []
        self.count = 0

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

def generate_hexagon(side_length=100, x_center=0, y_center=0, theta=0, num_points=50):
    angles = np.linspace(0, 2 * np.pi, 6, endpoint=False) + theta
    x_vertices = x_center + side_length * np.cos(angles)
    y_vertices = y_center + side_length * np.sin(angles)
    
    # Generate linearly spaced points along the edges of the hexagon
    x_points = np.linspace(x_vertices[-1], x_vertices[0], num_points)
    y_points = np.linspace(y_vertices[-1], y_vertices[0], num_points)
    
    # Interpolate points for the hexagon
    x_interp = np.interp(np.linspace(0, 1, num_points), np.linspace(0, 1, 6), x_vertices)
    y_interp = np.interp(np.linspace(0, 1, num_points), np.linspace(0, 1, 6), y_vertices)
    
    return x_interp.tolist(), y_interp.tolist(), theta

def generate_rectangle(width=100, height=50, x_center=0, y_center=0, theta=0, num_points=50):
    half_width = width / 2
    half_height = height / 2
    
    # Generate linearly spaced points along the edges of the rectangle
    x_left = np.linspace(-half_width, half_width, num_points // 4)
    y_bottom = np.linspace(-half_height, -half_height, num_points // 4)
    x_right = np.linspace(half_width, -half_width, num_points // 4)
    y_top = np.linspace(half_height, half_height, num_points // 4)
    
    # Combine points to form the rectangle
    x = np.concatenate((x_left, x_right[::-1], x_right, x_left[::-1]))
    y = np.concatenate((y_bottom, y_bottom[::-1], y_top, y_top[::-1]))
    
    # Apply rotation
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)
    x = x_center + x_rot
    y = y_center + y_rot
    
    return x.tolist(), y.tolist(), theta

def generate_triangle(side_length=100, x_center=0, y_center=0, theta=0, num_points=50):
    # Calculate the height of the equilateral triangle
    height = (np.sqrt(3) / 2) * side_length
    
    # Define the vertices of the equilateral triangle
    x_vertices = np.array([0, side_length / 2, -side_length / 2, 0])
    y_vertices = np.array([height / 2, -height / 2, -height / 2, height / 2])
    
    # Apply rotation
    x_rot = x_vertices * np.cos(theta) - y_vertices * np.sin(theta)
    y_rot = x_vertices * np.sin(theta) + y_vertices * np.cos(theta)
    
    # Translate to the specified center
    x = x_center + x_rot
    y = y_center + y_rot
    
    # Generate linearly spaced points along the edges of the triangle
    x_left = np.linspace(x[2], x[0], num_points // 3)
    y_left = np.linspace(y[2], y[0], num_points // 3)
    x_right = np.linspace(x[0], x[1], num_points // 3)
    y_right = np.linspace(y[0], y[1], num_points // 3)
    x_bottom = np.linspace(x[1], x[2], num_points // 3)
    y_bottom = np.linspace(y[1], y[2], num_points // 3)
    
    # Combine points to form the triangle
    x = np.concatenate((x_left, x_right[1:], x_bottom[1:]))
    y = np.concatenate((y_left, y_right[1:], y_bottom[1:]))
    
    return x.tolist(), y.tolist(), theta

def generate_square(side_length=100, x_center=0, y_center=0, theta=0, num_points=50):
    half_length = side_length / 2
    
    # Define the vertices of the square
    x_vertices = np.array([-half_length, half_length, half_length, -half_length, -half_length])
    y_vertices = np.array([-half_length, -half_length, half_length, half_length, -half_length])
    
    # Apply rotation
    x_rot = x_vertices * np.cos(theta) - y_vertices * np.sin(theta)
    y_rot = x_vertices * np.sin(theta) + y_vertices * np.cos(theta)
    
    # Translate to the specified center
    x = x_center + x_rot
    y = y_center + y_rot
    
    # Generate linearly spaced points along the edges of the square
    x_left = np.linspace(x[3], x[0], num_points // 4)
    y_left = np.linspace(y[3], y[0], num_points // 4)
    x_top = np.linspace(x[0], x[1], num_points // 4)
    y_top = np.linspace(y[0], y[1], num_points // 4)
    x_right = np.linspace(x[1], x[2], num_points // 4)
    y_right = np.linspace(y[1], y[2], num_points // 4)
    x_bottom = np.linspace(x[2], x[3], num_points // 4)
    y_bottom = np.linspace(y[2], y[3], num_points // 4)
    
    # Combine points to form the square
    x = np.concatenate((x_left, x_top[1:], x_right[1:], x_bottom[1:]))
    y = np.concatenate((y_left, y_top[1:], y_right[1:], y_bottom[1:]))
    # print(x,y)
    return x.tolist(), y.tolist(), theta

def generate_decagon(side_length=100, x_center=0, y_center=0, theta=0, num_points=50):
    angles = np.linspace(0, 2 * np.pi, 10, endpoint=False) + theta
    x_vertices = x_center + side_length * np.cos(angles)
    y_vertices = y_center + side_length * np.sin(angles)
    
    # Generate linearly spaced points along the edges of the decagon
    x_points = np.linspace(x_vertices[-1], x_vertices[0], num_points)
    y_points = np.linspace(y_vertices[-1], y_vertices[0], num_points)
    
    # Interpolate points for the decagon
    x_interp = np.interp(np.linspace(0, 1, num_points), np.linspace(0, 1, 10), x_vertices)
    y_interp = np.interp(np.linspace(0, 1, num_points), np.linspace(0, 1, 10), y_vertices)
    
    return x_interp.tolist(), y_interp.tolist(), theta

def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()
    shape_functions = ["generate_square", "generate_triangle", "generate_rectangle", "generate_hexagon", "generate_decagon"]
    random_shape_function_name = random.choice(shape_functions)
    random_shape_function_name = 'generate_square'
    if random_shape_function_name   == "generate_rectangle":
        shape_data = generate_rectangle()
    elif random_shape_function_name == "generate_square":
        shape_data = generate_square()
    elif random_shape_function_name == "generate_triangle":
        shape_data = generate_triangle()
    elif random_shape_function_name == "generate_hexagon":
        shape_data = generate_hexagon()
    elif random_shape_function_name == "generate_decagon":
        shape_data = generate_decagon()

    service_node.shape_list = [random_shape_function_name, shape_data]
    rclpy.spin(service_node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
###################################################################################################################
