def simulate_execution(schema):

    return {
        "database_tables": list(schema["database"]["tables"].keys()),
        "total_tables": len(schema["database"]["tables"]),
        "api_endpoints": schema["api"]["endpoints"],
        "total_endpoints": len(schema["api"]["endpoints"]),
        "ui_pages": schema["ui"]["pages"],
        "total_pages": len(schema["ui"]["pages"]),
        "status": "Executable ✅"
    }