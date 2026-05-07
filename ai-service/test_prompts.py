from services.groq_client import call_groq

test_inputs = [
    "Company must follow environmental safety rules",
    "Annual financial audit is required",
    "Employees must report to work on time",
    "Data privacy laws must be followed",
    "Waste disposal must follow regulations",
    "Company should maintain proper accounting records",
    "Workers must wear safety equipment",
    "Tax compliance is mandatory",
    "Operational guidelines must be documented",
    "Environmental impact assessment is required"
]

def test_categorise():
    print("\n--- Testing Categorise ---\n")

    for text in test_inputs:
        prompt = f"""
Classify into one of: Legal, Financial, Operational, Environmental

Text: {text}

Return JSON:
{{
  "category": "...",
  "confidence": 0.0,
  "reasoning": "..."
}}
"""
        result = call_groq(prompt)
        print(f"\nInput: {text}")
        print(f"Output: {result}")


def test_query():
    print("\n--- Testing Query ---\n")

    for text in test_inputs:
        prompt = f"""
Answer based on compliance knowledge:

Question: {text}
"""
        result = call_groq(prompt)
        print(f"\nQuestion: {text}")
        print(f"Answer: {result}")


if __name__ == "__main__":
    test_categorise()
    test_query()