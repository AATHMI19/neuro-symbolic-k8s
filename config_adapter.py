def adapt_to_existing_format(user_config):

    manifest = {
        "name": user_config["application"],
        "services": user_config["services"],

        # 🔹 Default policies (if not provided)
        "runAsNonRoot": False,
        "privileged": False,
        "readOnlyRootFilesystem": False,
        "allowPrivilegeEscalation": True,
        "resources": None,
        "imagePullPolicy": None
    }

    return manifest
