# Medibot Quick Start Guide

This guide will help you get started with Medibot hospital automation system quickly.

## Prerequisites

Make sure you have:
- Ubuntu 22.04 LTS
- ROS2 Humble installed
- Gazebo installed

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Osita16/Medibot.git
   cd Medibot
   ```

2. **Run the setup script:**
   ```bash
   source /opt/ros/humble/setup.bash
   ./setup.sh
   ```

3. **Source the workspace:**
   ```bash
   source install/setup.bash
   ```

## Quick Start Scenarios

### Scenario 1: View the Robot Model

View the robot in RViz without simulation:

```bash
ros2 launch medibot_description display.launch.py
```

### Scenario 2: Launch Simulation Only

Start the Gazebo simulation with the hospital environment:

```bash
ros2 launch medibot_gazebo hospital_simulation.launch.py
```

Control the robot manually:
```bash
# In a new terminal
source install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Scenario 3: Create a Map (First Time)

Launch simulation with SLAM for mapping:

```bash
ros2 launch medibot_navigation slam_simulation.launch.py
```

Control the robot to explore (in a new terminal):
```bash
source install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Save the map when done exploring:
```bash
# In another terminal
source install/setup.bash
ros2 run nav2_map_server map_saver_cli -f ~/medibot_hospital_map
```

Update the map files:
```bash
cp ~/medibot_hospital_map.pgm src/medibot_navigation/maps/hospital_map.pgm
cp ~/medibot_hospital_map.yaml src/medibot_navigation/maps/hospital_map.yaml
```

### Scenario 4: Autonomous Navigation

After creating a map, launch full navigation:

```bash
ros2 launch medibot_navigation full_navigation.launch.py
```

#### Option A: Set goals using RViz2
1. In RViz2, click "2D Pose Estimate" button
2. Click on the map where the robot is and drag to set orientation
3. Click "Nav2 Goal" button
4. Click on the map where you want the robot to go

#### Option B: Use the navigation script
```bash
# In a new terminal
source install/setup.bash
ros2 run medibot_navigation navigate_to_goal.py
```

This will automatically navigate:
- Pharmacy → Patient Room 1
- Patient Room 1 → Patient Room 2  
- Patient Room 2 → Pharmacy

#### Option C: Send goals via command line
```bash
# Navigate to Patient Room 1
ros2 topic pub --once /goal_pose geometry_msgs/msg/PoseStamped "
header:
  frame_id: 'map'
pose:
  position: {x: 7.0, y: -7.0, z: 0.0}
  orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}"

# Navigate to Patient Room 2
ros2 topic pub --once /goal_pose geometry_msgs/msg/PoseStamped "
header:
  frame_id: 'map'
pose:
  position: {x: 7.0, y: 7.0, z: 0.0}
  orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}"

# Navigate back to Pharmacy
ros2 topic pub --once /goal_pose geometry_msgs/msg/PoseStamped "
header:
  frame_id: 'map'
pose:
  position: {x: -7.0, y: -7.0, z: 0.0}
  orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}"
```

## Common Commands

### View Topics
```bash
# List all topics
ros2 topic list

# View robot velocity commands
ros2 topic echo /cmd_vel

# View laser scan data
ros2 topic echo /scan

# View odometry
ros2 topic echo /odom
```

### View TF Tree
```bash
# Install if needed
sudo apt install ros-humble-tf2-tools

# Generate and view TF tree
ros2 run tf2_tools view_frames
evince frames.pdf
```

### Monitor Navigation
```bash
# View navigation path
ros2 topic echo /plan

# View robot position
ros2 topic echo /amcl_pose
```

## Troubleshooting

### Gazebo doesn't start
- Make sure you've sourced both ROS2 and the workspace: 
  ```bash
  source /opt/ros/humble/setup.bash
  source install/setup.bash
  ```

### Robot doesn't move
- Check if cmd_vel topic is publishing: `ros2 topic echo /cmd_vel`
- Verify teleop_twist_keyboard is running
- Check Gazebo is not paused (press spacebar in Gazebo)

### Navigation fails
- Ensure you've created a map first using SLAM
- Set the initial pose in RViz2 using "2D Pose Estimate"
- Check that laser scan is working: `ros2 topic echo /scan`

### SLAM not working
- Verify laser scanner is publishing: `ros2 topic echo /scan`
- Check odometry is working: `ros2 topic echo /odom`
- Ensure use_sim_time is set to true

## Next Steps

1. **Create your own map** by exploring the environment with SLAM
2. **Customize the hospital layout** by editing `src/medibot_gazebo/worlds/hospital.world`
3. **Tune navigation parameters** in `src/medibot_navigation/config/nav2_params.yaml`
4. **Add more locations** to the navigation script for automated delivery routes
5. **Implement custom behaviors** for specific hospital automation tasks

## Hospital Layout

```
    Top Wall
┌─────────────────────────────┐
│                             │
│  Patient    Corridor        │
│  Room 2                     │
│  (Red)                      │
│                             │
│                             │
├─────────────────────────────┤
│                             │
│                             │
│  Pharmacy   Corridor    Patient │
│  (Blue)                 Room 1  │
│  START                  (Green) │
│                             │
└─────────────────────────────┘
    Bottom Wall
```

**Coordinates:**
- Pharmacy (Start): (-7, -7)
- Patient Room 1: (7, -7)
- Patient Room 2: (7, 7)
- Corridor Center: (0, 0)

## Additional Resources

- [ROS2 Documentation](https://docs.ros.org/en/humble/)
- [Nav2 Documentation](https://navigation.ros.org/)
- [Gazebo Documentation](https://gazebosim.org/)
- [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox)

## Support

For issues and questions, please open an issue on GitHub:
https://github.com/Osita16/Medibot/issues
