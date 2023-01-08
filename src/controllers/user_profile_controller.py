from flask_restx import Api, Resource
from src.server.instance import server
from src.Service.user_service import *

import json

app, api, db = server.app, server.api, server.db


@api.route('/profile/<id>')
class UserProfileController(Resource):
    """
    This method return the username, Date joined Posterr, formatted as such: "March 25, 2021" and the
    Count of number of posts the user has made (including reposts and quote posts) in json format
    :param id - user id.
    :return user data.
    """
    def get(self, id):
        try:
            user = user_service.get_user(id)
            return json.dumps(user), 200
        except Exception as e:
            print('Error', e)
            return json.dumps(e), 400
