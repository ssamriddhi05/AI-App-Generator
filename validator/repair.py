def repair_schema(schema: dict, errors: list):

    # ensure structure exists
    if "api" not in schema:
        schema["api"] = {"endpoints": []}

    if "ui" not in schema:
        schema["ui"] = {"pages": []}

    if "auth" not in schema:
        schema["auth"] = {"type": "basic", "rules": []}

    endpoints = schema.get("api", {}).get("endpoints", [])

    for error in errors:

        # 🔥 FIX: missing GET /tasks
        if error == "GET /tasks endpoint missing":
            endpoints.append({
                "path": "/tasks",
                "method": "GET"
            })

        # 🔥 FIX: missing login
        if error == "POST /login endpoint missing":
            endpoints.append({
                "path": "/login",
                "method": "POST"
            })

        # 🔥 FIX: missing signup
        if error == "POST /signup endpoint missing":
            endpoints.append({
                "path": "/signup",
                "method": "POST"
            })

        # 🔥 FIX: Dashboard without tasks → add tasks table
        if error == "Dashboard exists but no tasks table":
            if "database" not in schema:
                schema["database"] = {"tables": {}}

            schema["database"]["tables"]["tasks"] = [
                "id", "title", "user_id"
            ]

    return schema