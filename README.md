# Medibot – Autonomous Hospital Delivery Robot

🚀 **An end-to-end ROS2 autonomous mobile robot for hospital logistics**

Medibot is designed to simulate real-world hospital delivery tasks where a robot can autonomously navigate from a pharmacy to patient rooms using modern robotics algorithms.

> 🔥 **Complete Robotics Pipeline:**
> Simulation → SLAM Mapping → Localization → Autonomous Navigation

---


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
Medibot/
├── src/
│   ├── medibot_description/
│   ├── medibot_gazebo/
│   └── medibot_navigation/
└── README.md
```

---

## ⚙️ Installation

```bash
sudo apt update
sudo apt install ros-humble-gazebo-ros-pkgs \
                 ros-humble-navigation2 \
                 ros-humble-nav2-bringup \
                 ros-humble-slam-toolbox
```

---

## ▶️ How to Run

### 1️⃣ Launch Simulation

```bash
cd ~/medibot_ws
colcon build
source install/setup.bash
ros2 launch medibot_gazebo hospital_simulation.launch.py
```

---

### 2️⃣ Run SLAM (First-Time Mapping)

```bash
ros2 launch medibot_navigation slam.launch.py
```

Control robot:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Save map:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/medibot_map
```

---

### 3️⃣ Run Autonomous Navigation

```bash
ros2 launch medibot_navigation navigation.launch.py
```

---

## 🎯 Set Navigation Goals

### 🖱️ Using RViz

* Click **2D Pose Estimate**
* Click **Nav2 Goal**

### 💻 Using CLI

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

* **Global Planner** → NavFn
* **Local Planner** → DWB Controller
* **Localization** → AMCL
* **Recovery** → Spin, Backup

---

## 💡 Why This Project?

* Demonstrates **complete robotics autonomy pipeline**
* Combines perception, localization, and planning
* Real-world application in hospital automation
* Strong portfolio project for robotics roles

---

## 🚧 Future Improvements

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
