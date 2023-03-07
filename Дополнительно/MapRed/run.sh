#! /usr/bin/env bash

OUT_DIR="110_ievlev"
NUM_REDUCERS=9

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.job.name="exercise 110" \
	-D mapreduce.job.reduces=${NUM_REDUCERS} \
	-files mapper.py,reducer.py \
	-mapper "python3 ./mapper.py" \
    	-reducer "python3 ./reducer.py" \
	-input /data/ids \
	-output ${OUT_DIR} > /dev/null

hdfs dfs -text ${OUT_DIR}/part-00000 | head -50
