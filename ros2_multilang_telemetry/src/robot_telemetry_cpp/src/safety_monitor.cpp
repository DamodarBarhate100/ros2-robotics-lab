#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/float32.hpp"
#include "example_interfaces/msg/string.hpp"

class Safety_monitor: public rclcpp::Node{
    private:
        void callback_safety_monitor(const example_interfaces::msg::Float32::SharedPtr msg){
            RCLCPP_INFO(this->get_logger(), "%f", msg->data);
            
        }
        void publish_msg(){
            auto msg = example_interfaces::msg::String();
            msg.data = "SAFE";
            publisher_->publish(msg);
            
        }
        void callback_safety_status(const example_interfaces::msg::String::SharedPtr msg){
            RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
        }

        rclcpp::Subscription<example_interfaces::msg::Float32>::SharedPtr subscriber_;
        rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_1;
        rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
    
        public:
        // constructor
        Safety_monitor()
            :Node("safety_monitor"){
                publisher_ = this->create_publisher<example_interfaces::msg::String>
                ("robot/safety_status",10);
                subscriber_ = this->create_subscription<example_interfaces::msg::Float32>(
                    "obstacle_sensor",10,
                    std::bind(&Safety_monitor::callback_safety_monitor,this, std::placeholders::_1)
                );
                subscriber_1 = this->create_subscription<example_interfaces::msg::String>(
                    "robot/safety_status",10,
                    std::bind(&Safety_monitor::callback_safety_status,this, std::placeholders::_1)
                );
                timer_ = this->create_wall_timer(std::chrono::seconds(1),
                std::bind(&Safety_monitor::publish_msg,this));

                RCLCPP_INFO(this->get_logger(), "Initializing Safety Monitor Node");
            }
};

int main(int argc, char **argv){
    rclcpp::init(argc,argv);
    auto safety_monitor_node = std::make_shared<Safety_monitor>();
    rclcpp::spin(safety_monitor_node);
    rclcpp::shutdown();
      
}