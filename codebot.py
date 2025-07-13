def code_bot():
    print("👋 Hello! I'm your Python Code Bot. Ask me about Python basics!")
    print("Type 'exit' to quit.\n")

    while True:
        giuser_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Bot: Goodbye! Happy coding! 👋")
            break

        elif "for loop" in user_input:
            print("\nBot: Here's a basic for loop example:")
            print("for i in range(5):")
            print("    print(i)  # prints numbers from 0 to 4\n")

        elif "if statement" in user_input or "conditional" in user_input:
            print("\nBot: Here's how you write an if statement in Python:")
            print("x = 10")
            print("if x > 5:")
            print("    print('x is greater than 5')\n")

        elif "function" in user_input:
            print("\nBot: This is how you define a function in Python:")
            print("def greet(name):")
            print("    print(f'Hello, {name}!')\n")

        elif "list" in user_input:
            print("\nBot: Here's how to create and access a list in Python:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("print(fruits[1])  # Outputs: banana\n")

        else:
            print("\nBot: 🤔 Sorry, I don't understand that yet.")
            print("Try asking about: 'for loop', 'if statement', 'function', or 'list'.\n")


# Run the bot
if __name__ == "__main__":
    code_bot()

