# Imports
import nmap

# Functions
def get_ip():
    ip = input("Please specify the target's IP address: ")
    return ip


def get_port_range():
    port_range = input("Please specify the port range (origin-end): ")
    return port_range


#===================================================MAIN===============================================================#

def main():
    nmap_scanner = nmap.PortScanner()
    print("Version:", nmap_scanner.nmap_version())
    ip = get_ip()
    port_range = get_port_range()
    nmap_scanner.scan(ip, port_range, "-v")
    print('\n',nmap_scanner.scaninfo())
    print(nmap_scanner.csv())

main()