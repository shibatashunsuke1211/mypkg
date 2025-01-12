#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

# ROS2 ワークスペースに移動
cd $dir/ros2_ws

# ROS2 パッケージをビルド
colcon build
source $dir/.bashrc

# ノードを直接実行して、CPU使用率をパブリッシュする
timeout 75 ros2 run mypkg cpu_usage_listener | tee /tmp/mypkg.log

# ログの内容を確認
cat /tmp/mypkg.log | grep -E 'CPU Usage: [0-9]+'




