# AutoBot-RV
A versatile tool that automates the gathering of information on URLs, websites, and DNS. It enhances security by performing comprehensive scanning and network enumeration, facilitating detailed analysis and identification of potential vulnerabilities in system networks.
AutoBot-RV | Automated Reconnaissance Tool
Project Description:
AutoBot-RV is an automated reconnaissance tool designed to streamline the reconnaissance phase of ethical hacking. This tool enables users to perform comprehensive scanning and enumeration tasks for domains and IP addresses, making it an essential asset for security professionals. AutoBot-RV currently supports IP Information Gathering, Domain Information Gathering, Network Scanning, Port Scanning, DNS Enumeration, and SMB Enumeration. Future updates will include a Vulnerability Analysis feature to further enhance its capabilities.

Features:

IP Information: Retrieves detailed information about the given IP address.
Domain Information: Gathers essential details about the domain, including WHOIS records, DNS information, and more.
Network Scanning: Discovers devices connected to a network and identifies their IP addresses.
Port Scanning: Identifies open ports on a target system, along with the services running on them.
DNS Enumeration: Retrieves DNS records and subdomains associated with the target domain.
SMB Enumeration: Enumerates shared resources on a network using the SMB protocol.

Technological Stack:

Backend: Python, Flask
Frontend: HTML, CSS, JavaScript, Bootstrap
Tools Integrated: WHOIS, nslookup, Nmap, Dig, SMBClient
IDE: Visual Studio Code (VS Code)
Deployment: Localhost (Future plans for cloud deployment)

Installation:

Step 1. Clone the repository :  git clone [provide git repository link here]

Step 2: Navigate to the project directory : cd AutoBot-RV

Step 3: Run the application : python main.py

Step 4: You will get to local host addresses: 
        1: http://127.0.0.1:5001 is for InformationGatheringTool (main entry) 
        2: http://127.0.0.1:5002 is for scanning and enumeration

Step 5: http://127.0.0.1:5001 Access this by Clicking in Terminal or Copy and Paste in Browser

Step 6: Switch to Home from Navbar

Step 7: Your project is ready for use !!



Usage:

Select Option: Choose the reconnaissance task you want to perform.
Input: Enter the domain name or IP address to analyze.
View Results: The results are displayed in real-time on your window.

Future Enhancements:

Vulnerability Analysis: Automated vulnerability scanning and manual testing scripts for specific vulnerabilities.
Cloud Deployment: Hosting the tool on cloud platforms for broader accessibility.
Enhanced Reporting: Advanced visualization and reporting options for better analysis.


Contributors:

Team Name: BotBuddies
Developed During: IBM Internship Program
Team Members: Suryansh Singh and Srishti Prasad


License:
This project is licensed under the MIT License. See the LICENSE file for more details.

