import random
import json
from datetime import datetime

# Load responses from a JSON file
with open("responses.json", "r") as file:
    data = json.load(file)
    responses = data["responses"]
    random_responses = data["random_responses"]

#agent names
agent_names=["Sara","Lata","Josh","Shina","Shubu"]
agent_name= random.choice(agent_names)

#Timestamp function
def get_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M]")

#greetings
user_name=input("Hi there, What's your name? ")
greeting=f"Hello, {user_name}! My name is {agent_name}. How can i help you today?"
print(greeting)

#opening log file
with open("chat_log.txt", "a") as log_files:
    log_files.write(f"{get_timestamp()} Bot: {greeting}\n")

#conditions and loop
    while True:
         user_input= input(">").strip().lower()
         log_files.write(f"{get_timestamp()} User: {user_input}\n")

         if user_input in ["quit", "bye", "the end", "exit"]:
             farewell=f"Goodbye, {user_name}! It was wonderful talking to you!"
             log_files.write(f"{get_timestamp()} Bot: {farewell}\n")
             print(farewell)
             break

    
    #keyword detection and response
         response_found= False
         for keyword, response in responses.items():
            if keyword in user_input:
             log_files.write(f"{get_timestamp()} Bot: {response}\n")
             print(response)
             response_found= True
             break
   
    #random responses if no keyword is found
         if not response_found:
             random_responses = random.choice(random_responses)
             log_files.write(f"{get_timestamp()} Bot: {random_responses}\n")
             print(random_responses)

  