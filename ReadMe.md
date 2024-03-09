# Turtle Fleet

## Overview
Turtle Fleet is a ROS 2 package designed to demonstrate basic ROS 2 concepts including topics, publishers, and subscribers through a simple turtlesim simulation. The package contains two main nodes: `turtle_commander` and `turtle_monitor`. The `turtle_commander` node controls a turtle by publishing random velocities, while the `turtle_monitor` node subscribes to these commands and replicates them for a second turtle, effectively making the second turtle follow the movements of the first.
