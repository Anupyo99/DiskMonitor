# 🖥️ Python Disk Space Monitor

This is a simple Python project that monitors disk space on a specified drive (e.g., C:) and sends an email alert if free space falls below a set threshold. It also logs all checks in a `.log` file.

## 🔧 Features

- Monitors disk space every time it's run
- Sends email alert if space is less than 10%
- Logs results to `disk_monitor.log`

## 📂 Files

- `disk_monitor.py` – Main monitoring script
- `disk_monitor.log` – Log file (auto-created)
- `README.md` – Project overview

## ⚙️ Setup

1. Install Python and `psutil`:

2. Edit the script with your email credentials and desired drive:
```python
DRIVE = "C:\\"
EMAIL_FROM = "your-email@gmail.com"
EMAIL_TO = "it-team@example.com"
EMAIL_PASSWORD = "your-app-password"
python disk_monitor.py
