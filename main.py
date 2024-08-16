import subprocess

def run_app(script_path):
    subprocess.Popen(['python', script_path])

if __name__ == '__main__':
    # Absolute paths to app.py files
    run_app('./InformationGatheringTool/app.py')
    run_app('./ScanningEnumeration/app.py')

# http://127.0.0.1:5001 is for InformationGatheringTool (main entry)
# http://127.0.0.1:5002 is for scanning and enumeration