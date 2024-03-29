import launch 
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '/hb_bot_1/left_wheel_force','/hb_bot_1/right_wheel_force','/hb_bot_1/left_wheel_force',
                '/hb_bot_1/rear_wheel_force','/hb_bot_2/left_wheel_force','/hb_bot_2/rear_wheel_force','/hb_bot_2/right_wheel_force',
                '/hb_bot_3/left_wheel_force','/hb_bot_3/rear_wheel_force','/hb_bot_3/right_wheel_force','/detected_aruco_1','/detected_aruco_2','/detected_aruco_3',
                '/hb_bot_1/goal','/hb_bot_2/goal','/hb_bot_3/goal'


                ],
            output='screen'
        )
    ])