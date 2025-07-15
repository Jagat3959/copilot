import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        # Use the 'uptime' command
        try:
            uptime = subprocess.check_output(["uptime"]).decode().strip()
            print("System uptime:", uptime)
        except Exception as e:
            print("Error fetching uptime:", e)
    elif system == "Windows":
        # Use 'net stats srv' and parse output
        try:
            output = subprocess.check_output("net stats srv", shell=True).decode()
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System uptime (since):", line)
                    break
            else:
                print("Could not find uptime info.")
        except Exception as e:
            print("Error fetching uptime:", e)
    else:
        print("Unsupported OS:", system)

if __name__ == "__main__":
    get_uptime()
