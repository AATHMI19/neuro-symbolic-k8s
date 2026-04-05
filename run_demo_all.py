import sys
import os

# Ensure src is accessible
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from run_with_input import run_pipeline   # or your main pipeline function


def demo_cases():
    return [

        # 🔴 CASE 1: FAILURE (NO REPAIR)
        {
            "name": "frontend-risky",
            "services": [
                {
                    "name": "frontend",
                    "image": "nginx:latest",
                    "port": 80,
                    "replicas": 1,
                    "exposure": "ClusterIP"
                }
            ],
            "runAsNonRoot": False,
            "privileged": True,
            "readOnlyRootFilesystem": False,
            "allowPrivilegeEscalation": True
        },

        # 🟡 CASE 2: AUTO REPAIR
        {
            "name": "frontend-risky",
            "services": [
                {
                    "name": "frontend",
                    "image": "nginx:latest",
                    "port": 80,
                    "replicas": 1,
                    "exposure": "ClusterIP"
                }
            ],
            "runAsNonRoot": False,
            "privileged": False,
            "readOnlyRootFilesystem": False,
            "allowPrivilegeEscalation": True
        },

        # 🟢 CASE 3: CLEAN
        {
            "name": "payments-compliant",
            "services": [
                {
                    "name": "payments",
                    "image": "nginx:1.25.3",
                    "port": 80,
                    "replicas": 2,
                    "exposure": "ClusterIP"
                }
            ],
            "runAsNonRoot": True,
            "privileged": False,
            "readOnlyRootFilesystem": True,
            "allowPrivilegeEscalation": False
        }
    ]


def run_all_demos():
    print("=" * 80)
    print("RUNNING ALL DEMO CASES (PIPELINE MODE)")
    print("=" * 80)

    cases = demo_cases()

    for i, case in enumerate(cases, 1):
        print("\n" + "=" * 80)
        print(f"STEP {i:02d} - {case['name'].upper()}")
        print("=" * 80)

        result = run_pipeline(case)

        print("\n📊 RESULT")
        print("----------------------------------")
        print("Violations:", result.get("violation"))
        print("Repairs:", result.get("repairs"))
        print("Status:", "SECURE" if result.get("verified") else "UNSAFE")
        print("Certificate:", result.get("certificate"))


if __name__ == "__main__":
    run_all_demos()
