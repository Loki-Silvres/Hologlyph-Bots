// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from my_robot_interfaces:srv/NextGoal.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "my_robot_interfaces/srv/detail/next_goal__struct.h"
#include "my_robot_interfaces/srv/detail/next_goal__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool my_robot_interfaces__srv__next_goal__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[52];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("my_robot_interfaces.srv._next_goal.NextGoal_Request", full_classname_dest, 51) == 0);
  }
  my_robot_interfaces__srv__NextGoal_Request * ros_message = _ros_message;
  {  // request_goal
    PyObject * field = PyObject_GetAttrString(_pymsg, "request_goal");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->request_goal = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * my_robot_interfaces__srv__next_goal__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of NextGoal_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("my_robot_interfaces.srv._next_goal");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "NextGoal_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  my_robot_interfaces__srv__NextGoal_Request * ros_message = (my_robot_interfaces__srv__NextGoal_Request *)raw_ros_message;
  {  // request_goal
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->request_goal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "request_goal", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "my_robot_interfaces/srv/detail/next_goal__struct.h"
// already included above
// #include "my_robot_interfaces/srv/detail/next_goal__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool my_robot_interfaces__srv__next_goal__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[53];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("my_robot_interfaces.srv._next_goal.NextGoal_Response", full_classname_dest, 52) == 0);
  }
  my_robot_interfaces__srv__NextGoal_Response * ros_message = _ros_message;
  {  // x_goal
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_goal");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_goal = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_goal
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_goal");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_goal = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // theta_goal
    PyObject * field = PyObject_GetAttrString(_pymsg, "theta_goal");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->theta_goal = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // end_of_list
    PyObject * field = PyObject_GetAttrString(_pymsg, "end_of_list");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->end_of_list = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * my_robot_interfaces__srv__next_goal__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of NextGoal_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("my_robot_interfaces.srv._next_goal");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "NextGoal_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  my_robot_interfaces__srv__NextGoal_Response * ros_message = (my_robot_interfaces__srv__NextGoal_Response *)raw_ros_message;
  {  // x_goal
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_goal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_goal", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_goal
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_goal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_goal", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // theta_goal
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->theta_goal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "theta_goal", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // end_of_list
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->end_of_list);
    {
      int rc = PyObject_SetAttrString(_pymessage, "end_of_list", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
