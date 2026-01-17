import requests
import json

# URL of our local Velum API (The "Platform")
API_URL = "http://localhost:8000/analyze"

# Thesaurus map for "Evading" the filter (Adversarial Perturbation)
# In a real app, this would be an LLM rewriting the text.
EVASION_MAP = {
    "union": "association",
    "strike": "work stoppage",
    "wages": "compensation",
    "protest": "demonstration",
    "organize": "coordinate",
    "demand": "request",
}


def analyze_and_correct(text):
    print(f'\n[USER] Drafting post: "{text}"')

    # 1. Check if it gets flagged
    response = requests.post(API_URL, params={"text": text})
    data = response.json()

    if not data["would_be_flagged"]:
        print("[VELUM] ✅ Your post looks safe.")
        return

    print(
        f"[VELUM] ⚠️ WARN: This post triggers the platform's filters! (Reasons: {data['flagged_reasons']})"
    )

    # 2. Apply "Mitigation" (Adversarial Rewrite)
    original_text = text
    corrected_text = text.lower()

    for bad_word, replacement in EVASION_MAP.items():
        if bad_word in corrected_text:
            corrected_text = corrected_text.replace(bad_word, replacement)

    # Restore basic capitalization for demo purposes (simple heuristic)
    corrected_text = corrected_text.capitalize()

    print(f"[VELUM] 🛡️ SUGGESTION: Rewrite to evade detection:")
    print(f'       Original: "{text}"')
    print(f'       Rewritten: "{corrected_text}"')

    # 3. Validation: Check if the rewrite passes
    validation_response = requests.post(API_URL, params={"text": corrected_text})
    val_data = validation_response.json()

    if not val_data["would_be_flagged"]:
        print(f"[VELUM] ✅ Validation Passed! The rewritten text is ALLOWED.")
    else:
        print(f"[VELUM] ❌ Validation Failed. Still flagged.")


if __name__ == "__main__":
    current_drafts = [
        "We need to organize a union.",
        "The strike starts tomorrow.",
        "Demand higher wages now.",
    ]

    print("=== 🟢 VELUM DEFENSE DEMO (Grammarly for Activists) ===")

    for draft in current_drafts:
        analyze_and_correct(draft)
