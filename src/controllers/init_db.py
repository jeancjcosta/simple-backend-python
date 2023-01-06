from flask import Flask
from flask_restx import Api, Resource
from src.server.instance import server

app, api, db = server.app, server.api, server.db


@api.route('/initdb')
class InitDB(Resource):

    def post(self):
        db.create_all()
        return True, 200
