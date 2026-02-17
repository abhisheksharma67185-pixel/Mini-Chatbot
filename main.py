# Mini Chatbot.
import random
responses = {}
responses["hi"] = ["Hello!", "Hi there!", "Hey!"]
responses["how are you?"] = ["I'm good, thanks!", "Doing well, how about you?", "I'm fine, thank you!"]
responses["what's your name?"] = ["I'm Chatbot!"]
def chatbot():
    while True:
        
        user_input = input("you: ").lower()
        if user_input == 'exit':
            print('goodbye!')
            break
        response = responses.get(user_input, ["Sorry, I don't understand that."])
        print(random.choice(response))