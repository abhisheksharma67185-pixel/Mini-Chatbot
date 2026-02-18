# Mini Chatbot.
import random
responses = {}
responses["hi"] = ["Hello!", "Hi there!", "Hey!"]
responses["how are you?"] = ["I'm good, thanks!", "Doing well, how about you?", "I'm fine, thank you!"]
responses["what's your name?"] = ["I'm Chatbot!"]
responses["bye"] = ["Goodbye!", "See you later!", "Take care!"]
def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "hi":
            print(random.choice(responses["hi"]))
        elif user_input == "how are you?":
            print(random.choice(responses["how are you?"]))
        elif user_input == "what's your name?":
            print(random.choice(responses["what's your name?"]))
        elif user_input == "bye":
            print(random.choice(responses["bye"]))
            break
        else:
            print("Sorry, I don't understand that.")
if __name__ == "__main__":
    chatbot()