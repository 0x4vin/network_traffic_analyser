# Network Traffic Analyzer

## **Project Overview**
The Network Traffic Analyzer is a Python-based tool designed to monitor, capture, and analyze network traffic in real-time. It provides a web-based interface to visualize captured data and includes functionality to detect potential brute-force or fuzzing activities on the network. This project is tailored for educational and experimental purposes in controlled environments.

## **Features**
1. **Real-Time Traffic Capture**:
   - Captures all network traffic on the specified interface (`wlan0`).
   - Analyzes incoming and outgoing packets in real-time.

2. **Web-Based Visualization**:
   - Displays captured traffic in a tabular format on a locally hosted web app.
   - Columns include:
     - Source IP
     - Destination IP
     - Packet Type (e.g., TCP, FTP, HTTP)
     - Packet Length

3. **Live Traffic Analysis**:
   - Tracks live incoming and outgoing packets to detect anomalies.

4. **Brute-Force Detection**:
   - Identifies suspicious activities such as brute-force attempts or fuzzing, based on packet patterns and thresholds.

---

## **Project Purpose**
The purpose of this project is to provide a lightweight, efficient, and user-friendly tool for:
- Monitoring network traffic in real-time.
- Identifying potential security threats, such as brute-force attacks.
- Offering network administrators insights into traffic patterns and anomalies.

---

## **Setup and Usage**
### **1. Requirements**
- Python 3.8 or later
- Administrator privileges for packet capturing
- Libraries listed in `requirements.txt`
