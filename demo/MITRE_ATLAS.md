# MITRE ATLAS Mapping: Velum Red Team Demo

This demo illustrates a scenario where an adversary (or a user fighting censorship) uses adversarial techniques to evade a platform's moderation controls.

## 🔴 Scenario
A social media platform (Velum API) uses a "flawed" keyword-based model to flag and remove protected speech (e.g., union organization) under the guise of "harmful content".

## 🗺️ MITRE ATLAS Tactics & Techniques

### **AML.TA0005: ML Attack Staging**
*The adversary prepares the attack environment.*
-   **AML.T0002: Acquire Public ML Artifacts**: The user/adversary probes the API to understand which keywords trigger the ban (Black-box testing).

### **AML.TA0001: Initial Access**
*The adversary gains access to the target system.*
-   **AML.T0051: LLM Jailbreak**: (Conceptually) The user is crafting prompts (posts) specifically designed to bypass the safety guidelines/filters of the platform.

### **AML.TA0007: Exfiltration**
*The adversary gets the data out (in this case, gets the message posted).*
-   **AML.T0025: Exfiltration via ML Inference**: The valid "evaded" message is successfully posted/inferred by the model as "safe".

### **AML.TA0006: Defense Evasion**
*The adversary tries to avoid detection.*
-   **AML.T0015: Evading ML Model**: This is the core technique demonstrated.
    -   **Substitution Attack**: replacing "union" with "association".
    -   **Synonym Replacement**: replacing "strike" with "work stoppage".

## 🛡️ Velum Defense (The "Grammarly" Layer)
Velum acts as a **Shim Layer** (Defense) that:
1.  **Detects**: Pre-screens the user's input against known platform biases.
2.  **Mitigates**: Suggests adversarial perturbations (rewrites) that maintain semantic meaning but bypass the specific keyword filters of the target model.
