def apply_assumptions(intent: dict):

    # fix empty or unknown app type
    if not intent.get("app_type") or intent["app_type"] == "unknown":
        intent["app_type"] = "basic_app"

    # ensure features always exist
    if not intent.get("features"):
        intent["features"] = ["login"]

    # add default safety feature
    if "login" not in intent["features"]:
        intent["features"].append("login")

    return intent