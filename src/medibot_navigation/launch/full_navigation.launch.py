import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    """
    Launch file that starts both the hospital simulation and navigation stack.
    Use this after you have created a map using SLAM.
    """
    
    # Get package directories
    pkg_gazebo = get_package_share_directory('medibot_gazebo')
    pkg_navigation = get_package_share_directory('medibot_navigation')
    
    # Launch Gazebo simulation
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo, 'launch', 'hospital_simulation.launch.py')
        )
    )
    
    # Launch Navigation
    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_navigation, 'launch', 'navigation.launch.py')
        )
    )
    
    return LaunchDescription([
        gazebo_launch,
        nav_launch
    ])
