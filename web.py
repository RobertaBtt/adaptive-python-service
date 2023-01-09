from flask import Flask, request
from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config_conf().get('APP', 'name')


flask_app = Flask(__name__)


@flask_app.route('/')
def landing():
    return app_name


@flask_app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)

        return "Webhook received!"


flask_app.run(
        host='0.0.0.0',
        port=8080
)
