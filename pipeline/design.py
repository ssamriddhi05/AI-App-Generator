def design_system(intent):

    features = intent.get("features", [])

    entities = []
    roles = []
    flows = []

    if "login" in features:
        entities.append("User")
        roles.append("user")
        flows.append("authentication")

    if "tasks" in features:
        entities.append("Task")
        flows.append("create_task")
        flows.append("delete_task")

    if "dashboard" in features:
        flows.append("view_dashboard")

    if "analytics" in features:
        flows.append("view_analytics")

    return {
        "entities": entities,
        "roles": roles,
        "flows": flows
    }