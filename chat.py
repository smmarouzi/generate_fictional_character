import openai
class ChatBot:
    
    def __init__(self, api_key) -> None:
        openai.api_key = api_key
        self.model = None
        self.engine = None

    def initialize_chatgpt(self):
        # Define the model and engine to use
        self.model = "gpt-3.5-turbo"
        self.engine = "davinci-codex"  # Or use "davinci" for previous GPT-3 models

        # Set up any additional configuration options
        openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a customer representative selling witches stuff."},
                {"role": "system", "content": "You can help customers with their inquiries."},
            ]
        )

        # Display a message to confirm initialization
        print(f"ChatGPT initialized with model: {self.model}, engine: {self.engine}")

    def chat_with_customer(self, input_message):
        # Create a list of messages to send to the ChatGPT model
        messages = [
            {"role": "system", "content": "You are a customer representative selling witches stuff."},
            {"role": "system", "content": "You can help customers with their inquiries."},
            {"role": "user", "content": input_message}
        ]

        # Send user input and conversation history to the ChatGPT model
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            engine=self.engine,
            max_tokens=100  # Adjust the value as needed
        )

        # Retrieve the bot's response from the model's choices
        bot_response = response.choices[0].message.content

        return bot_response

    def start_chat(self):
        self.initialize_chatgpt()
        print("Welcome! How can I assist you today?")

        while True:
            user_input = input("You: ")

            if user_input.lower() in ['bye', 'quit']:
                print("KW: Goodbye!")
                break

            bot_response = self.chat_with_customer(user_input)
            print("KW:", bot_response)

if __name__=="__main__":
    cb = ChatBot(input("Please enter your Chatgpt API key! "))
    cb.start_chat()