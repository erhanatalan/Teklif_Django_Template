# server.py
import subprocess

def run_server():
    subprocess.run(["python", "manage.py", "runserver"])