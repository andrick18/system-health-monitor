#!/usr/bin/env python3
#############################################################
# System Health Monitor - Alert System
# Author: Andrick Diatilo
# Version: v0.0.1
# Description: Reads the latest health log and sends an
#              email alert if any metric is critical
#############################################################

import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ------------ CONFIG ------------
LOG_FILE = "health_log.json"
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")

THRESHOLDS = {
    "cpu": 80.0,
    "memory": 80.0,
    "disk": 80.0
}
# --------------------------------

def get_latest_log():
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    return json.loads(lines[-1])

def send_email(alerts, data):
    subject = "🚨 EC2 Health Alert!"
    body = f"""
System Health Alert on your EC2 instance:

Timestamp: {data['timestamp']}
CPU Usage:    {data['cpu']}%
Memory Usage: {data['memory']}%
Disk Usage:   {data['disk']}%

Critical alerts:
"""
    for alert in alerts:
        body += f"  - {alert}\n"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

    print("Alert email sent!")

def check_health():
    data = get_latest_log()
    alerts = []

    if data["cpu"] > THRESHOLDS["cpu"]:
        alerts.append(f"CPU is at {data['cpu']}% (threshold: {THRESHOLDS['cpu']}%)")
    if data["memory"] > THRESHOLDS["memory"]:
        alerts.append(f"Memory is at {data['memory']}% (threshold: {THRESHOLDS['memory']}%)")
    if data["disk"] > THRESHOLDS["disk"]:
        alerts.append(f"Disk is at {data['disk']}% (threshold: {THRESHOLDS['disk']}%)")

    if alerts:
        print(f"CRITICAL: {len(alerts)} alert(s) found. Sending email...")
        send_email(alerts, data)
    else:
        print(f"All systems healthy — CPU: {data['cpu']}% | Memory: {data['memory']}% | Disk: {data['disk']}%")

if __name__ == "__main__":
    check_health()
