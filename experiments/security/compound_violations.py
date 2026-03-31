def run():

    manifest = {
        "runAsNonRoot": False,
        "privileged": True,
        "hostNetwork": True
    }

    violations = []

    if manifest["runAsNonRoot"] == False:
        violations.append("runAsRoot")

    if manifest["privileged"] == True:
        violations.append("privilegedContainer")

    if manifest["hostNetwork"] == True:
        violations.append("hostNetworkEnabled")

    print("Security Test: Compound Violations")
    print("Total violations detected:", len(violations))
    print("Violations:", violations)