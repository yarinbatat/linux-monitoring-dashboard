#!/bin/bash

# Collect CPU usage (as float)
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

# Collect free disk space (remove the unit and keep just the number)
DISK_RAW=$(df -h / | tail -1 | awk '{print $4}')
DISK_NUM=$(echo $DISK_RAW | sed 's/[A-Za-z]//g')

# Collect memory usage percentage
MEMORY=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

# Create JSON with clean numeric values
echo "{
  \"cpu_usage\": \"$CPU\",
  \"disk_free\": \"$DISK_RAW\",
  \"disk_free_num\": $DISK_NUM,
  \"memory_usage\": \"$MEMORY\"
}" > data.json

echo "System stats updated at $(date)"
