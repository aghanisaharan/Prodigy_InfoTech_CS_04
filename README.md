# Simple Keylogger

This repository contains my Python program for Task 04 of the Cyber Security Internship at **Prodigy InfoTech**.

The objective of this project is to create a basic keylogger program that records and logs keystrokes. The focus is on accurately capturing the keys pressed by the user and saving them to a designated log file. 

**⚠️ Disclaimer:** This tool was built strictly for educational purposes as part of a cybersecurity training program. Ethical considerations and permissions are crucial for projects involving keyloggers. This software should only be used on systems where you have explicit authorization.

## Features
* **Keystroke Logging:** Captures alphanumeric keys and special characters (e.g., Space, Enter, Tab) for readability.
* **Session Tracking:** Automatically appends a timestamp at the beginning of each logging session to organize the data.
* **File Output:** Securely writes the logged keystrokes to a local `keylog.txt` file.
* **Graceful Exit:** Allows the user to stop the listener seamlessly by pressing the `Esc` key.

## Requirements
* Python 3.x
* `pynput` library (`pip install pynput`)
