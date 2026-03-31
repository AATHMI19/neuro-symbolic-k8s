def run():

    policy_a = {"runAsUser": 1000}
    policy_b = {"runAsUser": 2000}

    conflict = policy_a["runAsUser"] != policy_b["runAsUser"]

    print("Security Test: Policy Conflict")
    print("Policy A:", policy_a)
    print("Policy B:", policy_b)
    print("Conflict detected:", conflict)