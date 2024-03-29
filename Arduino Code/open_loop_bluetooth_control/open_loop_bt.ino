#include <Arduino.h>
#include <ESP32Servo.h>
#include <BluetoothSerial.h>
/* 
#####################################################################
#                         MY CODE                                   #
#####################################################################
*/
#define servo_rear_pin 25
#define servo_right_pin 26
#define servo_left_pin 27
#define servo_pen_pin 33

struct motor_speed{
  float left, right, rear;
};
typedef struct motor_speed mtr_spd;
mtr_spd motors;

struct vel{
  float x;
  float y;
  float w;
};

typedef struct vel Vel;

Servo servo_left, servo_right, servo_rear;
Servo servo_pen;
BluetoothSerial BlueTooth;

int pen_flag = 0;
int omega = 60.0;
double vel_threshold = 80;
int interval = 500;
int pen_up_angle = 30;
int pen_down_angle = 5;
double left_offset = 1.0;
double right_offset = 1.0;
double rear_offset = 1.0;

// dir = 0 => max clockwise rotation of servo
// dir = 180 => max counter-clockwise rotation of servo
// dir = 90 => no rotation of servo

void normalize(){
  if (abs(motors.left) > vel_threshold || abs(motors.right) > vel_threshold || abs(motors.rear) > vel_threshold){
    float norm = pow(pow(motors.left, 2.0) + pow(motors.right, 2.0) + pow(motors.rear, 2.0), 0.5);
    motors.left *= vel_threshold/norm;
    motors.right *= vel_threshold/norm;
    motors.rear *= vel_threshold/norm;
  }
}
void actuate(mtr_spd motors){

    Serial.print("Published motors speed: left: ");
    Serial.print((int)(motors.left));
    Serial.print(" right: ");
    Serial.print((int)motors.right);
    Serial.print(" rear: ");
    Serial.print((int)motors.rear);
    Serial.println();
  servo_left.write((90.0-motors.left)*left_offset);
  servo_right.write((90.0-motors.right)*right_offset);  // complete this
  servo_rear.write((90.0-motors.rear)*rear_offset);
}

void inverse_kinematics(Vel goal_vel){
  
  motors.left =  -1.0/3.0 * goal_vel.x +  5.77350269e-01  * goal_vel.y + 1.92450090 * goal_vel.w;
  motors.right = -1.0/3.0 * goal_vel.x + -5.77350269e-01  * goal_vel.y + 1.92450090 * goal_vel.w;
  motors.rear =   2.0/3.0 * goal_vel.x + -2.06957655e-17  * goal_vel.y + 1.92450090 * goal_vel.w;
  normalize();
  // matrix = np.array([[-1.0, -1.732/3, 1.0],[-1.0, 1.732/3, 1.0],[2.0, 0.0, 1.0]])
  // v1,v2,v3 = matrix @ np.array([[vx],[vy],[vtheta]])
}
void forward(int omega){
  Vel goal_vel = {0, omega, 0};
  inverse_kinematics(goal_vel);
  actuate(motors);
}

void backward(int omega){
  Vel goal_vel = {0, -omega, 0};
  inverse_kinematics(goal_vel);
  actuate(motors);
}

void left(int omega){
  Vel goal_vel = {-omega, 1, 0};
  inverse_kinematics(goal_vel);
  actuate(motors);
}
void right(int omega){
  Vel goal_vel = {omega, 0, 0};
  inverse_kinematics(goal_vel);
  actuate(motors);
}
void clockwise(int omega){
  Vel goal_vel = {0, 0, -omega};
  inverse_kinematics(goal_vel);
  actuate(motors);
}
void anticlockwise(int omega){
  Vel goal_vel = {0, 0, omega};
  inverse_kinematics(goal_vel);
  actuate(motors);
}
void pen_up(){
  servo_pen.write(pen_up_angle);
}
void pen_down(){
  servo_pen.write(pen_down_angle);

}
void stop(){
  servo_left.write(90);
  servo_right.write(90);
  servo_rear.write(90);
//  pen_up();
}
void setup() {
  Serial.begin(115200);
  BlueTooth.begin("Holo-bot-2");
  
/* 
#####################################################################
#                         MY CODE                                   #
#####################################################################
*/

  servo_left.attach(servo_left_pin);
  servo_right.attach(servo_right_pin);
  servo_rear.attach(servo_rear_pin);
  servo_pen.attach(servo_pen_pin);
  servo_left.write(90);
  servo_right.write(90);
  servo_rear.write(90);
  pen_up();
}

void loop() {

  if(BlueTooth.available()){
    char input = BlueTooth.read();
    switch (input)
    {
      case '1':
        forward(omega);
        break;
      case '2':
        backward(omega);
        break;
      case '3':
        left(omega);
        break;
      case '4':
        right(omega);
        break;
      case '5':
        clockwise(omega);
        break;
      case '6':
        anticlockwise(omega);
        break;
      case '0':
        if(pen_flag){
        pen_down();
        pen_flag = 1- pen_flag;
        }
        else{
        pen_up();
        pen_flag = 1- pen_flag;
        }
        break;
    }
    delay(interval);
  }
  stop();
   
  // pen_up();
  // delay(2000);
  // pen_down();
  // delay(2000);
}                                                                         
