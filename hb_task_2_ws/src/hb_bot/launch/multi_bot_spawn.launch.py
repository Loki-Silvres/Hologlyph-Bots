import os
import xacro
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    actions = []
    pos_x = [-4.0, 0.0,  4.5]
    pos_y = [-9.0, -9.0, -9.0]
    share_dir = get_package_share_directory('hb_bot')

    for i in range(1, 4): 
        bot_name = 'hb_bot_' + str(i)
        xacro_file = os.path.join(share_dir,'urdf', bot_name + '.urdf.xacro')
        robot_description_config = xacro.process_file(xacro_file)
        robot = robot_description_config.toxml()

        robot_state_publisher_node = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=bot_name,
            parameters=[
                {'robot_description': robot}
            ]
        )
        actions.append(robot_state_publisher_node)
        # Spawn Urdf
        urdf_spawn_node = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            namespace=bot_name,
               # arguments=['-entity', 'ebot', '-topic', 'robot_description_ebot', '-x', '1.1', '-y', '4.35', '-z', '0.1', '-Y', '3.14'],
        arguments=['-entity', bot_name, '-topic', 'robot_description', '-x', str(pos_x[i-1]), '-y', str(pos_y[i-1]), '-z', '0.1', '-Y', '0.0'],
        output='screen'

        )
        actions.append(urdf_spawn_node)


    ld = LaunchDescription()
    for action in actions:
        ld.add_action(action)

    return ld