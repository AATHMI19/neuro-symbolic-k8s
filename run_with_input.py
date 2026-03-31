from input_handler import get_user_input
from config_adapter import adapt_to_existing_format
from experiments.proposed.neuro_symbolic_pipeline import run


def main():
    # Step 1: Input
    user_input = get_user_input()

    # Step 2: Adapt config
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


if __name__ == "__main__":
    main()