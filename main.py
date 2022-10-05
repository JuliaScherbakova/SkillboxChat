from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__, static_folder="./client", template_folder="./client") #Настройки приожения
all_messages = []

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime('%H:%M')
    }
    if len(sender) < 3 or len(sender) > 100:
        # add_message("Invalid Name")
        return {"result": False, "Error": "Invalid Message"}
    elif len(text) < 1 or len(text) >3000:
        # add_message("Invalid Message")
        return {"result": False, "Error": "Invalid Message"}
    else:
        all_messages.append(new_message)
        # add_message(sender, text)
        return {"result": True}



@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


#API для получения отправки сообщения /send_message?sender=Mike&text=Hello
@app.route("/send_message")
def send_message():
    sender = request.args["sender"]
    text = request.args["text"]
    add_message(sender, text)
    return {"result": True}


@app.route("/")
def hello_page():
    return "Welcome to SkillboxChat5000"

@app.route("/info")
def info_page():
    info = len(all_messages)
    return {"Amount of messages": info}

app.run()
