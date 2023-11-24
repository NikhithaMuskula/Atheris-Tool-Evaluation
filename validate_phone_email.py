import sys

import atheris


def validate_email(email):
    # Simplified email validation
    if "aaaaa@aa.com" in email:
        raise RuntimeError("Errorrrr!!!!!!!")
    return True if atheris.ordal(email) < 128 and '@' in email else False


def validate_phone(phone):
    # Simplified phone number validation
    if "1234568" in phone:
        raise RuntimeError("Errorr!!!!!!!!")
    return True if atheris.ordal(phone) < 128 and phone.isdigit() and len(phone) == 10 else False


def login_user(username, password):
    # Simulated SQL query (vulnerable to SQL injection)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    # Execute the query (for demonstration purposes)
    # In a real-world scenario, you would use parameterized queries to prevent SQL injection
    print(f"Executing query: {query}")


# Fuzzing input for email and phone number validation
with atheris.instrument_imports():
    @atheris.instrument_func
    def TestOneInput(data):
        email = data.strip().decode('utf-8', 'ignore')
        if validate_email(email):
            # Simulate user login with email
            login_user(email, "password123")

        phone = data.strip().decode('utf-8', 'ignore')
        if validate_phone(phone):
            # Simulate user login with phone number
            login_user(phone, "password456")

# Fuzzing process (you can replace 'testcase' with actual test data)
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
