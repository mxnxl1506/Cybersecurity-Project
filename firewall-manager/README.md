# Firewall Management Tool

This project implements a basic firewall management tool in Python to interact with the 'ufw' (Uncomplicated Firewall) utility on Linux systems.

## Features
- **Enable/Disable Firewall**: Start or stop the firewall to control incoming and outgoing network traffic.
- **Add/Remove Firewall Rules**: Allow or deny specific ports and protocols for incoming traffic.

## Usage
1. Ensure 'ufw' (Uncomplicated Firewall) is installed on your Linux system (`sudo apt install ufw` on Debian/Ubuntu).
2. Run the script with appropriate privileges (`sudo`) to manage firewall settings.

### Available Functions
- `enable_firewall()`: Enable the firewall (`sudo ufw enable`).
- `disable_firewall()`: Disable the firewall (`sudo ufw disable`).
- `add_firewall_rule(port, protocol='tcp')`: Add a firewall rule to allow incoming traffic on a specific port and protocol.
- `remove_firewall_rule(port, protocol='tcp')`: Remove a firewall rule to deny incoming traffic on a specific port and protocol.

**Note**: Use responsibly and with proper authorization when modifying firewall settings.

For more details, refer to the [firewall_manager.py](./firewall_manager.py) script.
