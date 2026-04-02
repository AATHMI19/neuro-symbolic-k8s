from input_handler import get_user_input
from config_adapter import adapt_to_existing_format
from experiments.proposed.neuro_symbolic_pipeline import run
from k8s_generator import generate_k8s_yaml, save_yaml
from certificate_generator import generate_certificate

def main():
    user_input = get_user_input()
    config = adapt_to_existing_format(user_input)

    print("\n🔹 INPUT CONFIGURATION")
    print("----------------------------------")
    print(config)

    print("\n🔍 Running Neuro-Symbolic Pipeline...\n")

    # Step 3: Run pipeline
    result = run(config, verbose=False)

    # Step 4: Clean Output
    print("\n📊 SECURITY ANALYSIS")
    print("----------------------------------")

    if result['violation']:
        print("❌ Violation Detected : YES")
        print("🔁 Auto Repair Applied")
    else:
        print("✅ No Violations Detected")

    print(f"🛠 Repairs Count      : {result['repairs']}")
    print(f"✅ Deployment Status  : {'SECURE' if result['verified'] else 'FAILED'}")

    severity = "HIGH" if result['violation'] else "NONE"
    print(f"⚠️ Risk Level        : {severity}")

    print("\n🔄 CONFIG TRANSFORMATION")
    print("----------------------------------")
    print("Before:", result['before'])
    print("After :", result['after'])

    print("\n🏅 CERTIFICATION")
    print("----------------------------------")
    print(f"Certificate Hash : {result['certificate']}")

    print("\n⚡ PERFORMANCE")
    print("----------------------------------")
    print(f"Latency : {result['latency']:.6f} seconds")

    print("\n📦 SERVICES CONFIGURATION")
    print("----------------------------------")

    for s in user_input["services"]:
        print(f"Service: {s['name']} | Image: {s['image']} | Port: {s['port']} | Replicas: {s['replicas']} | Exposure: {s['exposure']}")

    k8s_objects = generate_k8s_yaml(user_input)
    save_yaml(k8s_objects)

    cert_file = generate_certificate(result)

    print("\n📥 DOWNLOAD CERTIFICATE")
    print("----------------------------------")
    print(f"Path: {cert_file}")

if __name__ == "__main__":
    main()
