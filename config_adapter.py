def adapt_to_existing_format(user_config):
    """
    Convert user input into format expected by pipeline
    """

    manifest = {
        "name": user_config["application"],
        "runAsNonRoot": False   # intentionally unsafe to trigger repair
    }

    return manifest