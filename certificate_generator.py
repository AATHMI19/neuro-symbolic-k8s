from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os


def generate_certificate(result):

    os.makedirs("certificates", exist_ok=True)

    app_name = result['after']['name']
    filename = f"certificates/cert_{app_name}.pdf"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c = canvas.Canvas(filename, pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, 750, "KUBERNETES SECURITY CERTIFICATE")

    # Content
    c.setFont("Helvetica", 12)

    c.drawString(100, 700, f"Application Name : {app_name}")
    c.drawString(100, 680, f"Status           : {'SECURE' if result['verified'] else 'UNSAFE'}")
    c.drawString(100, 660, f"Violations Found : {result['violation']}")
    c.drawString(100, 640, f"Repairs Applied  : {result['repairs']}")
    c.drawString(100, 620, f"Certificate Hash : {result['certificate']}")
    c.drawString(100, 600, f"Generated At     : {now}")

    c.drawString(100, 560, "Certified by Neuro-Symbolic Engine")

    c.save()

    print(f"\n📄 Certificate saved: {filename}")

    return filename
