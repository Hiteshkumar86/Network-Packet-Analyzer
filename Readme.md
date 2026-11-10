🔐 Network Packet Analyzer

📌 Project Overview

The Network Packet Analyzer is a Python-based cybersecurity project developed as part of the CodSoft Cyber Security Internship.

This application captures network packets and analyzes their metadata to understand network communication and protocols.

It uses Python and Scapy to capture and display important packet information.

🎯 Objectives

- Capture IP packets from a network interface.
- Identify source and destination IP addresses.
- Detect network protocols such as TCP, UDP, and ICMP.
- Display packet size and port information.
- Save captured packet information into a CSV file.

✨ Features

- Live network packet capturing.
- Source IP and destination IP detection.
- TCP, UDP, and ICMP protocol identification.
- Packet size analysis.
- Source and destination port extraction.
- Automatic CSV logging.
- Real-time terminal output.

🛠️ Technologies Used

- Python 3
- Scapy 2.8.0
- Npcap
- CSV Module
- Visual Studio Code

📂 Project Structure

Task1_Network_Packet_Analyzer/
│
├── main.py
├── packet_log.csv
├── requirements.txt
└── README.md

⚙️ Installation and Setup

1. Install Python

Download and install Python from:
https://www.python.org/

2. Install Npcap

Download Npcap from:
https://npcap.com/

3. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

4. Open the Project Folder

cd Task1_Network_Packet_Analyzer

5. Install Dependencies

pip install -r requirements.txt

▶️ How to Run

Open the terminal in the project directory and execute:

python main.py

Run the terminal with appropriate permissions for packet capturing.

The application will start capturing IP packet metadata.

Press "CTRL + C" to stop packet capturing.

📊 Sample Output

NETWORK PACKET ANALYZER

Packet Number     : 1
Timestamp         : 2026-11-10 09:43:57
Source IP         : 192.168.1.5
Destination IP    : 142.250.183.14
Protocol          : TCP
Packet Size       : 1354 bytes
Source Port       : 55168
Destination Port  : 443

Total Packets Captured: 983
Network Analyzer Closed.

Note: Sample values are illustrative. Actual results depend on network traffic.

📁 Output File

The application automatically generates "packet_log.csv", containing:

- Packet Number
- Timestamp
- Source IP
- Destination IP
- Protocol
- Packet Size
- Source Port
- Destination Port

🔒 Security and Privacy

This project is intended for educational use on networks and devices where packet capture is authorized.

It focuses on packet metadata and does not intentionally collect application passwords or private message contents.

🎓 Internship Information

Organization: CodSoft
Internship: Cyber Security Internship
Project: Task 1 – Network Packet Analyzer
Language: Python

👨‍💻 Author

Developed as part of the CodSoft Cyber Security Internship.