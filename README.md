# FUTURE_CS_03
Secure File Sharing System
# 🔐 Secure File Upload & Download Web App

A simple Python-Flask based web application that lets users **securely upload and download files using symmetric encryption (Fernet/AES)**. Built as part of **Cyber Security Task 3** for the **Future Interns Program**.

---

## 🚀 Features

- 🔐 **File Encryption** using Fernet (AES)
- 📤 **Upload Interface** – Encrypts and saves your file securely
- 📥 **Download Interface** – Decrypts the encrypted file and sends it back to you
- 🌐 **Web UI** with a clean landing page to choose between Upload/Download
- 🧠 Fully functional with auto-generated encryption key

---

## 📁 Folder Structure

FUTURE_CS_03/
│
├── app.py # Flask app
├── generate_key.py # Generates Fernet key
├── key.key # Auto-generated encryption key
├── uploads/ # Stores encrypted + decrypted files
├── templates/
│ ├── home.html
│ ├── upload.html
│ └── download.html
├── .gitignore
└── README.md # You're here!


---

## ⚙️ How It Works

1. Run `generate_key.py` once to create `key.key`
2. Launch the app:
   ```bash
   python3 app.py
3. Navigate to http://localhost:5000 (or Codespaces URL)
4. Upload a file → it gets encrypted & saved
5. Download with filename.enc → it decrypts and returns the original file

🛡️ Tech Stack
Language: Python
Framework: Flask
Encryption: Fernet (symmetric AES)
Runtime: GitHub Codespaces (or localhost)


🧠 Concepts Used
Cryptography with Fernet
File I/O & secure storage
Flask routing & templating
Data security in transit

📦 Requirements
Python 3.8+
Flask
cryptography

🙋‍♂️ Author
Suryansh Misra
Built for Future Interns - Cyber Security Track

🧠 Future Improvements
✅ Auto-list encrypted files on download page
🛡️ Add user authentication
🌍 Deploy to Render/Vercel

📄 License
MIT License
