#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleMonitor(Node):
    def __init__(self):
        super().__init__('turtle_monitor')
        self.subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)

    def listener_callback(self, msg):
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    turtle_monitor = TurtleMonitor()
    rclpy.spin(turtle_monitor)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
