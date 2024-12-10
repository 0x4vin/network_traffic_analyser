import scapy.all as scapy
from scapy.layers.inet import TCP, UDP, IP
from scapy.layers.http import HTTP
import threading

# List to store captured packets
packets = []

# Function to capture packets
def packet_callback(packet):
    global packets
    if packet.haslayer(IP):  # Capture only IP packets
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        packet_type = None
        if packet.haslayer(TCP):
            packet_type = 'TCP'
        elif packet.haslayer(UDP):
            packet_type = 'UDP'
        elif packet.haslayer(HTTP):
            packet_type = 'HTTP'

        packet_length = len(packet)

        # Add packet data to the list
        packets.append({
            'src': ip_src,
            'dst': ip_dst,
            'type': packet_type,
            'length': packet_length
        })

# Function to start sniffing packets
def start_sniffer():
    scapy.sniff(iface="wlan0", prn=packet_callback, store=0)

# Function to get packets (can be called by Flask route)
def get_packets():
    return packets

# Start the sniffer in a separate thread
def start_capture():
    thread = threading.Thread(target=start_sniffer)
    thread.daemon = True
    thread.start()
