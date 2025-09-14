def chatbot():
    print("Welcome to CodeAlpha Chatbot! Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How can I help you today?")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        elif user_input == "exit":
            print("Bot: Chat ended.")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

chatbot()
