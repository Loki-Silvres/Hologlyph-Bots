
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_prefix

pkg_name='hb_world'

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_models_dir = get_package_share_directory(pkg_name)

    install_dir = get_package_prefix(pkg_name)

    if 'GAZEBO_MODEL_PATH' in os.environ:
        gazebo_models_path = os.path.join(pkg_models_dir, 'models')
        os.environ['GAZEBO_MODEL_PATH'] = gazebo_models_path
    else:
        os.environ['GAZEBO_MODEL_PATH'] =  install_dir + "/share"

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )    

    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(pkg_models_dir, 'worlds', 'gazebo.world'), ''], # Change name of world file if required.
          description='SDF world file'),
        gazebo
       
    ])