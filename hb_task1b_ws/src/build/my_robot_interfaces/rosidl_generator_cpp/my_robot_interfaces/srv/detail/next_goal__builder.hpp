// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/NextGoal.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__NEXT_GOAL__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__NEXT_GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/srv/detail/next_goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_NextGoal_Request_request_goal
{
public:
  Init_NextGoal_Request_request_goal()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::NextGoal_Request request_goal(::my_robot_interfaces::srv::NextGoal_Request::_request_goal_type arg)
  {
    msg_.request_goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::NextGoal_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::NextGoal_Request>()
{
  return my_robot_interfaces::srv::builder::Init_NextGoal_Request_request_goal();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_NextGoal_Response_end_of_list
{
public:
  explicit Init_NextGoal_Response_end_of_list(::my_robot_interfaces::srv::NextGoal_Response & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::NextGoal_Response end_of_list(::my_robot_interfaces::srv::NextGoal_Response::_end_of_list_type arg)
  {
    msg_.end_of_list = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::NextGoal_Response msg_;
};

class Init_NextGoal_Response_theta_goal
{
public:
  explicit Init_NextGoal_Response_theta_goal(::my_robot_interfaces::srv::NextGoal_Response & msg)
  : msg_(msg)
  {}
  Init_NextGoal_Response_end_of_list theta_goal(::my_robot_interfaces::srv::NextGoal_Response::_theta_goal_type arg)
  {
    msg_.theta_goal = std::move(arg);
    return Init_NextGoal_Response_end_of_list(msg_);
  }

private:
  ::my_robot_interfaces::srv::NextGoal_Response msg_;
};

class Init_NextGoal_Response_y_goal
{
public:
  explicit Init_NextGoal_Response_y_goal(::my_robot_interfaces::srv::NextGoal_Response & msg)
  : msg_(msg)
  {}
  Init_NextGoal_Response_theta_goal y_goal(::my_robot_interfaces::srv::NextGoal_Response::_y_goal_type arg)
  {
    msg_.y_goal = std::move(arg);
    return Init_NextGoal_Response_theta_goal(msg_);
  }

private:
  ::my_robot_interfaces::srv::NextGoal_Response msg_;
};

class Init_NextGoal_Response_x_goal
{
public:
  Init_NextGoal_Response_x_goal()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NextGoal_Response_y_goal x_goal(::my_robot_interfaces::srv::NextGoal_Response::_x_goal_type arg)
  {
    msg_.x_goal = std::move(arg);
    return Init_NextGoal_Response_y_goal(msg_);
  }

private:
  ::my_robot_interfaces::srv::NextGoal_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::NextGoal_Response>()
{
  return my_robot_interfaces::srv::builder::Init_NextGoal_Response_x_goal();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__NEXT_GOAL__BUILDER_HPP_
