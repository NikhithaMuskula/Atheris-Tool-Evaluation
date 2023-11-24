import os

def process_user_input(user_input):
    # The vulnerability lies in using user input directly in a command
    command = f"echo {user_input}"

    # Execute the command using os.system
    os.system(command)

# Get user input
user_input = input("Enter something: ")

# Process the user input
process_user_input(user_input)