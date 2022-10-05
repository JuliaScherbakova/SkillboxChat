from utils import set_timeout, fetch

last_seen_id = 0
#Нахоидм элменты интерфейса по их ID
send_message = document.getElementById("send_message")
sender = document.getElementById("sender")
message_text = document.getElementById("message_text")
chat_window = document.getElementById("chat_window")

#добавляет новое сообщение в список сообщений
def append_message(message):
    # создаем HTML-элемент представляющий сообщeния
    # добавляе его в список сообщений (chat_window)
    item = document.createElement("li") # тег для элемента списка
    item.className = "list-group-item" # определяет, как элемент выглядит
    item.innerHTML = f'[<b>{message["sender"]}</b>]: <span>{message["text"]}</span><span class="badge text-bg-light text-secondary">{message["time"]}</span>'
    chat_window.prepend(item)

#вызывается при клике на send_message
async def send_message_click(e):
    #отправляем запрос
    await fetch(f"/send_message?sender={sender.value}&text={message_text.value}", method="GET")
    #очищаем поле
    message_text.value = ""


#загружает новые сообщения с сервера и отображает их
async def load_fresh_messages():
    #загружать все сообщения каждую секунду (большой трафик)
    result = await fetch("/get_messages", method="GET")
    chat_window.innerHTML = "" #очищем окно сообщений
    data = await result.json()
    all_messages = data["messages"]  # Берем список сообщений из ответа сервера
    for msg in all_messages:
        append_message(msg)
    set_timeout(1, load_fresh_messages)  # Запускаем загрузку заново через секунду
    # 2. Загружать только новые сообщения


# Устнаваливаем действие при клике
# send_message.onclick = send_message_click
# append_message({"sender": "MIKE", "text": "Add Message Works!!!", "time": "25:88"})
# load_fresh_messages()
