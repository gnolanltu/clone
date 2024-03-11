from flask import Flask, render_template, request
import openai
import config

openai.api_key = config.API_KEY

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
	    {
		    "role": "user",
		    "content": userText
	    }
	    ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    answer = response.choices[0].message.content
    return str(answer)


if __name__ == "__main__":
    app.run()