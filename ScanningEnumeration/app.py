from flask import Flask, render_template
import subprocess
import nmap
import socket
import threading

app = Flask(__name__)

# Function to get the connected IP address
def get_connected_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"[ERROR] Unable to get connected IP address: {e}"

# Network Scanning with nmap
def network_scanning(target):
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=target, arguments='-sn')
        result = f"[SUCCESS] Network Scanning Completed\nHosts found: {nm.all_hosts()}"
        print(result)
        return result if result.strip() else "[ERROR] No data found during Network Scanning"
    except Exception as e:
        return f"[ERROR] Network Scanning failed: {e}"

# Port Scanning with nmap
def port_scanning(target):
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=target, arguments='-p-')
        result = f"[SUCCESS] Port Scanning Completed\n{nm.csv()}"
        print(result)
        return result if result.strip() else "[ERROR] No data found during Port Scanning"
    except Exception as e:
        return f"[ERROR] Port Scanning failed: {e}"

# DNS Enumeration with nslookup
def dns_enumeration(domain):
    try:
        result = subprocess.run(['nslookup', domain], capture_output=True, text=True)
        output = f"[SUCCESS] DNS Enumeration Completed\n{result.stdout}"
        print(output)
        return output if output.strip() else "[ERROR] No data found during DNS Enumeration"
    except Exception as e:
        return f"[ERROR] DNS Enumeration failed: {e}"

# SMB Enumeration
def smb_enumeration(target):
    try:
        result = subprocess.run(['nmap', '--script', 'smb-enum-shares', target], capture_output=True, text=True)
        output = f"[SUCCESS] SMB Enumeration Completed\n{result.stdout}"
        print(output)
        return output if output.strip() else "[ERROR] No data found during SMB Enumeration"
    except Exception as e:
        return f"[ERROR] SMB Enumeration failed: {e}"

# Commented out SNMP Enumeration
# def snmp_enumeration(target):
#     try:
#         result = subprocess.run(['snmpwalk', '-v2c', '-c', 'public', target], capture_output=True, text=True)
#         output = f"[SUCCESS] SNMP Enumeration Completed\n{result.stdout}"
#         print(output)
#         return output if output.strip() else "[ERROR] No data found during SNMP Enumeration"
#     except Exception as e:
#         return f"[ERROR] SNMP Enumeration failed: {e}"

# Commented out User Enumeration with hydra
# def user_enumeration(target, service, user_list, password_list):
#     try:
#         command = [
#             'hydra', 
#             '-L', user_list, 
#             '-P', password_list, 
#             target, 
#             service
#         ]
#         result = subprocess.run(command, capture_output=True, text=True)
#         output = f"[SUCCESS] User Enumeration Completed\n{result.stdout}"
#         print(output)
#         return output if output.strip() else "[ERROR] No data found during User Enumeration"
#     except Exception as e:
#         return f"[ERROR] User enumeration failed: {e}"

# Commented out Web Application Enumeration with DirBuster
# def web_enumeration(target):
#     try:
#         result = subprocess.run(['dirb', target], capture_output=True, text=True)
#         output = f"[SUCCESS] Web Application Enumeration Completed\n{result.stdout}"
#         print(output)
#         return output if output.strip() else "[ERROR] No data found during Web Application Enumeration"
#     except Exception as e:
#         return f"[ERROR] Web application enumeration failed: {e}"

# Asynchronous scan function
def async_scan(target, domain, results):
    results['network'] = network_scanning(target)
    results['port'] = port_scanning(target)
    results['dns'] = dns_enumeration(domain)
    results['smb'] = smb_enumeration(target)
    # Commented out the below sections
    # results['snmp'] = snmp_enumeration(target)
    # results['user'] = user_enumeration(target, 'ssh', 'users.txt', 'passwords.txt')
    # results['web'] = web_enumeration(f'http://{domain}')

@app.route("/")
def index():
    target = get_connected_ip()
    domain = "example.com"  # Replace with the actual domain if needed
    results = {
        'ip': target,
        'network': '',
        'port': '',
        'dns': '',
        'smb': '',
        # Commented out fields
        # 'snmp': '',
        # 'user': '',
        # 'web': '',
        'error': ''
    }

    if target:
        try:
            # Perform scans in a separate thread
            scan_thread = threading.Thread(target=async_scan, args=(target, domain, results))
            scan_thread.start()
            scan_thread.join()  # Wait for the scans to complete
        except Exception as e:
            results['error'] = f"[ERROR] Scanning failed: {e}"
    else:
        results['error'] = "[ERROR] Could not determine the connected IP address."

    return render_template("index.html", result=results)

if __name__ == "__main__":
    app.run(port=5002)
