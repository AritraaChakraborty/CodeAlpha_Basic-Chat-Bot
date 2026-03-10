def simple_chatbot():
    print("Chatbot: Hello! I'm a simple bot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm functioning perfectly!")
        elif "your name" in user_input:
            print("Chatbot: I'm the CodeAlpha Basic Bot.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: That's interesting! Tell me more.")

simple_chatbot()

