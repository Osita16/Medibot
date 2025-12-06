import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # ------- PLANNING PART 1: GAZEBO --------
    # Gazebo ko launch karne ka standard ROS 2 'unsafe' code
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'pause': 'true'}.items() # Gazebo ko 'pause' mode mein start karega
    )

    # ------- PLANNING PART 2: MEDIBOT (URDF) --------
    # Apne 'medibot' package ka raasta dhoondh
    pkg_medibot = get_package_share_directory('medibot')

    # Apne 'medibot.urdf' file ka poora raasta bana
    urdf_file_path = os.path.join(pkg_medibot, 'description', 'medibot.urdf')
    
    # URDF file ko padh (Yeh zaroori hai)
    robot_description_config = xacro.process_file(urdf_file_path)
    robot_description = robot_description_config.toxml() # XML string mein convert kar

    # ------- PLANNING PART 3: ROBOT STATE PUBLISHER --------
    # Yeh node ROS ko batata hai ki robot kaisa dikhta hai (TF transforms)
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}]
    )

    # ------- PLANNING PART 4: GAZEBO SPAWNER --------
    # Yeh node Gazebo ko batata hai ki robot ko simulation mein 'spawn' (paida) karo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', # URDF yahaan se lo
                   '-entity', 'medibot'],        # Robot ka naam 'medibot' rakho
        output='screen'
    )

    # ------- EXECUTION: Sabko ek saath launch karo --------
    return LaunchDescription([
        gazebo,
        node_robot_state_publisher,
        spawn_entity
    ])