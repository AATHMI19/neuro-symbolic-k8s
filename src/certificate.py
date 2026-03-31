from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import hashlib
import os

def generate_certificate(manifest_name, violations_before, violations_after, decision):

    os.makedirs("certificates", exist_ok=True)

    filename = f"cert_{manifest_name}.pdf"
    filepath = os.path.join("certificates", filename)

    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Kubernetes Security Compliance Certificate", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"Manifest: {manifest_name}", styles['Normal']))
    content.append(Paragraph(f"Violations Before: {violations_before}", styles['Normal']))
    content.append(Paragraph(f"Violations After: {violations_after}", styles['Normal']))
    content.append(Paragraph(f"Final Decision: {decision}", styles['Normal']))

    timestamp = str(datetime.datetime.now())
    content.append(Paragraph(f"Timestamp: {timestamp}", styles['Normal']))

    hash_value = hashlib.sha256((manifest_name + timestamp).encode()).hexdigest()
    content.append(Paragraph(f"Certificate Hash: {hash_value}", styles['Normal']))

    doc.build(content)

    return filename