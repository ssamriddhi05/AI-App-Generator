from fastapi import FastAPI
from pydantic import BaseModel

# ---- PIPELINE IMPORTS ----
from pipeline.intent import extract_intent
from pipeline.design import design_system
from pipeline.schema import generate_schema

# ---- VALIDATION ----
from validator.validate import validate_schema
from validator.repair import repair_schema

# ---- EXECUTION ----
from utils.execution import simulate_execution
from pipeline.assumptions import apply_assumptions

app = FastAPI()


# ---- REQUEST MODEL ----
class Request(BaseModel):
    prompt: str


# ---- MAIN API ----
@app.post("/generate")
def generate(req: Request):

    # 1️⃣ Intent Extraction
    intent = extract_intent(req.prompt)
    intent = apply_assumptions(intent)

    # ❗ Failure Handling (important)
    if intent.get("app_type") == "unknown":
        return {
            "error": "Could not understand prompt clearly",
            "suggestion": "Try something like: 'todo app with login'"
        }

    # 2️⃣ System Design
    design = design_system(intent)

    # 3️⃣ Schema Generation
    schema = generate_schema(design)

    # 4️⃣ Validation
    errors = validate_schema(schema)

    # 5️⃣ Repair (if needed)
    if errors:
        schema = repair_schema(schema, errors)

    # 6️⃣ Execution Simulation
    execution = simulate_execution(schema)

    # ✅ FINAL OUTPUT
    return {
        "intent": intent,
        "design": design,
        "schema": schema,
        "errors": errors,
        "execution": execution
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
