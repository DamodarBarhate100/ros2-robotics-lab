import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/damodar-barhate/ros2-robotics-lab/ros2_multilang_telemetry/install/robot_telemetry_py'
