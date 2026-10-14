#include "rclcpp/rclcpp.hpp"

class Safety_monitor: public rclcpp::Node{
    private:

    public:
        // constructor
        Safety_monitor()
            :Node("safety_monitor"){
                RCLCPP_INFO(this->get_logger(), "Initializing Safery Monitor Node");
            }
};

int main(int argc, char **argv){
    rclcpp::init(argc,argv);
    auto safety_monitor_node = std::make_shared<Safety_monitor>();
    rclcpp::shutdown();
      
}