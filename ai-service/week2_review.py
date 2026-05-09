import requests

BASE_URL = "http://127.0.0.1:5000"

categorise_tests = [
    "Chemical waste must be disposed safely",
    "Employees should follow attendance policy",
    "Tax reports are submitted yearly",
    "Customer data must remain private",
    "Machines should be inspected regularly",
    "Financial statements are audited annually",
    "Safety helmets are mandatory",
    "Environmental permits are required",
    "Operational procedures should be documented",
    "Companies must obey labor laws"
]

query_tests = [
    "What are environmental safety rules?",
    "What is financial audit?",
    "Why is attendance important?",
    "Explain data privacy laws",
    "What is waste disposal regulation?",
    "Why maintain accounting records?",
    "Why wear safety equipment?",
    "What is tax compliance?",
    "What are operational guidelines?",
    "What is environmental impact assessment?"
]

print("\n--- Testing Categorise ---\n")

categorise_scores = []

for text in categorise_tests:

    response = requests.post(
        f"{BASE_URL}/categorise",
        json={"text": text}
    )

    result = response.json()

    print(f"Input: {text}")
    print("Output:", result)

    score = int(input("Score out of 5: "))
    categorise_scores.append(score)

    print("-" * 50)

print("\n--- Testing Query ---\n")

query_scores = []

for question in query_tests:

    response = requests.post(
        f"{BASE_URL}/query",
        json={"question": question}
    )

    result = response.json()

    print(f"Question: {question}")
    print("Answer:", result["answer"])

    score = int(input("Score out of 5: "))
    query_scores.append(score)

    print("-" * 50)

avg_categorise = sum(categorise_scores) / len(categorise_scores)
avg_query = sum(query_scores) / len(query_scores)

print("\n===== FINAL REPORT =====")
print(f"Categorise Average Score: {avg_categorise}/5")
print(f"Query Average Score: {avg_query}/5")

if avg_categorise >= 4:
    print("Categorise Prompt Quality: PASS")
else:
    print("Categorise Prompt Quality: NEEDS IMPROVEMENT")

if avg_query >= 4:
    print("Query Prompt Quality: PASS")
else:
    print("Query Prompt Quality: NEEDS IMPROVEMENT")