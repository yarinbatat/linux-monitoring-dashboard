#!/bin/bash

echo "Starting system monitoring scheduler..."

# Initially collect data
./collect_info.sh

# Run in a loop every 60 seconds
while true; do
  sleep 60
  ./collect_info.sh
done
