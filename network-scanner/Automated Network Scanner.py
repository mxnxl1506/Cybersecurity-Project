#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import scapy.all as scapy

def scan_network(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)
        return clients_list

    except KeyboardInterrupt:
        print("\n[-] User interrupted scanning.")
        return []
    except Exception as e:
        print(f"[-] An error occurred during scanning: {e}")
        return []

def display_result(results):
    print("Discovered Devices:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results:
        print(f"{client['ip']}\t\t{client['mac']}")

def main():
    target_ip = "192.168.1.0/24"  # Replace with your target IP range
    print(f"[*] Scanning target: {target_ip}")
    scan_result = scan_network(target_ip)

    if scan_result:
        display_result(scan_result)
    else:
        print("[-] No devices found or scanning was interrupted.")

if __name__ == "__main__":
    main()

