def adapt_to_existing_format(user_config):

    services = user_config["services"]

    manifest = {
        "name": user_config["application"],
        "runAsNonRoot": False,
        "services": services   # ✅ ADD THIS
    }

    return manifest
