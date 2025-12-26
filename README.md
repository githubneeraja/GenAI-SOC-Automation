
# GenAI-SOC-Automation
Mock GenAI SOC automation project

Genai Soc Readme
GenAI-Powered SOC Automation (Mock Version)
Overview

This project demonstrates a Mock GenAI SOC automation workflow. It simulates how security alerts from a SIEM (like Splunk or Wazuh) can be analyzed automatically and converted into incident reports.

Fully offline (no API key needed)

Beginner-friendly and safe for GitHub

Demonstrates Python + Cybersecurity integration

Tools & Folder Structure
Tools

Python 3.10+

VS Code (recommended)

Git

Folder Structure
GenAI-SOC-Automation/
GenAI-SOC-Automation/
├── scripts/
│   └── genai_alert_triage.py      # Mock GenAI alert analysis script
├── alerts/
│   └── splunk_alert.json          # Simulated SIEM alerts
├── reports/
│   └── incident_report.md         # Generated incident report
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies

 How It Works

Reads JSON alerts from the alerts/ folder.

Uses a Mock GenAI function to analyze alerts:

Summarizes the alert

Assigns severity

Maps to MITRE ATT&CK

Suggests response actions

Generates a Markdown incident report in reports/incident_report.md.

 How to Explore (Safe Version)

This project uses a Mock GenAI script to generate incident reports from alerts.
Since it’s fully offline, you don’t need to run it to see the workflow.

Check the folder structure and sample files:

alerts/splunk_alert.json → Example alert

reports/incident_report.md → Example report


 Running the script is safe in your own environment, but you don’t need it to explore or understand the project.

 Key Features

Automates SOC alert triage

Generates professional incident reports

Offline and safe for GitHub

Clean folder structure

Beginner-friendly and interview-ready

 Interview Explanation

“I built a Mock GenAI SOC automation project that simulates SIEM alerts, analyzes them automatically, and generates incident reports. This demonstrates alert triage automation and reduces analyst workload.”

 Next Steps / Enhancements

Add multiple alerts and batch report generation

Integrate with live SIEM logs (Splunk/Wazuh)

Replace Mock GenAI with real OpenAI API for dynamic analysis

Add an architecture diagram for visual clarity


