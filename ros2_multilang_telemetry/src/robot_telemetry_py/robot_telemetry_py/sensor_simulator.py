#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from example_interfaces.msg import Float32

class sensor_simulator(Node):
    def __init__(self):
        super().__init__("sensor_simulator")
        self.publisher_ = self.create_publisher(msg_type=Float32, topic="obstacle_sensor",qos_profile=10)
        self.timer_ = self.create_timer(1.0,self.publish_)
        self.get_logger().info("Initializing Sensor Simulator python node")

    def publish_(self):
        msg = Float32()
        msg.data = 0.5
        self.publisher_.publish(msg)
        self.get_logger().info("publishing obstacle distance: " + str(msg.data))
        



def main(args=None):
    rclpy.init(args=args)
    sensor_sim = sensor_simulator()
    rclpy.spin(sensor_sim)
    rclpy.shutdown()

if __name__ == "__main__":
    main()