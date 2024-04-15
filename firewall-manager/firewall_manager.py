import subprocess

def enable_firewall():
    """Enable the firewall using 'ufw enable' command."""
    try:
        subprocess.run(["sudo", "ufw", "enable"], check=True)
        print("Firewall enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling firewall: {e}")

def disable_firewall():
    """Disable the firewall using 'ufw disable' command."""
    try:
        subprocess.run(["sudo", "ufw", "disable"], check=True)
        print("Firewall disabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling firewall: {e}")

def add_firewall_rule(port, protocol='tcp'):
    """Add a firewall rule to allow incoming traffic on a specific port and protocol."""
    try:
        subprocess.run(["sudo", "ufw", "allow", f"{port}/{protocol}"], check=True)
        print(f"Firewall rule added successfully for {protocol.upper()} port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding firewall rule: {e}")

def remove_firewall_rule(port, protocol='tcp'):
    """Remove a firewall rule to deny incoming traffic on a specific port and protocol."""
    try:
        subprocess.run(["sudo", "ufw", "delete", f"allow", f"{port}/{protocol}"], check=True)
        print(f"Firewall rule removed successfully for {protocol.upper()} port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing firewall rule: {e}")

# Example usage:
if __name__ == "__main__":
    # Enable firewall
    enable_firewall()

    # Add firewall rule to allow incoming traffic on port 80 (HTTP)
    add_firewall_rule(80, 'tcp')

    # Disable firewall
    disable_firewall()
