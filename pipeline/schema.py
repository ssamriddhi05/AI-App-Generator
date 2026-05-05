def generate_schema(design):

    entities = design.get("entities", [])

    tables = {}
    endpoints = []

    if "User" in entities:
        tables["users"] = ["id", "email", "password"]
        endpoints.append({"path": "/login", "method": "POST"})

    if "Task" in entities:
        tables["tasks"] = ["id", "title", "user_id"]
        endpoints.append({"path": "/tasks", "method": "POST"})

    if "Analytics" in design.get("flows", []):
        endpoints.append({"path": "/analytics", "method": "GET"})

    return {
        "database": {"tables": tables},
        "api": {"endpoints": endpoints},
        "ui": {
            "pages": ["Login Page"] + (["Dashboard"] if "Task" in entities else [])
        },
        "auth": {
            "type": "basic",
            "rules": ["user can access only their data"]
        }
    }