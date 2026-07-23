# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), > 10 chars (Strong)

password = input("Enter the password: ")
password_length = len(password)

if password_length < 6:
    Strength = "Weak"
elif password_length <= 10:
    Strength = "Medium"
else:
    Strength = "Strong"

print("Strength:", Strength)