import socket

def scan_ports(target):
    print(f"Scanning ports on {target}...")
    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except socket.error:
            print(f"[-] Couldn't connect to {target}")
            break
