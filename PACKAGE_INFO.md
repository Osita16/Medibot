# Medibot Package Information

## Package Overview

### medibot_description
**Purpose**: Contains the robot's URDF/XACRO description files

**Key Files**:
- `urdf/medibot.urdf.xacro` - Robot model definition
- `launch/display.launch.py` - Launch file to visualize robot in RViz

**Dependencies**:
- robot_state_publisher
- joint_state_publisher
- xacro

**Usage**:
```bash
ros2 launch medibot_description display.launch.py
```

---

### medibot_gazebo
**Purpose**: Gazebo simulation environment and world files

**Key Files**:
- `worlds/hospital.world` - Hospital environment SDF file
- `launch/hospital_simulation.launch.py` - Launch Gazebo with hospital world and robot

**Dependencies**:
- gazebo_ros
- medibot_description

**Usage**:
```bash
ros2 launch medibot_gazebo hospital_simulation.launch.py
```

---

### medibot_navigation
**Purpose**: Navigation stack configuration and autonomous navigation

**Key Files**:
- `config/nav2_params.yaml` - Nav2 parameters
- `maps/hospital_map.yaml` - Map metadata
- `maps/hospital_map.pgm` - Map image
- `launch/slam.launch.py` - SLAM mapping
- `launch/navigation.launch.py` - Autonomous navigation
- `launch/slam_simulation.launch.py` - Combined SLAM + simulation
- `launch/full_navigation.launch.py` - Combined navigation + simulation
- `scripts/navigate_to_goal.py` - Automated navigation script

**Dependencies**:
- navigation2
- nav2_bringup
- slam_toolbox
- nav2_simple_commander

**Usage**:

*For mapping:*
```bash
ros2 launch medibot_navigation slam_simulation.launch.py
```

*For navigation:*
```bash
ros2 launch medibot_navigation full_navigation.launch.py
```

*For automated delivery:*
```bash
ros2 run medibot_navigation navigate_to_goal.py
```

---

## Robot Specifications

### Hardware Components
- **Base**: Differential drive robot
  - Length: 0.6 m
  - Width: 0.4 m
  - Height: 0.2 m
  - Weight: 15 kg

- **Wheels**: 
  - 2x driven wheels (radius: 0.1 m, width: 0.05 m)
  - Wheel separation: ~0.45 m

- **Caster**: 1x front caster for stability

- **Sensors**:
  - 360° Laser Scanner
    - Range: 0.1 m to 12.0 m
    - Resolution: 1° (360 samples)
    - Update rate: 10 Hz

### Performance Specifications
- **Maximum Linear Velocity**: 0.26 m/s
- **Maximum Angular Velocity**: 1.0 rad/s
- **Linear Acceleration**: 2.5 m/s²
- **Angular Acceleration**: 3.2 rad/s²

### Coordinate Frames
- `base_footprint` - Ground projection of robot center
- `base_link` - Robot base center
- `laser_frame` - Laser scanner frame
- `left_wheel_link`, `right_wheel_link` - Wheel frames
- `odom` - Odometry frame
- `map` - Map frame (when using navigation)

---

## Topics

### Published Topics
- `/cmd_vel` (geometry_msgs/Twist) - Velocity commands to robot
- `/odom` (nav_msgs/Odometry) - Odometry information
- `/scan` (sensor_msgs/LaserScan) - Laser scan data
- `/robot_description` (std_msgs/String) - Robot URDF
- `/tf` (tf2_msgs/TFMessage) - Transform tree
- `/map` (nav_msgs/OccupancyGrid) - Occupancy grid map (when mapping/navigating)

### Subscribed Topics
- `/cmd_vel` (geometry_msgs/Twist) - Velocity commands (by Gazebo plugin)
- `/goal_pose` (geometry_msgs/PoseStamped) - Navigation goal (by Nav2)
- `/initialpose` (geometry_msgs/PoseWithCovarianceStamped) - Initial pose for AMCL

---

## Parameters

### Key Navigation Parameters (nav2_params.yaml)

**Controller**:
- `max_vel_x`: 0.26 m/s
- `max_vel_theta`: 1.0 rad/s
- `xy_goal_tolerance`: 0.25 m
- `yaw_goal_tolerance`: 0.25 rad

**Costmaps**:
- Resolution: 0.05 m
- Robot radius: 0.3 m
- Inflation radius: 0.55 m

**AMCL**:
- Max particles: 2000
- Min particles: 500
- Update thresholds: 0.25 m / 0.2 rad

---

## Environment Details

### Hospital World Coordinates
- **World size**: 20m x 20m
- **Pharmacy**: (-8, -8) to (-6, -6)
- **Corridor**: Full width, between y=-6 and y=6
- **Patient Room 1**: (6, -8) to (10, -6)
- **Patient Room 2**: (6, 6) to (10, 10)

### Predefined Navigation Points
- `pharmacy`: (-7.0, -7.0)
- `patient_room_1`: (7.0, -7.0)
- `patient_room_2`: (7.0, 7.0)
- `corridor_center`: (0.0, 0.0)

---

## Common Commands

### Building
```bash
colcon build
colcon build --packages-select medibot_description
colcon build --symlink-install
```

### Sourcing
```bash
source install/setup.bash
source install/local_setup.bash
```

### Listing
```bash
ros2 pkg list | grep medibot
ros2 topic list
ros2 node list
```

### Debugging
```bash
ros2 topic echo /scan
ros2 topic hz /scan
ros2 topic info /cmd_vel
ros2 run tf2_tools view_frames
```

---

## Configuration Files

### URDF Parameters (medibot.urdf.xacro)
You can modify these properties:
- `base_width`, `base_length`, `base_height` - Robot dimensions
- `wheel_radius`, `wheel_width` - Wheel specifications
- `max_wheel_torque` - Motor torque limit
- Laser scanner properties (range, resolution, etc.)

### World Parameters (hospital.world)
You can customize:
- Room sizes and positions
- Wall positions
- Lighting
- Additional obstacles
- Physics parameters

### Navigation Parameters (nav2_params.yaml)
Tune these for better performance:
- Velocity limits
- Goal tolerances
- Costmap parameters
- Planner settings
- Recovery behavior parameters

---

## File Locations After Installation

After building with `colcon build`, files are installed in:

```
install/
├── medibot_description/
│   └── share/medibot_description/
│       ├── urdf/
│       └── launch/
├── medibot_gazebo/
│   └── share/medibot_gazebo/
│       ├── worlds/
│       └── launch/
└── medibot_navigation/
    └── share/medibot_navigation/
        ├── config/
        ├── launch/
        ├── maps/
        └── scripts/
```

---

For more information, see README.md and QUICKSTART.md.
