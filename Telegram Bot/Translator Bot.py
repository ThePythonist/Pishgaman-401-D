from flask import Flask, request
import mtranslate
import telepot
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "BOT"
bot = telepot.Bot('YOUR_TOKEN')
bot.setWebhook("https://USER.pythonanywhere.com/{}".format(secret), max_connections=1)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg["text"] == "/start":
            bot.sendMessage(chat_id, "From The Web, Hello Welcome To My Bot")
        else:
            output = mtranslate.translate(msg["text"], "en", "fa")
            bot.sendMessage(chat_id, output)
    else:
        bot.sendMessage(chat_id, "I only understand text messages :D")


app = Flask(__name__)


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    print(update)
    if "message" in update:
        handle(update["message"])
    return "OK"
