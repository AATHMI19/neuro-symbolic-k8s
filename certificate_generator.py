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

    y = 750  # vertical position

    # =========================
    # 🏷️ TITLE
    # =========================
    c.setFont("Helvetica-Bold", 16)
    c.drawString(120, y, "KUBERNETES SECURITY CERTIFICATE")
    y -= 40

    c.setFont("Helvetica", 12)

    # =========================
    # 📌 BASIC INFO
    # =========================
    c.drawString(50, y, f"Application Name : {app_name}")
    y -= 20
    c.drawString(50, y, f"Status           : {'SECURE' if result['verified'] else 'UNSAFE'}")
    y -= 20
    c.drawString(50, y, f"Violations Found : {result['violation']}")
    y -= 20
    c.drawString(50, y, f"Repairs Applied  : {result['repairs']}")
    y -= 20
    c.drawString(50, y, f"Certificate Hash : {result['certificate']}")
    y -= 20
    c.drawString(50, y, f"Generated At     : {now}")
    y -= 30

    # =========================
    # 🔄 AUTO-REPAIR SECTION
    # =========================
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "AUTO-REPAIRED CONFIGURATION")
    y -= 20

    c.setFont("Helvetica", 11)

    before = result['before']
    after = result['after']

    c.drawString(50, y, f"Before: runAsNonRoot = {before.get('runAsNonRoot')}")
    y -= 20
    c.drawString(50, y, f"After : runAsNonRoot = {after.get('runAsNonRoot')}")
    y -= 30

    # =========================
    # 📦 SERVICES CONFIGURATION
    # =========================
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "SERVICES CONFIGURATION")
    y -= 20

    c.setFont("Helvetica", 10)

    services = after.get("services", [])

    for svc in services:
        line = f"Service: {svc['name']} | Image: {svc['image']} | Port: {svc['port']} | Replicas: {svc['replicas']} | Exposure: {svc['exposure']}"
        c.drawString(50, y, line)
        y -= 15

        # Prevent overflow
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 750

    y -= 20

    # =========================
    # ✅ FINAL SECURE CONFIG
    # =========================
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "FINAL SECURE CONFIGURATION")
    y -= 20

    c.setFont("Helvetica", 10)

    final_config = result['after']

    for key, value in final_config.items():
        if key != "services":
            c.drawString(50, y, f"{key} : {value}")
            y -= 15

            # Prevent overflow
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = 750

    y -= 30

    # =========================
    # 📌 FOOTER
    # =========================
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Certified by Neuro-Symbolic Engine")

    # Save PDF
    c.save()

    print(f"\n📄 Certificate saved: {filename}")

    return filename
