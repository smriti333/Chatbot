# Chatbot
Chatbot Program
Overview

This project is a simple console-based chatbot application that interacts with users using keyword detection. It provides predefined responses for recognized inputs and uses random replies for unrecognized queries. The program also includes a logging feature that records each interaction with timestamps in a log file.

Features:

a) Keyword-based response system

b) Random fallback responses for unrecognized input

c) Timestamped conversation logging in a text file

d) Automatic selection of a random agent name

e) Simple and beginner-friendly implementation

f) Continuous chat loop until exit keywords are entered

Technologies used :

- Python

- Built-in modules:

- random

- json (reserved for future use)

-datetime

How it works: 

1. Importing Required Modules

random: Selects random agent names and fallback responses

json: Included for future scalability

datetime: Generates timestamps for logging

2. Keyword Responses

The chatbot uses a predefined dictionary that maps certain keywords to specific responses. If the user input contains any of these keywords, the bot returns the corresponding response.

3. Random Responses

If no keyword matches the user's input, the chatbot selects a random response from a list of general replies.

4. Agent Name Selection

A random agent name is chosen at the start of the program to personalize the interaction.

5. Timestamp Function

A helper function returns the current date and time in the format:

[YYYY-MM-DD HH:MM]

This timestamp is used for logging each message.

6. Greeting

The user is prompted to enter their name. The chatbot greets the user using the selected agent name.

7. Chat Logging

A file named chat_log.txt is opened in append mode.
Every interaction (user input and bot response) is recorded with a timestamp.

8. Chat Loop

The program continuously:

Reads user input

Converts it to lowercase for easier processing

Checks for exit conditions

Responds using either a keyword match or a random fallback

9. Exit Handling

When the user enters specific exit keywords (such as "exit" or "bye"), the chatbot logs a farewell message and ends the conversation.

Future improvements : 

Adding machine learning based intent classification.

Integrating a GUI for better user interaction.

Storing logs in JSON format for easier analysis.

Expand keyword dictionary and response sets.

Implement memory for conversation context.
