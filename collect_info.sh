#!/bin/bash

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
DISK=$(df -h / | tail -1 | awk '{print $4}')
MEMORY=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

echo "{
  \"cpu_usage\": \"$CPU\",
  \"disk_free\": \"$DISK\",
  \"memory_usage\": \"$MEMORY\"
}" > data.json
