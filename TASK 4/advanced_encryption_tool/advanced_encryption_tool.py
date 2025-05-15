
import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Function to derive AES-256 key from password
def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

# Encrypt file with AES-256
def encrypt_file(input_file, output_file, password):
    salt = os.urandom(16)
    key = derive_key(password.encode(), salt)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        data = f.read()

    # Padding (PKCS#7-like)
    pad_len = 16 - (len(data) % 16)
    data += bytes([pad_len]) * pad_len

    encrypted = encryptor.update(data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(salt + iv + encrypted)

# Decrypt file with AES-256
def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    key = derive_key(password.encode(), salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted = decryptor.update(encrypted_data) + decryptor.finalize()
    pad_len = decrypted[-1]
    decrypted = decrypted[:-pad_len]

    with open(output_file, 'wb') as f:
        f.write(decrypted)

# GUI Functions
def browse_file():
    file_path.set(filedialog.askopenfilename())

def encrypt():
    try:
        in_file = file_path.get()
        out_file = in_file + ".enc"
        encrypt_file(in_file, out_file, password.get())
        messagebox.showinfo("Success", f"Encrypted:\n{out_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt():
    try:
        in_file = file_path.get()
        if in_file.endswith(".enc"):
            out_file = in_file.replace(".enc", ".dec")
        else:
            out_file = in_file + ".dec"
        decrypt_file(in_file, out_file, password.get())
        messagebox.showinfo("Success", f"Decrypted:\n{out_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
app = tk.Tk()
app.title("Advanced Encryption Tool")
app.geometry("400x250")
app.resizable(False, False)

file_path = tk.StringVar()
password = tk.StringVar()

tk.Label(app, text="File Path:").pack(pady=5)
tk.Entry(app, textvariable=file_path, width=45).pack()
tk.Button(app, text="Browse", command=browse_file).pack(pady=5)

tk.Label(app, text="Password:").pack(pady=5)
tk.Entry(app, textvariable=password, show="*", width=45).pack()

tk.Button(app, text="Encrypt File", command=encrypt, bg="lightblue").pack(pady=10)
tk.Button(app, text="Decrypt File", command=decrypt, bg="lightgreen").pack()

app.mainloop()
