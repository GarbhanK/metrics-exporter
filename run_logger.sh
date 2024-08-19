#!/usr/bin/env bash

# run logger in the background, send output to dev/null
nohup python3 metrics_exporter.py > /dev/null 2>&1 &

# find the process
ps ax | grep metrics_exporter.py

