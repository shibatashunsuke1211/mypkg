#SPDX-FileCopyrightText: 2024 Shunsuke Shibata
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talker > /tmp/mypkg.log

cat /tmp/mypkg.log
