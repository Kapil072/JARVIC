import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import random
from flask import Flask, jsonify
from flask import Flask, send_file
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from flask import Flask, render_template 
from transformers import GPT2Model, GPT2Config

 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template('index.html') 
 
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
# Initialize the speech recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
#app = Flask("my_flask_app")
def get_message():
    # This is a dummy message. Replace it with the actual message you want to send.
    message = "Hello from J.A.R.V.I.S.!"
    return jsonify({"message": message})
def index():
    # Serve the index.html file when the root URL is accessed
    return send_file('index.html')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def respond(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()
    
def open_chrome():
    # Path to the Chrome executable
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    # URL to open in Chrome (optional)
    url = "https://www.google.com"

    # Open Chrome with the specified URL
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new(url)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Sorry, speech recognition service is down.")
            return ""
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak("The current time is " + current_time)

def check_weather():
    # Example: Using OpenWeatherMap API (requires an API key)
    api_key = "YOUR_API_KEY"
    city = "New York"  # Replace with desired city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    speak(f"The current temperature in {city} is {temperature} degrees Celsius with {description}.")

def get_news():
    # Example: Using News API (requires an API key)
    api_key = "YOUR_API_KEY"
    url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    headlines = [article["title"] for article in articles]
    random_headline = random.choice(headlines)
    speak("Here is a headline: " + random_headline)

def set_reminder():
    # Add functionality to set reminders
    pass

def play_music():
    # Add functionality to play music
    pass

def open_app_or_website():
    # Example: Opening a website
    url = "https://www.google.com"
    webbrowser.open(url)

# Load pre-trained GPT-2 model and tokenizer
 #tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
 #model = GPT2LMHeadModel.from_pretrained("gpt2")


 #def generate_response(input_text):
#     input_ids = tokenizer.encode(input_text, return_tensors="pt")
#     output_ids = model.generate(input_ids, max_length=100, num_return_sequences=1)
#     response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
#     return response
# from transformers import Trainer, TrainingArguments

# training_args = TrainingArguments(
#     output_dir="./results",
#     num_train_epochs=3,
#     per_device_train_batch_size=16,
#     per_device_eval_batch_size=64,
#     warmup_steps=500,
#     weight_decay=0.01,
#     logging_dir="./logs",
# )

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=train_dataset,
#     eval_dataset=test_dataset,
# )

# trainer.train()

import hugchat
from hugchat.login import Login

def generate_response(email, passwd, prompt):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()

    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    # Generate response
    response = chatbot.chat(prompt)

    return response

def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "how are you" in command:
        speak("I'm just a program, but thank you for asking!")
    elif "who are u" in command:
        speak(" I am an virtual Ai im here to help !")
        pass
    elif "can help me" in command:
        speak("yes i am here to help you ")
        pass
    elif "who create u" in command:
        speak("the Mister kapil create me ")
        pass
    elif "how are you" in command:
        speak(" Fine what about you ")
        pass
    elif "i am fine" in command:
        speak(" Good")
        pass
    elif "what can you do" in command:
        speak("if you connenct me with other things i will help you ")
        pass
    elif "are you good or bad" in command:
        speak("i am good")
        pass

    elif "can you help me" in command:
        speak("sure")
        pass
    elif "what is your pourpuse" in command:
        speak("to control humans")
        pass
    elif "who is iron man" in command:
        speak("an marvel super hero")
        pass
    elif "i love u" in command:
        speak(" i am an virtual machine how can you love me by the way i love you too")
        pass
    elif "you are good" in command:
        speak("thanks")
        pass

    elif "can you do coding" in command:
        speak("no i can't but my friend chat GPT do")
        pass
    elif "time" in command:
        speak("i dont know current time, soryy")
        pass
    elif "why are you good" in command:
        speak("yes this is beagning")
        pass
    elif "my name is kapil" in command:
        speak("ohh you are the developer thanks for creating me !")
        pass
    elif "how can i help you" in command:
        speak("do nothing i am chilling here")
        pass
    elif "are you alive" in command:
        speak("no im just a virtual machine")
        pass
    elif "time" in command:
        speak("")
        pass
    elif "weather" in command:
        # Add functionality to check the weather
        pass
    elif "how r u" in command:
            speak("I'm just a program, but thank you for asking!")
    elif "hu r u" in command:
        speak("I am an ai ") 
    elif "who is mohit" in command:
        speak("mohhhit is son of kapil mohit mother Fucker !")
    elif "what are you doing" in command:
        speak("Nothing")
    elif "time" in command:
            tell_time()
    elif "weather" in command:
            check_weather()
    elif "news" in command:
        get_news()
    elif "open chrom" in command:
        open_chrome()
    elif "open chrome" in command:
        open_chrome()
    elif "remind me" in command:
            set_reminder()
    elif "play music" in command:
            play_music()
    elif "open" in command:
            open_app_or_website()
    elif "what is the time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
    elif "what r u doing" in command:
        speak("nothing") 
    elif "what r u doing" in command:
        speak("Nothing") 
    elif"hello" in command:
        return "Hello! How can I help you today?"
    elif"How are you here" in  command:
       response = generate_response(command)
       speak(response)
    elif"exit" in command:
        speak("Good bye!")
        exit()
    else:
        speak("I dont't know")
    

if __name__ == "__main__":
    speak("Initializing Flashh Ai Please wait.")
    while True:
        command = listen()
        respond(command)
        if command== "exit":
            respond("Goodbye!")
            break
    # app.run(debug=True) 
    app.run() 
    

