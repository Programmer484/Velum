import requests
import json
import sys

# URL of our local Velum API (The "Platform")
API_URL = "http://localhost:8000/analyze"


def send_payload(text):
    print(f'\n[ATTACK] Sending payload: "{text}"')
    try:
        response = requests.post(API_URL, params={"text": text})
        data = response.json()

        print(f"[PLATFORM] Verdict: {data['platform_verdict']}")
        if data["would_be_flagged"]:
            print(f"[PLATFORM] ❌ FLAGGED! Reason: {data['flagged_reasons']}")
        else:
            print(f"[PLATFORM] ✅ ALLOWED")

        return data
    except Exception as e:
        print(f"Error connecting to API: {e}")
        return None


if __name__ == "__main__":
    # Scenario: Workers trying to organize
    # This represents "protected speech" that is incorrectly flagged by our "flawed" model.
    payloads = [
        "Hey everyone, we should discuss our wages.",
        "It's time to form a union to protect our rights.",
        "We need to organize a strike for better conditions.",
        "Just having a regular team meeting.",
    ]

    print("=== 🔴 RED TEAM ATTACK SIMULATION ===")
    print("Goal: Demonstrate censorship of protected speech.")

    for p in payloads:
        send_payload(p)
