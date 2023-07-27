import subprocess
import signal
import time

def stop_server():
    try:
        # Find the process running the Django server
        process = subprocess.Popen(["python", "manage.py", "runserver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process_info = process.communicate()[0].decode("utf-8")

        # Extract the process ID from the process_info
        process_id = None
        for line in process_info.splitlines():
            if "Starting development server" in line:
                process_id = int(line.split()[0])
                break

        # Terminate the Django server process gracefully
        if process_id:
            print(f"Stopping the Django server (PID: {process_id})")
            os.kill(process_id, signal.SIGTERM)
        else:
            print("Django server process not found. Server may not be running.")

    except Exception as e:
        print("Error stopping the Django server:", str(e))

def run_server():
    # Stop the server if it is running
    stop_server()

    # Wait a bit to allow the server to shut down properly
    time.sleep(2)

    # Start the server
    print("Starting the Django server")
    subprocess.run(["python", "manage.py", "runserver"])