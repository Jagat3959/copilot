# copilot_test.py

## Overview

`copilot_test.py` is a Python script that retrieves and displays the system's uptime information. It works across different operating systems:

- **Linux/MacOS (Darwin):** Uses the `uptime` command to show how long the system has been running.
- **Windows:** Uses the `net stats srv` command and parses its output to display the system uptime since last boot.
- Prints errors if the uptime cannot be fetched or if the OS is unsupported.

## How It Works

The script detects your operating system using Python's `platform` module, then runs the appropriate system command:
- On Linux/MacOS: Prints the result of `uptime`.
- On Windows: Prints the line from `net stats srv` containing "Statistics since".
- If the OS is not supported, it prints a message indicating so.

## How to Run

1. **Requirements:**  
   - Python 3.x installed on your system.

2. **Usage:**  
   Open a terminal or command prompt and navigate to the directory containing `copilot_test.py`, then run:

   ```
   python copilot_test.py
   ```

   The script will print your system's uptime information to the console.

## Example Output

**Linux/MacOS:**
```
System uptime:  10:01  up 2 days,  3:42, 3 users, load averages: 0.52 0.48 0.46
```

**Windows:**
```
System uptime (since): Statistics since 7/13/2025 8:00:00 AM
```

**Unsupported OS:**
```
Unsupported OS: <your_os>
```

## Notes

- Administrative privileges may be required on some systems to run the uptime commands.
- Errors will be printed if the required command is not available or fails to execute.
