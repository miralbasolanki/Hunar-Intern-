import re

def password_strength(password):
    if len(password) < 6:
        return "Weak"

    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if has_upper and has_lower and has_digit and has_special and len(password) >= 12:
        return "Strong"
    elif (has_upper or has_lower) and has_digit and has_special and len(password) >= 8:
        return "Okay"
    else:
        return "Weak"

password = input("Enter a password to check its strength: ")
strength = password_strength(password)
print(f"The password is {strength}.")
