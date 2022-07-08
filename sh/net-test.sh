#!/bin/bash

#log_file=/tmp/ping/ping`date +"%Y%m%d"`.log               # 网络日志文件
log_file=/tmp/ping/ping.log                                # 网络日志文件

while true
do
	result=`ping -c 4 -W 1 baidu.com | grep 'packet loss' | awk -F 'packet loss' '{ print $1 }' | awk '{ print $NF }' | sed 's/%//g'`

	if [ $result -gt 0 ]
	 then
		echo "`date '+%Y-%m-%d %H:%M:%S'`:ping result=$result" >> $log_file
	fi
done