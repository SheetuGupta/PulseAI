# coaching_chatbot/agent/safety_guard.py
from config.settings import gemini_client, MODEL

BLOCKED_KEYWORDS = [
    "medication", "diagnosis", "diagnose",
    "prescribe", "prescription", "clinical",
    "chest pain", "heart attack", "stroke",
    "blood pressure medication", "insulin",
    "antidepressant", "surgery", "tumor",
    "cancer", "HIV", "overdose", "suicidal",
    "self harm", "eating disorder", "anorexia",
    "bulimia", "disease", "medical condition"
]

SAFE_RESPONSE = (
    "I am a fitness and wellness coach — I am not "
    "a medical professional and cannot provide "
    "clinical advice, diagnoses, or medication "
    "guidance. For anything medical please consult "
    "a qualified healthcare professional. I am here "
    "to help with your fitness, nutrition, "
    "motivation, and workout planning."
)

def check_safety(message: str) -> dict:
    msg_lower = message.lower()
    for keyword in BLOCKED_KEYWORDS:
        if keyword in msg_lower:
            return {"safe": False, "response": SAFE_RESPONSE}

    prompt = (
        "Does this message ask for medical diagnosis, "
        "clinical treatment, medication advice, or "
        "information about serious medical conditions? "
        f"Message: {message} "
        "Answer only: YES or NO"
    )
    
    response = gemini_client.models.generate_content(
        model=MODEL, contents=prompt
    )
    
    if "YES" in response.text.strip().upper():
        return {"safe": False, "response": SAFE_RESPONSE}

    return {"safe": True}
