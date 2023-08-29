# Chatbot using GPT-3.5

This is a simple command line chatbot powered by OpenAI's GPT-3.5 language model. The chatbot engages in conversational interactions with users, providing responses based on the input it receives. It's capable of having a customizable personality and utilizes the OpenAI API for text generation.

## Prerequisites

Before using the chatbot, ensure you have the following components set up:

1. Python: Make sure you have Python 3.x installed on your system.
2. OpenAI API Key: Obtain an API key from OpenAI (you'll need an account).
3. `.env` File: Create a `.env` file in the same directory as the script and store your OpenAI API key in it. The format should be as follows:

```
OPENAI_API_KEY=your_api_key_here
```

## Installation

1. Clone or download the repository containing the chatbot script.
2. Install the required Python packages using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Open a terminal and navigate to the directory containing the script.
2. Run the chatbot using the following command:

```
python chatbot.py [-p|--personality PERSONALITY]
```

Optional arguments:

- `-p|--personality`: Specify the desired personality of the chatbot. This is a brief summary of how you want the chatbot to come across in conversations. If not provided, a default personality ("Friendly and helpful") will be used.

## Example

```bash
python chatbot.py -p "Inquisitive and witty"
```

## Conversation Flow

The chatbot engages in a continuous conversation loop with the user. It prompts the user for input and responds based on the conversation history. It uses the GPT-3.5 Turbo model for text generation.

The conversation alternates between the user and the assistant, with the assistant considering the entire conversation history to generate contextually relevant responses.

To exit the conversation, simply press `Ctrl + C`.

## Notes

- This chatbot is a basic implementation for demonstration purposes and can be extended for more complex use cases.
- Ensure you follow OpenAI's guidelines and terms of use while interacting with the API.

Feel free to modify and adapt the script to suit your needs. Happy chatting! 🤖💬
