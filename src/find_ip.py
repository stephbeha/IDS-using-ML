import socket

def get_machine_ip():
    try:
        # Connect to an external server (Google's DNS server) to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return f"Error: {e}"

# Get and print the machine's IP address
ip_address = get_machine_ip()
print(f"Your machine's IP address is: {ip_address}")
