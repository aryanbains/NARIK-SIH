ṇ# import files
from flask import Flask, render_template, request
import bot

app = Flask(__name__)

doc = bot.chat()


@app.route("/")
def home():
    return render_template("new.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(doc.get_response(user_input = userText))


if __name__ == "__main__":
    print("bruh")
    app.run()
    print("bruh")
