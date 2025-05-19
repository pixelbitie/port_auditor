# port_auditor.py - finds all unauthorised ports

import psutil

def load_allowed_ports():
    # Loads allowed ports from 'allowed_ports.txt'.
    try:
        with open('allowed_ports.txt', 'r') as f:
            content = f.read()
            return set(map(int, content.strip().split()))
    except FileNotFoundError:
        print(f"Error: 'allowed_ports.txt' not found.")
        return set()
    except ValueError:
        print("Error: Ensure all ports in the file are valid integers.")
        return set()

def get_listening_ports():
    # Returns a dict of open TCP ports mapped to process names
    port_map = {}
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == psutil.CONN_LISTEN:
            lport = conn.laddr.port
            pid = conn.pid
            if pid:
                try:
                    proc = psutil.Process(pid)
                    port_map[lport] = proc.name()
                except psutil.NoSuchProcess:
                    port_map[lport] = "Unknown"
    return port_map

def audit_ports(allowed_ports):
    print("Scanning for open ports...\n")
    found_ports = get_listening_ports()

    if not found_ports:
        print("No open listening ports found.")
        return

    for port, proc in found_ports.items():
        if port not in allowed_ports:
            print(f"Unauthorized port open: {port} (Process: {proc})")
        else:
            print(f"Allowed port: {port} (Process: {proc})")

if __name__ == "__main__":
    print("NOTE: Ensure that this script is being run with root privileges, otherwise it will not work.")
    allowed = load_allowed_ports()
    if allowed:
        audit_ports(allowed)
