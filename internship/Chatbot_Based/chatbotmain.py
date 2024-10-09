from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def add(a, b):
    sum=str(a + b)
    return sum

def subtract(a, b):
    return str(a - b)

def chat_response(userInput):
    responses = {
        "what is your name": "I am a rule-based chatbot.",
        "who are you": "I am a rule-based chatbot.",
        "what can you do": "I can sum or subtract two numbers and answer some preset questions.",
        "can you sum two numbers": "Sure! Please provide two numbers.",
        "can you subtract two numbers": "Sure! Please provide two numbers.",
        "how are you": "I am just a bunch of code, but thanks for asking!",
        "what's the weather like": "I can't check the weather, but you can!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the time": "I can't tell time, but your device can!",
        "what's your favorite color": "I don't have one, but I hear blue is quite popular.",
        "exit": "Goodbye! Have a great day!"
    }
    return responses.get(userInput.lower(), "I am not sure how to answer that. Try asking something else.")

def process_math_command(userInput):
    parts = userInput.split()
    if parts[0] == "sum":
        return add(int(parts[1]), int(parts[2]))
    elif parts[0] == "subtract":
        return subtract(int(parts[1]), int(parts[2]))
    else:
        return "Unknown math command. Use 'sum' or 'subtract'."

class ChatBotUI(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatBotUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(text="Welcome to the rule-based chatbot! How can I help you?\nWrite 'exit' to stop.", size_hint_y=0.1)
        self.add_widget(self.label)
        
        self.chat_input = TextInput(size_hint_y=0.1, multiline=False)
        self.chat_input.bind(on_text_validate=self.send_message)
        self.add_widget(self.chat_input)
        
        self.response_label = Label(text="", size_hint_y=0.8)
        self.add_widget(self.response_label)
        
        self.send_button = Button(text="Send", size_hint_y=0.1)
        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)
        
    def send_message(self, instance):
        userInput = self.chat_input.text
        
        self.chat_input.text = ""
        if userInput.lower().startswith("sum") or userInput.lower().startswith("subtract"):
            response = process_math_command(userInput)
        else:
            response = chat_response(userInput)
        self.response_label.text = response

class ChatBotApp(App):
    def build(self):
        return ChatBotUI()

if __name__ == '__main__':
    ChatBotApp().run()