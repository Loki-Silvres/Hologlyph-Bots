#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from functools import partial

class draw_circle(Node):
    def __init__(self):
        super().__init__(node_name='Draw_circle')
        self.flag1 = False
        self.flag11 = False
        self.flag2 = False
        self.t = 3.2
        self.get_logger().info("Draw circle has been started.")

        self.cmd_vel_pub1 = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10) 
        self.cmd_vel_pub2 = None
        self.pose_sub1 = self.create_subscription(
            Pose, '/turtle1/pose', self.send_vel_cmd1, 10)
        self.pose_sub2 = None
        self.timer1 = self.create_timer(self.t, self.set_flag1)
        self.timer2 = None

    def set_flag1(self):
        self.flag1 = True

    def set_flag2(self):
        self.flag2 = True

    def send_vel_cmd1(self, pose: Pose):
       
        if self.flag1 == False:
            # self.get_logger().info('inside if 2')
            msg = Twist()
            msg.linear.x = 2.0
            msg.angular.z = 2.0
            self.cmd_vel_pub1.publish(msg)
        else:
            # self.get_logger().info('inside else 1')
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.cmd_vel_pub1.publish(msg)
            if self.flag11 == False:
                self.set_spawn()
                self.pose_sub2 = self.create_subscription(
                        Pose, '/turtle2/pose', self.send_vel_cmd2, 10)
                self.cmd_vel_pub2 = self.create_publisher(
                        Twist, '/turtle2/cmd_vel', 10) 
                self.timer2 = self.create_timer(self.t*2, self.set_flag2)
                self.flag11 = True

    def send_vel_cmd2(self, pose: Pose):
        if self.flag2 == False:
            # self.get_logger().info('inside if 2')
            msg = Twist()
            msg.linear.x = 2.0
            msg.angular.z = -1.0
            self.cmd_vel_pub2.publish(msg)
        else:
            # self.get_logger().info('inside else 2')
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.cmd_vel_pub2.publish(msg)
            rclpy.shutdown()

    
    def set_spawn(self):
        god = self.create_client(Spawn, '/spawn')
        while not god.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Service...")
            
        created = Spawn.Request()
        created.x = 5.544444561004639
        created.y = 5.544444561004639
        created.theta = 0.0
        future = god.call_async(created)
        future.add_done_callback(partial(self.set_spawn_callback))

    def set_spawn_callback(self, future):

        try :
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call Failed: %r"%(e,))


    

def main(args = None):
    rclpy.init(args = args)
    node = draw_circle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
