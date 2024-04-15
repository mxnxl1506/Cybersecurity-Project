# Spyware Script

This Python script demonstrates various techniques to collect system information and monitor user activity, simulating functionalities often associated with spyware. **Please note that this script is for educational purposes only and should not be used for malicious intent or unauthorized monitoring of individuals.**

## Functionalities

The `spyware.py` script includes the following functionalities:

1. **Keystroke Logging**
   - Records keystrokes in real-time using the `pynput` library and stores them in a text file (`logs.txt`).

2. **System Information Retrieval**
   - Retrieves computer information such as IP address, processor details, system type, and host name.
   - Saves the retrieved information in an Excel file (`keystrokes.xlsx`) using `pandas`.

3. **Clipboard Data Capture**
   - Captures clipboard contents (text) and logs them with timestamp information in a text file (`clipboard.txt`).

4. **Google Chrome History Retrieval**
   - Accesses the Google Chrome browsing history database to retrieve URLs, titles, and timestamps of visited websites.
   - Stores the browsing history in an Excel file (`search_history.xlsx`) using SQLite and `pandas`.

5. **Screenshot Capture**
   - Takes a screenshot of the computer screen and saves it as a PNG image file (`screenshot.png`) using `PIL` (Pillow) library.

## Usage

1. **Installation**
   - Install the required Python libraries using pip:
     ```bash
     pip install pynput pandas pillow
     ```

2. **Running the Script**
   - Execute the `spyware.py` script:
     ```bash
     python spyware.py
     ```
   - The script will start monitoring and logging keystrokes, capturing system information, clipboard contents, browsing history, and taking screenshots.

3. **Stopping the Script**
   - To stop the script and terminate monitoring, press `Esc` key.

## Disclaimer

**Warning**: This script is intended for educational purposes only. **Do not use this script for any unauthorized or malicious activities.** Monitoring or logging user activities without explicit consent is illegal and unethical. Always respect privacy and adhere to applicable laws and regulations.

The author of this script is not responsible for any misuse or damages caused by unauthorized use of this script.

---

**Note**: Modify and use the script responsibly in controlled environments for learning and experimentation purposes only. Avoid using this script in any way that violates privacy or legal rights of individuals.
