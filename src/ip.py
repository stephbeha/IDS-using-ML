from scapy.all import sniff

def detect_ping(packet):
    if packet.haslayer(ICMP):  # Check if the packet has ICMP layer (pings)
        if packet[ICMP].type == 8:  # Check if the ICMP type is 8 (Echo request)
            print(f"Potential ping detected! Source: {packet[IP].src}")

def main():
    print("Sniffing network traffic for potential pings...")
    sniff(prn=detect_ping)  # Sniff packets and call detect_ping for each

if __name__ == "__main__":
    main()
