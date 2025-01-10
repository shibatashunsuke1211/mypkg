# SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CpuUsageubscriber(Node):
    def __init__(self):
        super().__init__("CpuUsageubscriber")
        self.create_subscription(String, "cpuusage", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = CpuUsageSubscriber()
    rclpy.spin(node)
~
