import os
from datetime import datetime


def generate_certificate(result):

    os.makedirs("certificates", exist_ok=True)

    app_name = result['after']['name']
    filename = f"certificates/cert_{app_name}.txt"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""
========================================
   KUBERNETES SECURITY CERTIFICATE
========================================

Application Name : {app_name}
Status           : {'SECURE' if result['verified'] else 'UNSAFE'}

Violations Found : {result['violation']}
Repairs Applied  : {result['repairs']}

Certificate Hash : {result['certificate']}

Generated At     : {now}

========================================
Certified by Neuro-Symbolic Engine
========================================
"""

    with open(filename, "w") as f:
        f.write(content)

    print(f"\n📄 Certificate saved: {filename}")

    return filename
