#include <micro_ros_arduino.h>
#include <Arduino.h>
#include <ESP32Servo.h>
#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <geometry_msgs/msg/twist.h>
#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

const char* ssid = "LOKI";
const char* password = "12345678";
//const char* ssid = "Can you dig it";
//const char* password = "22122212";
// IPAddress local_IP(192, 168, 0, 1);
// IPAddress gateway(192, 168, 232, 255); // 192.168.232.255
// IPAddress subnet(255, 255, 255, 0);

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

int flag = 0;
int omega = 30.0;
double vel_threshold = 60;
int interval = 3000;
int pen_up_angle = 30;
int pen_down_angle = 5;

rcl_subscription_t subscriber;
geometry_msgs__msg__Twist msg;

rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;


#define LED_PIN 2
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}


struct twist_message {
    double lin_x;
    double lin_y;
    double lin_z;
    double angle_x;
    double angle_y;
    double angle_z;
};

void error_loop(){
  while(1){
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    delay(100);
  }
}


// dir = 0 => max clockwise rotation of servo
// dir = 180 => max counter-clockwise rotation of servo
// dir = 90 => no rotation of servo

void normalize(){
  if (abs(motors.left) > vel_threshold || abs(motors.left) > vel_threshold || abs(motors.left) > vel_threshold){
    float norm = pow(pow(motors.left, 2.0) + pow(motors.right, 2.0) + pow(motors.rear, 2.0), 0.5);
    motors.left *= vel_threshold/norm;
    motors.right *= vel_threshold/norm;
    motors.rear *= vel_threshold/norm;
  }
}
void actuate(mtr_spd motors){

  servo_left.write(90.0-motors.left);
  servo_right.write(90.0-motors.right);
  servo_rear.write(90.0-motors.rear);
}

void inverse_kinematics(Vel goal_vel){
  
  motors.left =  -1.0/3.0 * goal_vel.x +  5.77350269e-01  * goal_vel.y + 1.92450090 * goal_vel.w;
  motors.right = -1.0/3.0 * goal_vel.x + -5.77350269e-01  * goal_vel.y + 1.92450090 * goal_vel.w;
  motors.rear =   2.0/3.0 * goal_vel.x + .00000000000000  * goal_vel.y + 1.92450090 * goal_vel.w;
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
  Vel goal_vel = {-omega, 0, 0};
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
  pen_up();
}




void twist_subscription_callback(const void * msgin)
{
    const geometry_msgs__msg__Twist * msg = (const geometry_msgs__msg__Twist *)msgin;
    
    // Deal with the twist message recieved here
    int current = millis();
    Vel goal_vel;
    goal_vel.x = msg->linear.x;
    goal_vel.y = msg->linear.y;
    goal_vel.w = msg->angular.z;

    pen_down();
    inverse_kinematics(goal_vel);
    actuate(motors);

    Serial.print("Received speed: x: ");
    Serial.print(goal_vel.x);
    Serial.print(" y: ");
    Serial.print(goal_vel.y);
    Serial.println();
    Serial.print("Published motors speed: left: ");
    Serial.print(motors.left);
    Serial.print(" right: ");
    Serial.print(motors.right);
    Serial.print(" rear: ");
    Serial.print(motors.rear);
    Serial.println();

    while((millis()-current)<interval);
//    pen_up();
}








void setup() {
  Serial.begin(115200);
  Serial.println("Booting");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("Connection Failed! Rebooting...");
    delay(5000);
    ESP.restart();
  }

  // Port defaults to 3232
  // ArduinoOTA.setPort(3232);

  // Hostname defaults to esp3232-[MAC]
  // ArduinoOTA.setHostname("myesp32");

  // No authentication by default
  // ArduinoOTA.setPassword("admin");

  // Password can be set with it's md5 value as well
  // MD5(admin) = 21232f297a57a5a743894a0e4a801fc3
  // ArduinoOTA.setPasswordHash("21232f297a57a5a743894a0e4a801fc3");

  ArduinoOTA
    .onStart([]() {
      String type;
      if (ArduinoOTA.getCommand() == U_FLASH)
        type = "sketch";
      else // U_SPIFFS
        type = "filesystem";

      // NOTE: if updating SPIFFS this would be the place to unmount SPIFFS using SPIFFS.end()
      Serial.println("Start updating " + type);
    })
    .onEnd([]() {
      Serial.println("\nEnd");
    })
    .onProgress([](unsigned int progress, unsigned int total) {
      Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
    })
    .onError([](ota_error_t error) {
      Serial.printf("Error[%u]: ", error);
      if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
      else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
      else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
      else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
      else if (error == OTA_END_ERROR) Serial.println("End Failed");
    });

  ArduinoOTA.begin();

  Serial.println("Ready");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());//10.42.0.181

   pinMode(LED_PIN, OUTPUT);
   digitalWrite(LED_PIN, HIGH); 

  // Micro-ROS
   set_microros_wifi_transports("LOKI", "12345678", "10.42.0.1", 8888);
   pinMode(LED_PIN, OUTPUT);
   digitalWrite(LED_PIN, HIGH); 
//   delay(2000);

   allocator = rcl_get_default_allocator();
   RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));
   RCCHECK(rclc_node_init_default(&node, "hb_bot_3", "", &support));
   RCCHECK(rclc_subscription_init_default(
     &subscriber,
     &node,
     ROSIDL_GET_MSG_TYPE_SUPPORT(geometry_msgs, msg, Twist),
     "/cmd_vel_3"));
   RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
   RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &msg, &twist_subscription_callback, ON_NEW_DATA));
//   Serial.println("HI");
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
  pen_down();

}

void loop() {

   ArduinoOTA.handle();
   RCCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));
//   motors.left = 80;
//   motors.right = -80;
//   motors.rear = 0;
//   actuate(motors);
  stop();
}                                                                         
