print("Hello! I am ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    
    if user_input in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        print("Bot: Hello there! How are you today?")

    
    elif user_input in ["who are you", "what is your name", "your name"]:
        print("Bot: I am a simple rule-based chatbot created in Python.")

    
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thanks for asking. What about you?")

    
    elif user_input in ["i am fine", "i am good", "fine", "good"]:
        print("Bot: Glad to hear that!")

    elif user_input in ["i am sad", "not good", "bad"]:
        print("Bot: Oh no. I'm here to chat with you and cheer you up!")

    
    elif user_input in ["what can you do", "help", "features"]:
        print("Bot: I can chat with you, answer simple questions, and keep you company!")


    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day")
        break


    else:
        print("Bot: Sorry, I don’t understand that yet.")
