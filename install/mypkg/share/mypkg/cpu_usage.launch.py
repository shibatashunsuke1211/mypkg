# SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    cpu_usage = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'cpu_usage',
            )

    listener_cpu_usage　= launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'cpu_usage.listener',
            output = 'screen'
            )

    return launch.LaunchDescription([check_cpu_stats, listener_cpu_stats])
