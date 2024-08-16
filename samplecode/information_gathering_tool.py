import subprocess
import socket
import requests
import whois
import json

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        print("\nWHOIS Lookup Result:")
        print(json.dumps(domain_info, indent=4))
    except Exception as e:
        print(f"WHOIS Lookup failed: {e}")

def nslookup(domain):
    try:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        print("\nNSLOOKUP Result:")
        print(result.stdout)
    except Exception as e:
        print(f"NSLOOKUP failed: {e}")

def get_ip_info(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        print("\nIP Address Information:")
        print(f"Hostname: {hostname[0]}")
        print(f"Aliases: {hostname[1]}")
        print(f"IP Addresses: {hostname[2]}")
    except Exception as e:
        print(f"IP Information retrieval failed: {e}")

def http_headers(url):
    try:
        response = requests.get(url)
        print("\nHTTP Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"HTTP Header retrieval failed: {e}")

def main():
    print("Information Gathering Tool")
    print("--------------------------")
    target = input("Enter the IP address, domain, or website URL: ")

    if target.startswith('http://') or target.startswith('https://'):
        http_headers(target)
        domain = target.split("//")[1].split('/')[0]
    else:
        domain = target
    
    if domain:
        whois_lookup(domain)
        nslookup(domain)
    
    if target.replace('.', '').isdigit():
        get_ip_info(target)

if __name__ == "__main__":
    main()
