from modules import port_scanner, ssh_brute_forcer

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    choice = input("Choose a module (1/2): ")

    if choice == '1':
        target = input("Enter target IP or domain: ")
        port_scanner.scan_ports(target)
    elif choice == '2':
        target = input("Enter target IP: ")
        username = input("Enter SSH username: ")
        wordlist_path = input("Enter path to password wordlist: ")
        ssh_brute_forcer.brute_force(target, username, wordlist_path)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
