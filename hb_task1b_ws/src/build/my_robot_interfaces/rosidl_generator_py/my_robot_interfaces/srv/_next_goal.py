# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_robot_interfaces:srv/NextGoal.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NextGoal_Request(type):
    """Metaclass of message 'NextGoal_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.srv.NextGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__next_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__next_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__next_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__next_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__next_goal__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NextGoal_Request(metaclass=Metaclass_NextGoal_Request):
    """Message class 'NextGoal_Request'."""

    __slots__ = [
        '_request_goal',
    ]

    _fields_and_field_types = {
        'request_goal': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.request_goal = kwargs.get('request_goal', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.request_goal != other.request_goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def request_goal(self):
        """Message field 'request_goal'."""
        return self._request_goal

    @request_goal.setter
    def request_goal(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'request_goal' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'request_goal' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._request_goal = value


# Import statements for member types

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_NextGoal_Response(type):
    """Metaclass of message 'NextGoal_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.srv.NextGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__next_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__next_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__next_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__next_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__next_goal__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NextGoal_Response(metaclass=Metaclass_NextGoal_Response):
    """Message class 'NextGoal_Response'."""

    __slots__ = [
        '_x_goal',
        '_y_goal',
        '_theta_goal',
        '_end_of_list',
    ]

    _fields_and_field_types = {
        'x_goal': 'double',
        'y_goal': 'double',
        'theta_goal': 'double',
        'end_of_list': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x_goal = kwargs.get('x_goal', float())
        self.y_goal = kwargs.get('y_goal', float())
        self.theta_goal = kwargs.get('theta_goal', float())
        self.end_of_list = kwargs.get('end_of_list', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.x_goal != other.x_goal:
            return False
        if self.y_goal != other.y_goal:
            return False
        if self.theta_goal != other.theta_goal:
            return False
        if self.end_of_list != other.end_of_list:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x_goal(self):
        """Message field 'x_goal'."""
        return self._x_goal

    @x_goal.setter
    def x_goal(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_goal' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_goal' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_goal = value

    @builtins.property
    def y_goal(self):
        """Message field 'y_goal'."""
        return self._y_goal

    @y_goal.setter
    def y_goal(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_goal' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_goal' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_goal = value

    @builtins.property
    def theta_goal(self):
        """Message field 'theta_goal'."""
        return self._theta_goal

    @theta_goal.setter
    def theta_goal(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'theta_goal' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'theta_goal' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._theta_goal = value

    @builtins.property
    def end_of_list(self):
        """Message field 'end_of_list'."""
        return self._end_of_list

    @end_of_list.setter
    def end_of_list(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'end_of_list' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'end_of_list' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._end_of_list = value


class Metaclass_NextGoal(type):
    """Metaclass of service 'NextGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.srv.NextGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__next_goal

            from my_robot_interfaces.srv import _next_goal
            if _next_goal.Metaclass_NextGoal_Request._TYPE_SUPPORT is None:
                _next_goal.Metaclass_NextGoal_Request.__import_type_support__()
            if _next_goal.Metaclass_NextGoal_Response._TYPE_SUPPORT is None:
                _next_goal.Metaclass_NextGoal_Response.__import_type_support__()


class NextGoal(metaclass=Metaclass_NextGoal):
    from my_robot_interfaces.srv._next_goal import NextGoal_Request as Request
    from my_robot_interfaces.srv._next_goal import NextGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
