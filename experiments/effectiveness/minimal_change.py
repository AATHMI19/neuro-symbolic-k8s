def run():

    original = {
        "image": "nginx",
        "runAsNonRoot": False
    }

    repaired = {
        "image": "nginx",
        "runAsNonRoot": True
    }

    changes = 0

    for key in original:
        if original[key] != repaired[key]:
            changes += 1

    print("Effectiveness: Minimal Change")
    print("Fields modified:", changes)
    print("Original:", original)
    print("Repaired:", repaired)