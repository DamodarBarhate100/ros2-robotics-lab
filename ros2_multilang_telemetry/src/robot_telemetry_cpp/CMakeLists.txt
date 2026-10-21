cmake_minimum_required(VERSION 3.8)
project(robot_telemetry_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(safety_monitor src/safety_monitor.cpp)
ament_target_dependencies(safety_monitor rclcpp example_interfaces)

install(TARGETS 
  safety_monitor
  DESTINATION lib/${PROJECT_NAME}

)

ament_package()
