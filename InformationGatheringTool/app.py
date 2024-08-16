from flask import Flask, render_template, request, send_from_directory
import subprocess
import socket
import requests
import whois
import json
from io import StringIO
import sys
import os

app = Flask(__name__)

# Define paths to static directories
app.config['MAIN_PROJECT'] = os.path.abspath('main-project')

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return json.dumps(domain_info, indent=4)
    except Exception as e:
        return f"WHOIS Lookup failed: {e}"

def nslookup(domain):
    try:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"NSLOOKUP failed: {e}"

def get_ip_info(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        return f"Hostname: {hostname[0]}\nAliases: {hostname[1]}\nIP Addresses: {hostname[2]}"
    except Exception as e:
        return f"IP Information retrieval failed: {e}"

def http_headers(url):
    try:
        response = requests.get(url)
        headers = "\n".join([f"{header}: {value}" for header, value in response.headers.items()])
        return headers
    except Exception as e:
        return f"HTTP Header retrieval failed: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        target = request.form['url']

        # Capture the print statements
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        if target.startswith('http://') or target.startswith('https://'):
            print("\nHTTP Headers:")
            print(http_headers(target))
            domain = target.split("//")[1].split('/')[0]
        else:
            domain = target

        if domain:
            print("\nWHOIS Lookup Result:")
            print(whois_lookup(domain))
            print("\nNSLOOKUP Result:")
            print(nslookup(domain))

        if target.replace('.', '').isdigit():
            print("\nIP Address Information:")
            print(get_ip_info(target))

        sys.stdout = old_stdout
        output = mystdout.getvalue()

    return render_template('index.html', output=output)

@app.route('/main-project/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['MAIN_PROJECT'], filename)

@app.route('/information-gathering', methods=['GET', 'POST'])
def information_gathering():
    output = ""
    if request.method == 'POST':
        target = request.form['url']

        # Capture the print statements
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        if target.startswith('http://') or target.startswith('https://'):
            print("\nHTTP Headers:")
            print(http_headers(target))
            domain = target.split("//")[1].split('/')[0]
        else:
            domain = target

        if domain:
            print("\nWHOIS Lookup Result:")
            print(whois_lookup(domain))
            print("\nNSLOOKUP Result:")
            print(nslookup(domain))

        if target.replace('.', '').isdigit():
            print("\nIP Address Information:")
            print(get_ip_info(target))

        sys.stdout = old_stdout
        output = mystdout.getvalue()

    return render_template('index.html', output=output)


if __name__ == "__main__":
    app.run(port=5001)
