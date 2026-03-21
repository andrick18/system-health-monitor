#!/bin/bash
###################################################
# System Health Monitor - Data Collector
# Author: Andrick Diatilo
# Version: v0.0.1
# Description: Collects CPU, memory, and disk usage
# and logs results to a file
###################################################

# Config
LOG_FILE="health_log.json"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# CPU usage (percentage)
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)

# Memory usage (percentage)
MEM_TOTAL=$(free | grep Mem | awk '{print $2}')
MEM_USED=$(free | grep Mem | awk '{print $3}')
MEM_PERCENT=$(awk "BEGIN {printf \"%.1f\", ($MEM_USED/$MEM_TOTAL)*100}")

# Disk usage (percentage of root partition)
DISK=$(df / | grep / | awk '{print $5}' | cut -d'%' -f1)

# Write to log file as JSON
echo "{\"timestamp\": \"$TIMESTAMP\", \"cpu\": $CPU, \"memory\": $MEM_PERCENT, \"disk\": $DISK}" >> $LOG_FILE

echo "Health check complete — $TIMESTAMP"
echo "CPU: $CPU% | Memory: $MEM_PERCENT% | Disk: $DISK%"
