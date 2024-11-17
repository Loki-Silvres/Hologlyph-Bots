
# Hologlyph-Bots

![Hologlyph Bots Background](https://github.com/Loki-Silvres/Hologlyph-Bots/blob/main/Hologylph_bots_background.png?raw=true)

This repository contains the source code and resources developed by **Team eyrc_hb_1523** for the **E-Yantra 2023-2024 Hologlyph Bots** competition. This theme focuses on designing robots capable of creating artistic patterns or glyphs using holonomic drive systems. Holonomic drive robots offer superior control over movement, enabling translation along both x and y axes and rotation along the z-axis, a feature ideal for precision tasks in a confined arena.

---

## Overview

### **Key Features**
- Implements precise control algorithms for holonomic drive robots.
- Implemented Swarm Algorithms to accomplish collaborative tasks.
- Completes various tasks in a simulated arena and with physical hardware, demonstrating advanced robotics capabilities.
- Leverages robotic motion control to draw complex shapes like triangles, rectangles, and intricate mathematical functions.

### **Purpose**
This project is part of the E-Yantra Robotics Competition, where participants design robots to solve real-world challenges. In this *Hologlyph Bots* theme:
- Robots must autonomously navigate an region.
- Teams create artistic outputs leveraging the robot's mobility.

---

## Results

### **Submission Playlist**
- [Click here to view our Submission Playlist](https://youtube.com/playlist?list=PL_9--5xsFYUQ-xg70fmYQrzXn2ip_9O3C&si=z0v1tnEO03IPCXnJ)

---

### **Task Demonstrations**

#### **Task 5: Final Arena with Bots**
- **Arena Layout**  
  <img src="https://github.com/Loki-Silvres/Hologlyph-Bots/blob/main/Arena%20photos/Task_5_arena_with_Bots.jpg?raw=true" width="450" alt="Task 5 Arena with Bots" />

- **Task Result**  
  <img src="https://github.com/Loki-Silvres/Hologlyph-Bots/blob/main/Arena%20photos/Task_5_result.jpg?raw=true" width="450" alt="Task 5 Result" />

#### **Task 4: Artistic Shape Drawings**
- **Triangle Drawing**  
  <img src="https://github.com/Loki-Silvres/Hologlyph-Bots/blob/main/Arena%20photos/task_4_triangle.png?raw=true" width="320" alt="Task 4 Triangle Drawing" />

- **Rectangle Drawing**  
  <img src="https://github.com/Loki-Silvres/Hologlyph-Bots/blob/main/Arena%20photos/task_4_rectangle.png?raw=true" width="579" alt="Task 4 Rectangle Drawing" />

---

## Repository Structure

```plaintext
Hologlyph-Bots/
├── Arduino Code
├── Arena photos
├── Aruco_Markers
├── cam_calibration_640x480
├── hb_task1a_ws
├── hb_task1b_ws
├── hb_task_2_ws
├── hb_task_4_ws
├── hb_task_5_ws
├── hb_task_6_ws
├── PCB and Circuit
├── STL files
└── README.md
```

---

## Getting Started

### **Prerequisites**
- Python 3.8+
- Ubuntu 22.04 LTS
- ROS-HUMBLE (Robot Operating System)
- Gazebo-Classic Simulator
- Required libraries: `numpy`, `matplotlib`, `scipy`, `opencv-python`

### **Installation**
1. Clone the repository:
   ```bash
   cd 
   git clone https://github.com/Loki-Silvres/Hologlyph-Bots.git
   cd ~/Hologlyph-Bots/
   ```

2. Running Simulations:
   
- Run specific simulation tasks with the help of their corresponding documentations:

  - [Task1A](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/hb_task1a_ws#readme)
  - [Task1B](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/hb_task1b_ws#readme)
  - [Task2](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/hb_task_2_ws#readme)

3. Hardware Implementation:
   
- [STL files for 3D printing](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/STL%20files)
- [PCB and Circuit Design](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/PCB%20and%20Circuit)
- [Arena flex-printing](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/Arena%20photos)
- [Overhead Camera Calibration](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/cam_calibration_640x480)
- [ESP32-code](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/Arduino%20Code)
- [Aruco-Markers](https://github.com/Loki-Silvres/Hologlyph-Bots/tree/main/Aruco_Markers)

---


## Acknowledgments
- **E-Yantra**: For organizing this inspiring robotics competition.
- **Team Members**: EYRC_HB_1523:
  - [Alok Raj](https://github.com/Loki-Silvres)
  - [Aman Anand](https://github.com/Aman3214) 

