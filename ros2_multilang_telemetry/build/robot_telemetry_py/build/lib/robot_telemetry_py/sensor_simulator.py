import rclpy
from rclpy.node import Node 

class sensor_simulator(Node):
    def __init__(self):
        super().__init__("sensor_simulator")
        self.get_logger().info("Initializing Sensor Simulator python node")




def main(args=None):
    rclpy.init(args=args)
    sensor_sim = sensor_simulator()
    # rclpy.spin(sensor_sim)
    rclpy.shutdown()

if __name__ == "__main__":
    main()