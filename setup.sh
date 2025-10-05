#!/bin/bash
# Setup script for Medibot workspace

set -e

echo "======================================"
echo "Medibot Workspace Setup"
echo "======================================"

# Check if ROS2 is installed
if [ -z "$ROS_DISTRO" ]; then
    echo "Error: ROS2 is not sourced. Please source your ROS2 installation first:"
    echo "  source /opt/ros/humble/setup.bash"
    exit 1
fi

echo "ROS2 Distribution: $ROS_DISTRO"

# Check for required ROS2 packages
echo ""
echo "Checking for required ROS2 packages..."

REQUIRED_PACKAGES=(
    "gazebo_ros"
    "navigation2"
    "nav2_bringup"
    "slam_toolbox"
    "robot_state_publisher"
    "joint_state_publisher"
    "xacro"
)

MISSING_PACKAGES=()

for pkg in "${REQUIRED_PACKAGES[@]}"; do
    if ! ros2 pkg list | grep -q "^${pkg}$"; then
        MISSING_PACKAGES+=("$pkg")
    fi
done

if [ ${#MISSING_PACKAGES[@]} -ne 0 ]; then
    echo ""
    echo "Missing required packages:"
    for pkg in "${MISSING_PACKAGES[@]}"; do
        echo "  - $pkg"
    done
    echo ""
    echo "Install them with:"
    echo "  sudo apt update"
    echo "  sudo apt install \\"
    for pkg in "${MISSING_PACKAGES[@]}"; do
        echo "    ros-${ROS_DISTRO}-${pkg//_/-} \\"
    done
    echo ""
    read -p "Would you like to install them now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo apt update
        for pkg in "${MISSING_PACKAGES[@]}"; do
            sudo apt install -y "ros-${ROS_DISTRO}-${pkg//_/-}"
        done
    else
        echo "Please install the missing packages before continuing."
        exit 1
    fi
fi

echo "All required packages are installed!"

# Build the workspace
echo ""
echo "Building workspace..."
cd "$(dirname "$0")"

if colcon build --symlink-install; then
    echo ""
    echo "======================================"
    echo "Build successful!"
    echo "======================================"
    echo ""
    echo "To use the workspace, run:"
    echo "  source install/setup.bash"
    echo ""
    echo "Quick start commands:"
    echo ""
    echo "1. Launch hospital simulation:"
    echo "   ros2 launch medibot_gazebo hospital_simulation.launch.py"
    echo ""
    echo "2. Launch SLAM for mapping:"
    echo "   ros2 launch medibot_navigation slam.launch.py"
    echo ""
    echo "3. Launch navigation (after creating a map):"
    echo "   ros2 launch medibot_navigation navigation.launch.py"
    echo ""
else
    echo ""
    echo "======================================"
    echo "Build failed!"
    echo "======================================"
    exit 1
fi
