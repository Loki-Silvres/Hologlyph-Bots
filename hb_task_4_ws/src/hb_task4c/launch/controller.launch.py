
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hb_task4c',
            executable='next_goal',
        ),
        Node(
            package='hb_task4c',
            executable='feedback',
        ),
        Node(
            package='hb_task4c',
            executable='controller_1',
        ),
        Node(
            package='hb_task4c',
            executable='controller_2',
        ),
        Node(
            package='hb_task4c',
            executable='controller_3',
        ),
        # Node(
        #     package='hb_task4c',
        #     executable='tracer',
        # )
    ])