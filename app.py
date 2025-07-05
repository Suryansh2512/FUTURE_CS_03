from flask import Flask, request, render_template, send_file, redirect, url_for
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load encryption key
fernet = Fernet(open('key.key', 'rb').read())

# Landing page
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

# Upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        data = f.read()
        encrypted = fernet.encrypt(data)
        filename = f.filename + '.enc'
        with open(os.path.join(UPLOAD_FOLDER, filename), 'wb') as file:
            file.write(encrypted)
        return f"✅ Encrypted and saved as <b>{filename}</b><br><br><a href='/home'>Back to Home</a>"
    return render_template('upload.html')

# Download route
@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        filename = request.form['filename']
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(path) and filename.endswith('.enc'):
            decrypted_data = fernet.decrypt(open(path, 'rb').read())
            decrypted_filename = filename.replace('.enc', '')
            decrypted_path = os.path.join(UPLOAD_FOLDER, decrypted_filename)
            with open(decrypted_path, 'wb') as f:
                f.write(decrypted_data)
            return send_file(decrypted_path, as_attachment=True)
        return "❌ File not found or not encrypted!<br><br><a href='/home'>Back to Home</a>"
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
