#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

# ワークスペースのディレクトリを設定
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2 環境をセットアップ
source /opt/ros/foxy/setup.bash  # ROS 2のインストールパスを確認
source $dir/ros2_ws/install/setup.bash  # 自分のワークスペースのパス

# ワークスペースに移動してビルド
cd $dir/ros2_ws
colcon build --symlink-install

# ビルドが成功したらROS 2 ノードを起動
echo "Starting the CPU usage publisher..."
timeout 10 ros2 run mypkg cpu_usage_publisher  # mypkgパッケージ内での実行例

# CPU使用率トピックのメッセージを確認
echo "Waiting for messages on the cpu_usage topic..."
ros2 topic echo /cpu_usage

# ログファイルを確認
echo "Showing log files..."
cat /tmp/mypkg.log

