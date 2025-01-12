# SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

class CpuUsagePublisher(Node):
    def __init__(self):
        super().__init__('cpu_usage_publisher')
        self.publisher_ = self.create_publisher(Float32, 'cpu_usage', 10)
        self.timer = self.create_timer(0.5, self.publish_cpu_usage) 

    def publish_cpu_usage(self):
        cpu_usage = psutil.cpu_percent(interval=None)
        msg = Float32()
        msg.data = cpu_usage
        self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = CpuUsagePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

