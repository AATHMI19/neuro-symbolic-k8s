def run(manifest=None, verbose=False):

    import hashlib
    import time

    if manifest is None:
        manifest = {
            "name": "demo",
            "runAsNonRoot": False
        }

    original_manifest = manifest.copy()

    if verbose:
        print("Neuro-Symbolic Pipeline")
        print("Generated manifest:", manifest)

    # 🔍 Detection
    violation = not manifest.get("runAsNonRoot", False)

    if verbose:
        print("Policy violation detected:", violation)

    # 🔁 Repair
    repairs = 0
    if violation:
        manifest["runAsNonRoot"] = True
        repairs += 1

    # ✅ Verification
    verified = manifest["runAsNonRoot"]

    if verbose:
        print("Repairs applied:", repairs)
        print("Deployment verified:", verified)

    # 🏅 Certification
    start = time.time()
    certificate = hashlib.sha256(str(manifest).encode()).hexdigest()
    latency = time.time() - start

    if verbose:
        print("Certificate:", certificate)
        print("Pipeline latency:", latency)

    # ✅ Return structured output
    return {
        "violation": violation,
        "repairs": repairs,
        "verified": verified,
        "certificate": certificate,
        "latency": latency,
        "before": original_manifest,
        "after": manifest
    }