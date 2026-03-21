# EC2 System Health Monitor

> Live and running on AWS EC2 

A lightweight system health monitoring tool for AWS EC2 instances built with Bash and Python.

## Author
Andrick Diatilo

## What it does
- Collects CPU, memory, and disk usage every minute via cron
- Logs all results to a JSON file for easy parsing
- Sends an email alert if any metric exceeds a threshold

## Tech Stack
- Bash
- Python 3
- AWS EC2
- Cron

## Project Structure
- `health_check.sh` — collects system metrics and logs to JSON
- `alert.py` — reads latest log and sends email if critical
- `health_log.json` — auto-generated log file
- `cron_log.txt` — auto-generated cron output log

## Docker

Pull and run from Docker Hub:
```bash
docker pull andrick18/system-health-monitor
docker run --rm \
  -e EMAIL_SENDER="youremail@gmail.com" \
  -e EMAIL_PASSWORD="your_app_password" \
  -e EMAIL_RECEIVER="youremail@gmail.com" \
  andrick18/system-health-monitor
```

## Usage

### Run manually
```bash
./health_check.sh
python3 alert.py
```

### Automate with cron
```bash
* * * * * cd /home/ubuntu/system-health-monitor && ./health_check.sh && python3 alert.py >> cron_log.txt 2>&1
```

## Thresholds
Default alert thresholds (configurable in `alert.py`):
- CPU: 80%
- Memory: 80%
- Disk: 80%

