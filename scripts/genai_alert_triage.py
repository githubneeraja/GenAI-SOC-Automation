import os
import json
from datetime import datetime

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

def analyze_alert(alert):
    """
    Simulates GenAI analysis of a SOC alert
    """
    report = f"""
# 🛡️ Incident Report

## 📌 Summary
Multiple failed login attempts detected for user **{alert['username']}**
from source IP **{alert['source_ip']}** on host **{alert['host']}**.

## 🚨 Severity
**{alert.get('severity', 'Medium')}**

## 🧠 MITRE ATT&CK Mapping
- **T1110 – Brute Force**

## 🔍 Analysis
The repeated login failures indicate a possible brute-force
or credential-stuffing attempt targeting a privileged account.

## ✅ Recommended Response Actions
1. Block source IP **{alert['source_ip']}**
2. Reset password for user **{alert['username']}**
3. Enable MFA if not already enabled
4. Monitor authentication logs for additional attempts

## 🕒 Report Generated
{datetime.now()}
"""
    return report

# Load alert from alerts folder
alert_file_path = os.path.join("alerts", "splunk_alert.json")

if not os.path.exists(alert_file_path):
    print(f"❌ Alert file not found: {alert_file_path}")
    print("Make sure 'splunk_alert.json' exists in 'alerts/' folder.")
    exit(1)

with open(alert_file_path, "r", encoding="utf-8") as f:
    alert = json.load(f)

# Generate incident report
report_file_path = os.path.join("reports", "incident_report.md")
with open(report_file_path, "w", encoding="utf-8") as f:
    f.write(analyze_alert(alert))

print(f"✅ Incident report generated (Mock GenAI) → {report_file_path}")
