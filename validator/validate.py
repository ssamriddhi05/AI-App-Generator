def validate_schema(schema: dict):
    errors = []

    # ---- BASIC STRUCTURE CHECKS ----
    if "database" not in schema:
        errors.append("Missing database")

    if "api" not in schema:
        errors.append("Missing API")

    if "ui" not in schema:
        errors.append("Missing UI")

    if "auth" not in schema:
        errors.append("Missing auth")

    # ---- SAFE EXTRACTION ----
    tables = schema.get("database", {}).get("tables", {})
    endpoints = schema.get("api", {}).get("endpoints", [])

    # convert endpoints → (path, method)
    endpoint_set = [(e.get("path"), e.get("method")) for e in endpoints]

    # ---- CROSS-LAYER VALIDATION ----

    # 🔥 1. Tasks table → GET /tasks must exist
    if "tasks" in tables and ("/tasks", "GET") not in endpoint_set:
        errors.append("GET /tasks endpoint missing")

    # 🔥 2. Users table → login/signup must exist
    if "users" in tables:
        if ("/login", "POST") not in endpoint_set:
            errors.append("POST /login endpoint missing")
        if ("/signup", "POST") not in endpoint_set:
            errors.append("POST /signup endpoint missing")

    # 🔥 3. UI pages consistency
    pages = schema.get("ui", {}).get("pages", [])
    if "Dashboard" in pages and "tasks" not in tables:
        errors.append("Dashboard exists but no tasks table")

    return errors