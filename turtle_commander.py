#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class TurtleCommander(Node):
    def __init__(self):
        super().__init__('turtle_commander')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = random.uniform(0.1, 1.0)
        msg.angular.z = random.uniform(-1.0, 1.0)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    turtle_commander = TurtleCommander()
    rclpy.spin(turtle_commander)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
