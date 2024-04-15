# Keylogger Script

This Python script demonstrates a basic keylogger functionality, logging keystrokes and capturing clipboard data, then sending it to a specified server via a TCP connection. **Please note that this script is for educational purposes only and should not be used for unauthorized monitoring of individuals.**

## Functionalities

The `keylogger.py` script includes the following functionalities:

1. **Keystroke Logging**
   - Listens to and logs keystrokes using the `pynput` library.
   - Sends captured keystrokes to a specified server via a TCP connection.

2. **Clipboard Data Capture**
   - Reads clipboard contents and sends them to the server along with keystroke data.

3. **TCP Data Transmission**
   - Establishes a TCP connection to a specified server address (`SERVER_ADDRESS`) to transmit captured data.
   - Sends keystroke and clipboard data to the server for remote monitoring.

## Usage

1. **Installation**
   - Ensure you have the required Python libraries (`pynput` and `pandas`) installed:
     ```bash
     pip install pynput pandas
     ```

2. **Running the Script**
   - Execute the `keylogger.py` script:
     ```bash
     python keylogger.py
     ```
   - The script will start logging keystrokes and clipboard data in the background.

3. **Monitoring the Server**
   - Replace `SERVER_ADDRESS` with your server's IP address and port in the script (`192.168.29.54:53`).
   - Run a server on the specified IP address and port to receive incoming keystroke and clipboard data.

## Disclaimer

**Warning**: This script is intended for educational purposes only. **Do not use this script for any unauthorized or malicious activities.** Monitoring or logging user activities without explicit consent is illegal and unethical. Always respect privacy and adhere to applicable laws and regulations.

The author of this script is not responsible for any misuse or damages caused by unauthorized use of this script.

---

**Note**: Modify and use the script responsibly in controlled environments for learning and experimentation purposes only. Avoid using this script in any way that violates privacy or legal rights of individuals.
