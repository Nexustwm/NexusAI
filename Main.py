import random
import json
import os

# Path to the JSON data file
data_file = os.path.join(os.path.dirname(__file__), 'data', 'data.json')

# Load the data from the JSON file
def load_data():
    with open(data_file, 'r') as file:
        return json.load(file)

# Function to get a response for a given prompt
def get_response(prompt):
    data = load_data()
    prompt = prompt.lower()  # Normalize prompt to lowercase
    if prompt in data:
        return random.choice(data[prompt])  # Return a random response
    else:
        return "Sorry, I don't understand that."

# Main function to interact with the chatbot
def chat():
    print("Hello! I'm your chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            response = get_response(user_input)
            print(f"Bot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
