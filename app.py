import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set OpenAI API key and model engine
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-002"

# Define a function to generate text based on user input
def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text.strip()
    return message

# Define a route to handle user input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        prompt = request.form['prompt']

        # Generate text based on the user's prompt
        generated_text = generate_text(prompt)

        # Return the generated text to the user
        return render_template('index.html', prompt=prompt, generated_text=generated_text)

    # If the request is a GET request, render the index.html template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
