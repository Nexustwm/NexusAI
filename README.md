# NexusAI Project

This project is a simple AI chatbot that interacts with the user based on prompts and responses stored in a `data.json` file. The chatbot allows you to manage its prompts and responses through the `train.py` script and chat with it using the `main.py` script.

### 1. **data.json**

The `data.json` file contains prompts and their corresponding responses. Prompts are mapped to lists of possible responses, and the chatbot randomly selects one of the available responses when asked a question.

Example structure of `data.json`:

`
{
  "hello": ["Hi there!", "Hello! How can I assist you today?", "Hey! How's it going?"],
  "how are you": ["I'm just a bot, but I'm doing well, thank you!", "I'm functioning as expected!", "I'm good, how about you?"],
  "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"]
}
`

### 2. train.py

This script is used to manage the prompts and responses stored in the data.json file. It allows you to:

- Add a new prompt and responses.
- Remove a prompt.
- Edit existing responses.

To interact with the script, run train.py in the data folder, and follow the options presented in the menu.

# 3. main.py

This is the main script where the chatbot interacts with the user. It loads the prompts and responses from the data.json file and responds based on the user's input.

To start the chatbot, run main.py:

`python main.py`

### Running the Project
Manage Prompts and Responses with train.py:

Navigate to the data folder.
Run the train.py script to add, remove, or edit prompts and responses.

### Features
- Add, remove, and edit prompts using train.py.
- Chatbot interaction in the command line with main.py.
- Randomized responses: The bot randomly selects from a list of responses for each prompt.
