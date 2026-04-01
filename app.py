from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

CERT_FOLDER = "certificates"


# 🔹 UI Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Certificate Dashboard</title>
</head>
<body>
    <h2>✅ Certificate Dashboard</h2>
    <hr>

    {% if files %}
        <ul>
        {% for file in files %}
            <li>
                📄 {{ file }}
                <a href="/view/{{ file }}" target="_blank">[View]</a>
                <a href="/download/{{ file }}">[Download]</a>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No certificates found</p>
    {% endif %}
</body>
</html>
"""


# 🔹 Home → Dashboard
@app.route('/')
def home():
    files = [f for f in os.listdir(CERT_FOLDER) if f.endswith(".pdf")]
    files.sort(reverse=True)
    return render_template_string(HTML_TEMPLATE, files=files)


# 🔹 View PDF
@app.route('/view/<filename>')
def view_file(filename):
    file_path = os.path.join(CERT_FOLDER, filename)
    return send_file(file_path)


# 🔹 Download PDF
@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(CERT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
