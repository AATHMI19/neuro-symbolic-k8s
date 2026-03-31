from flask import Flask, send_file
import os

app = Flask(__name__)

CERT_FOLDER = "certificates"

@app.route('/')
def home():
    return "Certificate Download Server Running"

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(CERT_FOLDER, filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return {"error": "File not found"}, 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)