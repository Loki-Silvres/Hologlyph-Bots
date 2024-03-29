// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:srv/NextGoal.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__NEXT_GOAL__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__NEXT_GOAL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__NextGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__NextGoal_Request __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct NextGoal_Request_
{
  using Type = NextGoal_Request_<ContainerAllocator>;

  explicit NextGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->request_goal = 0ll;
    }
  }

  explicit NextGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->request_goal = 0ll;
    }
  }

  // field types and members
  using _request_goal_type =
    int64_t;
  _request_goal_type request_goal;

  // setters for named parameter idiom
  Type & set__request_goal(
    const int64_t & _arg)
  {
    this->request_goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__NextGoal_Request
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__NextGoal_Request
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NextGoal_Request_ & other) const
  {
    if (this->request_goal != other.request_goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const NextGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NextGoal_Request_

// alias to use template instance with default allocator
using NextGoal_Request =
  my_robot_interfaces::srv::NextGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__NextGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__NextGoal_Response __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct NextGoal_Response_
{
  using Type = NextGoal_Response_<ContainerAllocator>;

  explicit NextGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_goal = 0.0;
      this->y_goal = 0.0;
      this->theta_goal = 0.0;
      this->end_of_list = 0ll;
    }
  }

  explicit NextGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_goal = 0.0;
      this->y_goal = 0.0;
      this->theta_goal = 0.0;
      this->end_of_list = 0ll;
    }
  }

  // field types and members
  using _x_goal_type =
    double;
  _x_goal_type x_goal;
  using _y_goal_type =
    double;
  _y_goal_type y_goal;
  using _theta_goal_type =
    double;
  _theta_goal_type theta_goal;
  using _end_of_list_type =
    int64_t;
  _end_of_list_type end_of_list;

  // setters for named parameter idiom
  Type & set__x_goal(
    const double & _arg)
  {
    this->x_goal = _arg;
    return *this;
  }
  Type & set__y_goal(
    const double & _arg)
  {
    this->y_goal = _arg;
    return *this;
  }
  Type & set__theta_goal(
    const double & _arg)
  {
    this->theta_goal = _arg;
    return *this;
  }
  Type & set__end_of_list(
    const int64_t & _arg)
  {
    this->end_of_list = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__NextGoal_Response
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__NextGoal_Response
    std::shared_ptr<my_robot_interfaces::srv::NextGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NextGoal_Response_ & other) const
  {
    if (this->x_goal != other.x_goal) {
      return false;
    }
    if (this->y_goal != other.y_goal) {
      return false;
    }
    if (this->theta_goal != other.theta_goal) {
      return false;
    }
    if (this->end_of_list != other.end_of_list) {
      return false;
    }
    return true;
  }
  bool operator!=(const NextGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NextGoal_Response_

// alias to use template instance with default allocator
using NextGoal_Response =
  my_robot_interfaces::srv::NextGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces

namespace my_robot_interfaces
{

namespace srv
{

struct NextGoal
{
  using Request = my_robot_interfaces::srv::NextGoal_Request;
  using Response = my_robot_interfaces::srv::NextGoal_Response;
};

}  // namespace srv

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__NEXT_GOAL__STRUCT_HPP_
