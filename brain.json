import re
import json

# Load or initialize the bot's brain
def load_brain():
    try:
        with open("brain.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Initial brain data
        initial_brain = {
            "add": ["addition"],
            "addition": ["addition"],
            "subtract": ["subtraction"],
            "subtraction": ["subtraction"],
            "multiply": ["multiplication"],
            "multiplication": ["multiplication"],
            "divide": ["division"],
            "division": ["division"]
        }
        return initial_brain

def save_brain(brain):
    with open("brain.json", "w") as file:
        json.dump(brain, file)

# Extract numbers and operation based on known terms in the brain
def extract_numbers_and_operation(statement, brain):
    numbers = list(map(int, re.findall(r'\b\d+\b', statement)))
    operation = None

    for term, synonyms in brain.items():
        if any(synonym in statement for synonym in synonyms):
            operation = term
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
        user_input = input("You: ").strip().lower()
        numbers, operation = extract_numbers_and_operation(user_input, brain)

        if not numbers:
            print("AI: I didn't find any numbers in your statement. Please provide numbers for the calculation.")
            continue

        if not operation:
            print("AI: I am confused, tell me which calculation you would like to perform (e.g., addition, subtraction, multiplication, division).")
            clarification = input("You: ").strip().lower()

            # Check if the clarification matches known operations
            known_operations = ["addition", "subtraction", "multiplication", "division"]
            if clarification in known_operations:
                operation = clarification
            else:
                print(f"AI: I don't know what '{clarification}' means. Could you explain it?")
                definition = input("You: ").strip().lower()

                # Check if the definition is one of the known operations
                if definition in known_operations:
                    # Add the new term as a synonym for the known operation
                    if clarification not in brain[definition]:
                        brain[definition].append(clarification)
                    save_brain(brain)
                    operation = definition
                else:
                    print("AI: Sorry, I still don't understand that operation.")
                    continue

        result = perform_calculation(numbers, operation)

        if result is not None:
            print(f"AI: The result of the {operation} is: {result}")
        else:
            print("AI: I am still confused. Could you please clarify your request?")

# Run the AI bot
ai_bot()
