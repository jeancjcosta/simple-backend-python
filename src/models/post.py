from src.server.instance import server
import enum
from sqlalchemy import Integer, Enum, ForeignKey
from flask_restx import fields

db = server.db


class PostType(enum.Enum):
    POST = 1
    REPOST = 2
    QUOTE_POST = 3

    @staticmethod
    def get(id):
        if id == "POST":
            return PostType.POST
        elif id == "REPOST":
            return PostType.REPOST
        elif id == "QUOTE_POST":
            return PostType.QUOTE_POST
        return None


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(777), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    post_type = db.Column(db.Enum(PostType), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey("post.id"), nullable=True)

    def __init__(self, content, created_at, post_type=PostType.POST, user_id=None, post_id=None):
        self.content = content
        self.created_at = created_at
        self.post_type = post_type
        self.user_id = user_id
        self.post_id = post_id

    def as_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.strftime('%B %d, %Y'),
            'post_type': self.post_type.name,
            'user_id': self.user_id,
            'post_id': self.post_id
        }


post = server.api.model('Post', {
    'id': fields.Integer(description='The instance id - should be empty while recording new post', required=False),
    'content': fields.String(description='The content of the post', required=True, min_length=1, max_length=777),
    'created_at': fields.Date(description='The date of the post in the format "yyyy-mm-dd".', required=True),
    'post_type': fields.String(description='The type of the post (1 - post / 2 - repost / 3 - quote)', required=True),
    'user_id': fields.Integer(description='The user id of the post', required=True),
    'post_id': fields.Integer(description='The referenced post if it is a repost or quote post.', required=False)
})

homepage_request = server.api.model('homepage_request', {
    'user_id': fields.Integer(description='The user id of the post', required=True),
    'only_mine': fields.Boolean(description='Indicate if should bring only the user posts.', required=True),
    'start_date': fields.Date(description='The beginning of the date range of posts in the format "yyyy-mm-dd".', required=False),
    'end_date': fields.Date(description='The end date of range of posts in the format "yyyy-mm-dd".', required=False),
    'page_number': fields.Integer(description='The number of the page to be loaded', required=False)
})