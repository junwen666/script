#!/bin/bash
echo "rpc-pad": `date` >> /data/server/server_log/rpc_pad_server.log
PATH_LIB=./lib

CLASSPATH=./etc

JVM_PARAM='-Xms8g -Xmx8g -Xmn3g -Xss1m -XX:ParallelGCThreads=20 -XX:-DisableExplicitGC -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+CMSParallelRemarkEnabled  -XX:MetaspaceSize=128m -XX:+ParallelRefProcEnabled -XX:+CMSScavengeBeforeRemark'

JVM_GC='-XX:+PrintGCDetails -XX:+PrintGCDateStamps  -Xloggc:work/log/gc.log'


RUN_MAIN=cn.com.gc.hsz.pad.RpcPadMain

SERVER_NAME=rpc-pad

SERVER_PORT=29060

for jar in `ls $PATH_LIB/*.jar`

do

      CLASSPATH="$CLASSPATH:""$jar"

done

exec -a $SERVER_NAME java -server $JVM_PARAM  $JVM_GC $ARGS -classpath "$CLASSPATH" $RUN_MAIN --server.port=$SERVER_PORT 2>&1