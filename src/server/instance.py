from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
import os


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        self.db = SQLAlchemy(self.app)
        self.api = Api(
            self.app,
            version='1.0',
            title='Sample',
            description='description',
            doc='/docs'
        )

    def run(self) -> None:
        self.app.run(debug=True, host="0.0.0.0", port=8080)


server = Server()
