import re
import json
import os

# Load or initialize the bot's brain
def load_brain():
    if os.path.exists("brain.json"):
        with open("brain.json", "r") as file:
            return json.load(file)
    else:
        # Initial brain data
        initial_brain = {
            "add": "addition",
            "addition": "addition",
            "subtract": "subtraction",
            "subtraction": "subtraction",
            "multiply": "multiplication",
            "multiplication": "multiplication",
            "divide": "division",
            "division": "division"
        }
        return initial_brain

def save_brain(brain):
    with open("brain.json", "w") as file:
        json.dump(brain, file)

# Extract numbers and operation based on known terms in the brain
def extract_numbers_and_operation(statement, brain):
    numbers = list(map(int, re.findall(r'\b\d+\b', statement)))
    operation = None

    for term in brain:
        if term in statement:
            operation = brain[term]
            break

    return numbers, operation

def perform_calculation(numbers, operation):
    if operation == "addition":
        result = sum(numbers)
    elif operation == "subtraction":
        result = numbers[0] - sum(numbers[1:])
    elif operation == "multiplication":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "division":
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    else:
        result = None

    return result

def ai_bot():
    brain = load_brain()
    print("Hello! I can help you with basic arithmetic calculations.")
    while True:
        user_input = input("You: ")
        numbers, operation = extract_numbers_and_operation(user_input, brain)

        if not numbers:
            print("AI: I didn't find any numbers in your statement. Please provide numbers for the calculation.")
            continue

        if not operation:
            print("AI: I am confused, tell me which calculation you would like to perform (e.g., addition, subtraction, multiplication, division).")
            clarification = input("You: ")
            numbers, operation = extract_numbers_and_operation(user_input + " " + clarification, brain)

            if not operation:
                operation = clarification.strip().lower()

            if operation not in ["addition", "subtraction", "multiplication", "division"]:
                print(f"AI: I don't know what '{operation}' means. Could you explain it?")
                definition = input("You: ")
                brain[operation] = definition.strip().lower()
                save_brain(brain)
                operation = definition.strip().lower()

        result = perform_calculation(numbers, operation)

        if result is not None:
            print(f"AI: The result of the {operation} is: {result}")
        else:
            print("AI: I am still confused. Could you please clarify your request?")

# Run the AI bot
ai_bot()
