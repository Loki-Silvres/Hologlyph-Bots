# Task 1B

In this task, the robot autonomously draws shapes such as **rectangles, squares, and triangles**, based on randomly chosen functions (generate_rectangle(), generate_square(), generate_triangle()). A **Proportional Controller (P-Control)** is used for precise navigation, adjusting the robot's speed based on the error between its current position and the target trajectory.

### **Build the workspace**
```bash
cd ~/Hologlyph-Bots/hb_task1b_ws/
colcon build
source install/setup.bash
```

### **Launch Gazebo Simulation**
```bash
ros2 launch hb_task_1b gazebo.launch.py
```

![Screenshot from 2024-11-17 08-09-09](https://github.com/user-attachments/assets/ce2bd159-a38e-4f70-ad3f-ceb32e069798)

### Run service node and controller
```bash
ros2 launch hb_task_1b hb_task1b.launch.py
```
