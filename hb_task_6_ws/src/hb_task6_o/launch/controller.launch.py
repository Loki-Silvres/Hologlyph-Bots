from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hb_task6_o',
            executable='next_goal',
        ),
        # Node(
        #     package='hb_task6_o',
        #     executable='feedback',
        # ),
        Node(
            package='hb_task6_o',
            executable='controller_1',
        ),
        Node(
            package='hb_task6_o',
            executable='controller_2',
        ),
        Node(
            package='hb_task6_o',
            executable='controller_3',
        ),
    ])
