import json
import os

# Path to the JSON data file
data_file = os.path.join(os.path.dirname(__file__), 'data.json')

# Load the current data from the JSON file
def load_data():
    with open(data_file, 'r') as file:
        return json.load(file)

# Save data back to the JSON file
def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new prompt and responses
def add_prompt(prompt, responses):
    data = load_data()
    if prompt not in data:
        data[prompt] = responses
        save_data(data)
        print(f"Prompt '{prompt}' added successfully!")
    else:
        print(f"Prompt '{prompt}' already exists.")

# Remove a prompt
def remove_prompt(prompt):
    data = load_data()
    if prompt in data:
        del data[prompt]
        save_data(data)
        print(f"Prompt '{prompt}' removed successfully!")
    else:
        print(f"Prompt '{prompt}' not found.")

# Edit a prompt's responses
def edit_prompt(prompt, new_responses):
    data = load_data()
    if prompt in data:
        data[prompt] = new_responses
        save_data(data)
        print(f"Prompt '{prompt}' updated successfully!")
    else:
        print(f"Prompt '{prompt}' not found.")

# Main menu for the user to interact with
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Prompt")
        print("2. Remove Prompt")
        print("3. Edit Prompt")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            prompt = input("Enter the prompt: ")
            responses = input("Enter responses (comma-separated): ").split(',')
            add_prompt(prompt.strip(), [response.strip() for response in responses])
        elif choice == '2':
            prompt = input("Enter the prompt to remove: ")
            remove_prompt(prompt.strip())
        elif choice == '3':
            prompt = input("Enter the prompt to edit: ")
            responses = input("Enter new responses (comma-separated): ").split(',')
            edit_prompt(prompt.strip(), [response.strip() for response in responses])
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
