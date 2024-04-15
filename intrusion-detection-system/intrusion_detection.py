import scapy.all as scapy

def detect_intrusions():
    print("[*] Starting Intrusion Detection System...")
    sniffed_packets = scapy.sniff(filter="tcp and port 80", count=10)
    print("[+] Packets sniffed:")
    for packet in sniffed_packets:
        print(packet.summary())

if __name__ == "__main__":
    detect_intrusions()
