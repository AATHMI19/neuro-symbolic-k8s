from flask import Flask, send_file, redirect, url_for
import os

app = Flask(__name__)

CERT_FOLDER = "certificates"


def get_latest_certificate():
    files = [f for f in os.listdir(CERT_FOLDER) if f.endswith(".pdf")]
    if not files:
        return None

    files.sort(reverse=True)
    return files[0]


@app.route('/')
def home():
    # Redirect directly to latest certificate
    return redirect(url_for('view_certificate'))


@app.route('/cert')
def view_certificate():
    filename = get_latest_certificate()

    if not filename:
        return "No certificate found"

    file_path = os.path.join(CERT_FOLDER, filename)
    return send_file(file_path)


@app.route('/download')
def download_latest():
    filename = get_latest_certificate()

    if not filename:
        return {"error": "No certificate found"}, 404

    file_path = os.path.join(CERT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)


# (Keep your existing route also if needed)
@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(CERT_FOLDER, filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return {"error": "File not found"}, 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
