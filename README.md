# 🌀 VBS.py — A Funware Code Obfuscation Demo

Welcome to `FUnware` — a short, mysterious, and slightly chaotic piece of Python code that demonstrates basic **code obfuscation** using symmetric encryption and `cryptography`. Is it malware? No. Is it funware? Absolutely.

> This project is for educational and entertainment purposes only. No system was harmed in the making of this obfuscation.

---

## 💡 What It Does

This script uses [Fernet](https://cryptography.io/en/latest/fernet/) encryption to hide a command or script (which could be anything from a harmless message to... well, that's for you to decide). Upon execution, the encrypted payload is decrypted and then executed with Python’s `os.system()`.

In other words:
1. It **decrypts** an encrypted string using a predefined key.
2. It **executes** the decrypted string as a system command.
3. It looks simple. It **isn't**.

---

## 📁 Files

- `vbs.py` – The main script that does the decryption and execution.
- `this.vbs` – The VBS script with the actual payload.

---

## 🔐 How It Works

``` python
from cryptography. fernet import Fernet
from os import system

b = b'...'  # The encryption key
e = b'...'  # The encrypted payload

fer = Fernet(b)
d = fer.decrypt(e).decode()

system(d)
```

The payload in `e` is encrypted using the key `b`. To customize it for your own use:

## ⚠️ Disclaimer

This project is a **demo of obfuscation**, not malware. Do not use this code for any harmful or unethical purposes. Always respect privacy, system integrity, and the law.

---

## 🎉 Why?

Because sometimes, encrypting your `echo Hello World!` just feels cool.

