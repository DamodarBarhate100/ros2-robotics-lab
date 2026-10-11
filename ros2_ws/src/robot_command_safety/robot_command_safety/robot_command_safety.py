# !/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Robot_cmd_Safety(Node):
    def __init__(self):
        super().__init__("robot_command_safety")
        self.get_logger().info("Robot command safety node created")

def main(args=None):
    rclpy.init(args=args)
    node = Robot_cmd_Safety()
    rclpy.shutdown()

if __name__ == '__main__':
    main()