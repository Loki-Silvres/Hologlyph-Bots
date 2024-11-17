# Task 2
## Task 2A

In this task, the robot autonomously draws shapes such as **rectangles, squares, and triangles**, based on randomly chosen functions (generate_rectangle(), generate_square(), generate_triangle()). A **Proportional Controller (P-Control)** is used for this task as well but unlike the previous task (1b), this task is more physically aligned with real-world dynamics through the application of wrench forces on the wheels as is the case with motors and friction, adjusting the robot's speed based on the error between its current position and the target trajectory. The inverse kinematics are utilized and the resultant force is used to drive the robot.

### **Build the workspace**
```bash
cd ~/Hologlyph-Bots/hb_task_2_ws/
colcon build
source install/setup.bash
```
### **Launch Gazebo Simulation**
```bash
ros2 launch hb_task_2a task2a.launch.py
```
![image](https://github.com/user-attachments/assets/6842e173-c549-40c4-922c-37a89aa76835)

### **Run controller launch file**
Runs service, camera feedback, line tracer and controller nodes.
```bash
ros2 launch hb_task2a controller.launch.py
```
![bots_screenshot_17 11 2024](https://github.com/user-attachments/assets/920b8034-1c6b-402b-bb4f-50f9ba8a534c)


