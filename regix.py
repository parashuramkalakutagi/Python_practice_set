import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Example usage:
email = "exampl@eemail.com"
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")



