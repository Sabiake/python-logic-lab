import sys
import socket
from datetime import datetime
import threading


# Function to scan a port


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(
            (target, port)
        )  # error indicator - if the connection is successful, it returns 0; otherwise, it returns an error code
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


# Main function to scan ports on a given IP address (argument validation and target definition)


def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <IP_ADDRESS>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Scanning target: {target}")

    # Record the start time of the scan

    start_time = datetime.now()

    # Create threads for scanning ports 1 to 65535

    threads = []
    for port in range(1, 65536):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete

    for thread in threads:
        thread.join()

    # Record the end time of the scan and calculate the duration

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Scanning completed in: {duration}")


if __name__ == "__main__":
    main()
