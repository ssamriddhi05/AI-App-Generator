import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import generate
# ---- TEST PROMPTS ----
test_prompts = [
    "todo app with login",
    "crm with dashboard",
    "simple app",
    "",
    "build something",
    "todo app with payments",
    "chat app",
    "app",
    "crm with roles",
    "todo"
]


# ---- RUN TESTS ----
def run_tests(generate_function):
    results = []

    for prompt in test_prompts:
        try:
            output = generate_function(prompt)

            success = "schema" in output
            results.append({
                "prompt": prompt,
                "success": success,
                "errors": output.get("errors", [])
            })

        except Exception as e:
            results.append({
                "prompt": prompt,
                "success": False,
                "error": str(e)
            })

    return results


# ---- METRICS FUNCTION (YAHI HAI TUMHARA PART) ----
def calculate_metrics(results):
    total = len(results)
    success = sum(1 for r in results if r["success"])

    return {
        "total_tests": total,
        "success_rate": success / total
    }

if __name__ == "__main__":

    from main import generate

    # wrapper to match function format
    def wrapper(prompt):
        return generate(type("obj", (object,), {"prompt": prompt}))

    results = run_tests(wrapper)
    metrics = calculate_metrics(results)

    print("RESULTS:\n", results)
    print("\nMETRICS:\n", metrics)