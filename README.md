# Medibot – Autonomous Hospital Delivery Robot

🚀 **An end-to-end ROS2 autonomous mobile robot for hospital logistics**

Medibot is designed to simulate real-world hospital delivery tasks where a robot can autonomously navigate from a pharmacy to patient rooms using modern robotics algorithms.

> 🔥 **Complete Robotics Pipeline:**
> Simulation → SLAM Mapping → Localization → Autonomous Navigation

---

<img width="1072" height="854" alt="image" src="https://github.com/user-attachments/assets/bd013591-6ab7-4577-89de-845d1ef92121" />

---


## 🔄 System Pipeline

```text
Gazebo → SLAM → Map → AMCL → Nav2 → Goal Navigation
```

| Stage           | Description                                  |
| --------------- | -------------------------------------------- |
| 🧠 Simulation   | Robot spawned in Gazebo hospital environment |
| 🗺️ SLAM        | Builds map of unknown environment            |
| 💾 Map Saving   | Stores occupancy grid                        |
| 📍 Localization | AMCL estimates robot pose                    |
| 🧭 Planning     | Nav2 computes optimal path                   |
| 🚀 Execution    | Robot navigates autonomously                 |

---

## 🚀 Features

* 🤖 Custom differential drive robot (URDF/Xacro)
* 🏥 Hospital simulation environment (Gazebo)
* 🧭 Autonomous navigation using Nav2
* 🗺️ SLAM-based mapping (SLAM Toolbox)
* 📍 AMCL-based localization
* 🎯 Goal-based navigation (RViz + CLI)

---

## 🛠️ Tech Stack

| Category   | Tools        |
| ---------- | ------------ |
| Framework  | ROS2 Humble  |
| Simulation | Gazebo       |
| Navigation | Nav2         |
| Mapping    | SLAM Toolbox |
| Language   | Python       |

---

## 📁 Project Structure

```bash
medibot_ws/
└── src/
    ├── medibot_description/
    ├── medibot_gazebo/
    ├── medibot_navigation/
    └── aws-robomaker-hospital-world/
```

---

## ⚙️ Installation

```bash
sudo apt update
sudo apt install \
  ros-humble-gazebo-ros-pkgs \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-slam-toolbox
```

---
# ▶️ How to Run (Copy-Paste Ready)

> ⚠️ Open **5 terminals** and run commands in order.

---

# 🟢 Terminal 1 — Launch Simulation

```bash
source /opt/ros/humble/setup.bash
source ~/medibot_ws/install/setup.bash

export GAZEBO_MODEL_PATH=~/medibot_ws/src/aws-robomaker-hospital-world/models

ros2 launch medibot_gazebo sim.launch.py
```

---

# 🟢 Terminal 2 — Launch SLAM

```bash
source /opt/ros/humble/setup.bash
source ~/medibot_ws/install/setup.bash

ros2 launch nav2_bringup slam_launch.py use_sim_time:=true
```

---

# 🟢 Terminal 3 — Open RViz

```bash
source /opt/ros/humble/setup.bash

rviz2
```

---

# 🟢 RViz Setup

Set:

```text
Fixed Frame → map
```

Add:

* TF
* LaserScan → `/scan`
* Map → `/map`

---

# 🟢 Terminal 4 — Teleop Robot

```bash
source /opt/ros/humble/setup.bash
source ~/medibot_ws/install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Control Keys:

```text
i → forward
k → stop
j → left
l → right
```

---

# 🟢 Save Map

After exploring environment:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/medibot_map
```

---

# 🟢 Terminal 5 — Autonomous Navigation

Stop SLAM first, then run:

```bash
source /opt/ros/humble/setup.bash
source ~/medibot_ws/install/setup.bash

ros2 launch nav2_bringup navigation_launch.py \
use_sim_time:=true \
map:=~/medibot_map.yaml
```

---

# 🎯 Navigation in RViz

1. Click **2D Pose Estimate**
2. Set robot pose
3. Click **Nav2 Goal**
4. Select destination

Robot will autonomously navigate to target location.

---

# 🔍 Debugging Commands

## Check LaserScan

```bash
ros2 topic echo /scan
```

## Check Odometry

```bash
ros2 topic echo /odom
```

## Check TF Tree

```bash
ros2 run tf2_tools view_frames
```

---

# ✅ Expected Working Topics

```bash
/scan
/odom
/map
/tf
/cmd_vel
```

## 🔁 SLAM Mode (Optional – First Time Mapping)

```bash
ros2 launch nav2_bringup slam_launch.py use_sim_time:=true
```

Save map:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/medibot_map
```

---

## 🎯 Set Navigation Goals (CLI)

```bash
ros2 topic pub --once /goal_pose geometry_msgs/msg/PoseStamped "
header:
  frame_id: 'map'
pose:
  position:
    x: 7.0
    y: -7.0
  orientation:
    w: 1.0"
```

---

## 🏥 Example Tasks

| Task                 | From     | To      |
| -------------------- | -------- | ------- |
| 💊 Pharmacy → Room 1 | (-7, -7) | (7, -7) |
| 💊 Pharmacy → Room 2 | (-7, -7) | (7, 7)  |

---

## 🤖 Robot Specifications

* Differential drive mobile robot
* 360° LiDAR (0.1m – 12m range)
* Max speed: 0.26 m/s
* Angular velocity: 1.0 rad/s

---

## 🧭 Navigation Stack

* Global Planner → NavFn
* Local Planner → DWB Controller
* Localization → AMCL
* Recovery → Spin, Backup

---

## 💡 Why This Project?

* Demonstrates full robotics autonomy pipeline
* Combines perception, localization, and planning
* Real-world hospital automation use-case
* Strong portfolio project for robotics roles

---

## 🚧 Future Improvements

* Camera + YOLO integration 🤖
* Multi-goal scheduling
* Multi-robot coordination
* Dynamic obstacle handling
* Real robot deployment

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!

---

## 📜 License

Apache License 2.0

---

## 🙏 Acknowledgments

* ROS2 Nav2
* SLAM Toolbox
* Gazebo
