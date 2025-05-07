import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import random
from flask import Flask, jsonify, render_template
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    # Get the user's command from the request data
    command = request.json['command']
    # Call the respond function with the user's command as input
    response = respond(command)
    # Return the response as JSON
    return jsonify({'response': response})

# The rest of the code for the respond function, speech recognition, etc. goes here

if __name__ == "__main__":
    # Initialize the speech recognizer and the text-to-speech engine
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    # Load pre-trained GPT-2 model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    # Start the Flask app
    app.run(debug=True)