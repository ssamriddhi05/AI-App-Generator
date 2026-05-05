def extract_intent(user_input: str):

    text = user_input.lower()

    if not text or len(text.strip()) < 3:
        return {
            "app_type": "unknown",
            "features": [],
            "confidence": "low"
        }

    # fuzzy handling
    if "todo" in text:
        features = ["login", "tasks"]

    elif "crm" in text:
        features = ["login", "dashboard", "contacts"]

    elif "app" in text:
        features = ["login"]

    else:
        features = ["login"]

    return {
        "app_type": "general_app",
        "features": features,
        "confidence": "medium"
    }
