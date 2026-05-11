import requests

BASE_URL = "http://127.0.0.1:5000"

categorise_inputs = [
    "Chemical waste must be disposed safely",
    "Employees should follow attendance policy",
    "Tax reports are submitted yearly",
    "Customer data must remain private",
    "Machines should be inspected regularly",
    "Financial statements are audited annually",
    "Safety helmets are mandatory",
    "Environmental permits are required",
    "Operational procedures should be documented",
    "Companies must obey labor laws",

    "Workers must wear gloves",
    "Audit logs should be maintained",
    "Wastewater must be treated properly",
    "Payroll records should be accurate",
    "Fire exits must remain accessible",

    "Employee IDs should be verified",
    "Financial compliance is important",
    "Hazardous chemicals require monitoring",
    "Legal contracts must be reviewed",
    "Operational risks should be minimized",

    "Companies should reduce pollution",
    "Taxes must be paid on time",
    "Protective equipment is required",
    "Attendance records must be updated",
    "Accounting systems need audits",

    "Factory emissions should be controlled",
    "Data protection laws are mandatory",
    "Machine maintenance is necessary",
    "Safety drills should be conducted",
    "Environmental reports must be submitted"
]

query_inputs = [
    "What are environmental safety rules?",
    "What is financial audit?",
    "Why is attendance important?",
    "Explain data privacy laws",
    "What is waste disposal regulation?",

    "Why maintain accounting records?",
    "Why wear safety equipment?",
    "What is tax compliance?",
    "What are operational guidelines?",
    "What is environmental impact assessment?",

    "Why are audits important?",
    "What is workplace safety?",
    "Explain environmental permits",
    "What is compliance reporting?",
    "Why track employee attendance?",

    "What are labor laws?",
    "What is pollution control?",
    "Explain financial regulations",
    "What is operational compliance?",
    "Why document procedures?",

    "What is hazardous waste?",
    "Why conduct safety drills?",
    "Explain legal compliance",
    "What is employee monitoring?",
    "Why maintain records?",

    "What is risk management?",
    "Explain tax reporting",
    "Why inspect machines?",
    "What is data protection?",
    "Why use safety gear?"
]

print("\n===== FINAL PROMPT QA =====\n")

categorise_scores = []
query_scores = []

# TEST CATEGORISE
print("----- TESTING /categorise -----\n")

for text in categorise_inputs:

    response = requests.post(
        f"{BASE_URL}/categorise",
        json={"text": text}
    )

    data = response.json()

    print("Input:", text)
    print("Output:", data)

    score = int(input("Score out of 5: "))
    categorise_scores.append(score)

    print("-" * 50)

# TEST QUERY
print("\n----- TESTING /query -----\n")

for question in query_inputs:

    response = requests.post(
        f"{BASE_URL}/query",
        json={
            "question": question,
            "fresh": True
        }
    )

    data = response.json()

    print("Question:", question)
    print("Answer:", data["answer"])

    score = int(input("Score out of 5: "))
    query_scores.append(score)

    print("-" * 50)

# FINAL RESULTS
avg_cat = round(sum(categorise_scores) / len(categorise_scores), 2)
avg_query = round(sum(query_scores) / len(query_scores), 2)

print("\n===== FINAL QA REPORT =====")
print(f"Categorise Average: {avg_cat}/5")
print(f"Query Average: {avg_query}/5")

if avg_cat >= 4:
    print("Categorise Prompt: PASS")
else:
    print("Categorise Prompt: NEEDS IMPROVEMENT")

if avg_query >= 4:
    print("Query Prompt: PASS")
else:
    print("Query Prompt: NEEDS IMPROVEMENT")