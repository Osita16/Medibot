from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    world = os.path.join(
        os.path.expanduser('~'),
        'medibot_ws/src/aws-robomaker-hospital-world/worlds/hospital.world'
    )

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', world,
             '-s', 'libgazebo_ros_init.so',
             '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        arguments=[os.path.expanduser('~/medibot_ws/src/medibot_description/urdf/medibot.urdf')],
        parameters=[{'use_sim_time': True}]
    )

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'medibot',
            '-file', os.path.expanduser('~/medibot_ws/src/medibot_description/urdf/medibot.urdf'),
            '-x', '0', '-y', '0', '-z', '0.2'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        rsp,
        spawn
    ])
