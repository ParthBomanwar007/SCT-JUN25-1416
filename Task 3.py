import re
def check_password_strength(password):
    strength = 0
    suggestions = []
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters.")
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add special characters (e.g., !@#$%).")
    if strength == 5:
        status = "Strong"
    elif strength >= 3:
        status = "Moderate"
    else:
        status = "Weak"

    return status, suggestions
password = input("Enter your password: ")
status, feedback = check_password_strength(password)

print(f"\nPassword Strength: {status}")
if feedback:
    print("Suggestions to improve:")
    for tip in feedback:
        print(f" - {tip}")
