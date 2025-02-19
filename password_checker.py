import re

def check_password_strength(password):
    """
    Check password strength and return a score and feedback.
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Minimum 8 characters required.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1
        
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Missing uppercase letters")
        
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Missing lowercase letters")
        
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Missing numbers")
        
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Missing special characters")
        
    # Calculate strength based on score
    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"
        
    return strength, feedback

def main():
    print("Password Strength Checker")
    print("-" * 25)
    
    while True:
        # Get password input
        password = input("Enter a password (or 'q' to quit): ")
        
        if password.lower() == 'q':
            break
            
        strength, feedback = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")
        print("\n")

if __name__ == "__main__":
    main()
