#!/bin/bash -xv
#SPDX-FileCopyrightText: 2025 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 75 ros2 launch mypkg cpu_usage.launch | tee - /tmp/mypkg.log

cat /tmp/mypkg.log | 
grep 'CPU Usage:'


