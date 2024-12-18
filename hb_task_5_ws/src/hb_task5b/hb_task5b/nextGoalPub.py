import numpy as np
import rclpy
from rclpy.node import Node  
from my_robot_interfaces.msg import Goal           

class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')
        self.get_logger().info("Publisher Node is now active.")

        self.publish_goal_1 = self.create_publisher(Goal, 'hb_bot_1/goal', 10)
        self.publish_goal_2 = self.create_publisher(Goal, 'hb_bot_2/goal', 10)
        self.publish_goal_3 = self.create_publisher(Goal, 'hb_bot_3/goal', 10)
        
        self.timer = self.create_timer(5.0, self.publish_shapes)

    def publish_shapes(self):

        shape1_x, shape1_y, shape1_theta  = generate_right()
        shape2_x, shape2_y, shape2_theta  = generate_middle()
        shape3_x, shape3_y, shape3_theta  = generate_left()

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


def generate_right():
    
    num_points = 200
    theta = 0.0
    t1 = np.concatenate((0 * np.ones(50), np.linspace(0, 2 * np.pi/3, num_points)))
    x = 200 * np.cos(t1)
    y = 150 * np.sin(4 * t1)

    return x.tolist(), y.tolist(), theta

def generate_middle():

    num_points = 200
    theta = 0.0
    t1 = np.concatenate((2*np.pi/3 * np.ones(50), np.linspace(2 * np.pi/3, 4 * np.pi/3, num_points)))
    x = 200 * np.cos(t1)
    y = 150 * np.sin(4 * t1)

    return x.tolist(), y.tolist(), theta

def generate_left():
    
    num_points = 200
    theta = 0.0
    t1 = np.concatenate((4*np.pi/3 * np.ones(50), np.linspace(4 * np.pi/3, 2 * np.pi, num_points)))
    x = 200 * np.cos(t1)
    y = 150 * np.sin(4 * t1)

    return x.tolist(), y.tolist(), theta

def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()

    rclpy.spin(service_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

#######################################     DO NOT MODIFY THIS  FILE     ##########################################
