from flask import Flask
from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config().get('APP', 'name')


flask_app = Flask(__name__)


@flask_app.route('/')
def landing():
    return app_name


flask_app.run(
        host='0.0.0.0',
        port=8080
)