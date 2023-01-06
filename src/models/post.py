from src.server.instance import server
import enum
from sqlalchemy import Integer, Enum, ForeignKey

db = server.db


class PostType(enum.Enum):
    POST = 1
    REPOST = 2
    QUOTE_POST = 3


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
