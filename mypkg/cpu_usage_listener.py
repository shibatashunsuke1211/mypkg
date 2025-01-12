# SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class CpuUsageSubscriber(Node):
    def __init__(self):
        super().__init__("cpu_usage_subscriber")

        self.subscription = self.create_subscription(
            Float32,
            "cpu_usage",
            self.cb,
            10
        )

    def cb(self, msg):
        # ロギング機能を使用してCPU使用率を表示
        self.get_logger().info(f"Received CPU Usage: {msg.data}%")

def main():
    rclpy.init()
    node = CpuUsageSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


