import subprocess
import time
import signal
import sys
import os

def run_command(duration, command):
    # Start the command
    process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Wait for the specified duration
    time.sleep(duration)

    # Send the SIGINT signal to the process group
    os.killpg(os.getpgid(process.pid), signal.SIGINT)

    # Print the output of the command
    output, _ = process.communicate()
    print(output.decode())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 run_for_duration.py <duration(seconds)> <command>")
        sys.exit(1)

    duration = int(sys.argv[1])
    command = sys.argv[2]

    run_command(duration, command)
