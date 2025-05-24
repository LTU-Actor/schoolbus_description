import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def zenoh_daemon():
    return Node(
        package="rmw_zenoh_cpp",
        executable="rmw_zenohd",
        name="rmw_zenohd",
    )


# Robot description from URDF
urdf_path = os.path.join(get_package_share_directory("schoolbus_urdf"), "urdf", "schoolbus.urdf")
with open(urdf_path, "r") as f:
    robot_description = f.read()


def robot_state_publisher_node():
    return Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[
            {"use_sim_time": False},
            {"robot_description": robot_description},
        ],
    )


def joint_state_publisher_node():
    return Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        output="screen",
        parameters=[
            {"use_sim_time": False},
            {"robot_description": robot_description},
        ],
    )


def generate_launch_description():
    ld = LaunchDescription()
    # ld.add_action(zenoh_daemon())
    ld.add_action(robot_state_publisher_node())
    ld.add_action(joint_state_publisher_node())
    return ld
