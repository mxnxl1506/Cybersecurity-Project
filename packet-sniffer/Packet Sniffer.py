#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

def packet_sniffer(interface):
    try:
        print(f"[*] Sniffing packets on interface: {interface}")
        subprocess.call(["sudo", "tcpdump", "-i", interface])

    except KeyboardInterrupt:
        print("\n[-] Packet sniffing stopped by user.")
    except Exception as e:
        print(f"[-] An error occurred during packet sniffing: {e}")

if __name__ == "__main__":
    network_interface = "eth0"  # Replace with your network interface
    packet_sniffer(network_interface)

