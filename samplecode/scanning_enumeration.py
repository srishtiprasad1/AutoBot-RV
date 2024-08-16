import subprocess
import nmap
import socket
import os

# Function to get the connected IP address
def get_connected_ip():
    try:
        # Create a socket connection to an external server (Google's DNS) to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"[ERROR] Unable to get connected IP address: {e}")
        return None

# Network Scanning with nmap
def network_scanning(target):
    nm = nmap.PortScanner()
    print(f"\n[INFO] Starting Network Scanning on target: {target}")
    try:
        nm.scan(hosts=target, arguments='-sn')  # -sn is for host discovery
        print(f"[SUCCESS] Network Scanning Completed")
        print(nm.all_hosts())
    except Exception as e:
        print(f"[ERROR] Network Scanning failed: {e}")

# Port Scanning with nmap
def port_scanning(target):
    nm = nmap.PortScanner()
    print(f"\n[INFO] Starting Port Scanning on target: {target}")
    try:
        nm.scan(hosts=target, arguments='-p-')  # Scanning top 1000 ports with verbosity
        print(f"[SUCCESS] Port Scanning Completed")
        print(nm.csv())
    except Exception as e:
        print(f"[ERROR] Port Scanning failed or timed out: {e}")

# DNS Enumeration with nslookup
def dns_enumeration(domain):
    print(f"\n[INFO] Starting DNS Enumeration on domain: {domain}")
    try:
        result = subprocess.run(['nslookup', domain], capture_output=True, text=True)
        print(f"[SUCCESS] DNS Enumeration Completed")
        print(result.stdout)
    except Exception as e:
        print(f"[ERROR] DNS Enumeration failed: {e}")

# SMB Enumeration
def smb_enumeration(target):
    print(f"\n[INFO] Starting SMB Enumeration on target: {target}")
    try:
        result = subprocess.run(['nmap', '--script', 'smb-enum-shares', target], capture_output=True, text=True)
        print(f"[SUCCESS] SMB Enumeration Completed")
        print(result.stdout)
    except Exception as e:
        print(f"[ERROR] SMB Enumeration failed: {e}")

# SNMP Enumeration
def snmp_enumeration(target):
    print(f"\n[INFO] Starting SNMP Enumeration on target: {target}")
    try:
        result = subprocess.run(['snmpwalk', '-v2c', '-c', 'public', target], capture_output=True, text=True)
        print(f"[SUCCESS] SNMP Enumeration Completed")
        print(result.stdout)
    except Exception as e:
        print(f"[ERROR] SNMP Enumeration failed: {e}")

# User Enumeration with hydra
def user_enumeration(target, service, user_list, password_list):
    print(f"\n[INFO] Starting User Enumeration on target: {target}")
    try:
        command = [
            'hydra', 
            '-L', user_list, 
            '-P', password_list, 
            target, 
            service
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        print(f"[SUCCESS] User Enumeration Completed")
        print(result.stdout)
    except Exception as e:
        print(f"[ERROR] User enumeration failed: {e}")

# Web Application Enumeration with DirBuster
def web_enumeration(target):
    print(f"\n[INFO] Starting Web Application Enumeration on target: {target}")
    try:
        result = subprocess.run(['dirb', target], capture_output=True, text=True)
        print(f"[SUCCESS] Web Application Enumeration Completed")
        print(result.stdout)
    except Exception as e:
        print(f"[ERROR] Web application enumeration failed: {e}")

# Main Function
def main():
    target = get_connected_ip()
    domain = 'example.com'  # Replace with your domain

    if target:
        print(f"[INFO] Connected IP address: {target}")
        network_scanning(target)
        port_scanning(target)
    
        dns_enumeration(domain)
        smb_enumeration(target)
        snmp_enumeration(target)
        user_enumeration(target, 'ssh', 'users.txt', 'passwords.txt')
        web_enumeration(f'http://{domain}')
    else:
        print("[ERROR] Could not determine the connected IP address.")

if __name__ == "__main__":
    main()
