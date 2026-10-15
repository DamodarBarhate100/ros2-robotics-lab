#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32

class Distance_Monitor_Node(Node):
    def __init__(self):
        super().__init__("distance_monitor")
        self.subscriber_ = self.create_subscription(msg_type=Float32,topic="obstacle_sensor",callback=self.callback_obstacle_sensor,qos_profile=10)
        self.get_logger().info("Initializing the Distance Monitor Node")

    def callback_obstacle_sensor(self, msg:Float32):
        self.get_logger().info("Received obstacle distance: "+str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = Distance_Monitor_Node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
