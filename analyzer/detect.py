from collections import defaultdict

connection_attempts = defaultdict(int)

def detect_bruteforce(packet):
    if packet.haslayer(TCP):
        src = packet[IP].src
        if packet[TCP].flags == "S":  # SYN packets indicate connection attempts
            connection_attempts[src] += 1
            if connection_attempts[src] > 10:  # Example brute-force threshold
                print(f"[ALERT] Possible brute-force activity from {src}")
