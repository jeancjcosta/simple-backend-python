import json

from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from src.server.instance import server
from src.Service.homepage_service import homepage_service
from src.models.post import Post, post, homepage_request

app, api, db = server.app, server.api, server.db


@api.route('/homepage')
class HomepageController(Resource):
    """
    This method brings a feed of posts (including reposts and quote posts), starting with the latest 10 posts.
    Older posts are loaded on-demand passing the number of the page to show the next 10 posts.
    The consumer has to pass the code indicating if wants "All" or "Only mine" posts to be shown.
    The consumer has to pass the range date to filter the posts.
    """

    # @api.expect(homepage_request)
    @api.doc(params={
        'user_id': {'in': 'query', 'description': 'The user id of the post', 'type': 'string'},
        'only_mine': {'in': 'query', 'description': 'Indicate if should bring only the user posts.', 'type': 'boolean'},
        'start_date': {'in': 'query',
                       'description': 'The beginning of the date range of posts in the format "yyyy-mm-dd".', 'type': 'date'},
        'end_date': {'in': 'query', 'description': 'The end date of range of posts in the format "yyyy-mm-dd".', 'type': 'date'},
        'page_number': {'in': 'query', 'description': 'The number of the page to be loaded', 'type': 'integer'}
    })
    def get(self):
        data = request.args
        try:
            post_list = homepage_service.get_posts(data)
            return json.dumps(post_list), 200
        except Exception as e:
            print('Error', e)
            return json.dumps(e), 400

    """
    This method will record new post in the database.  
    """

    @api.expect(post)
    def post(self):
        data = api.payload
        try:
            post_instance = homepage_service.fill_post(data)
            db.session.add(post_instance)
            db.session.commit()
            return json.dumps("Success"), 200
        except Exception as e:
            print('Error', e)
            return json.dumps(e), 400
