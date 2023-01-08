from datetime import datetime
from src.models.user import *
from src.models.post import *


class UserService:

    """
    Method to get the user information.
    """
    def get_user(self, id):
        user = User.query.filter(User.id == id).first()
        n_posts = Post.query.filter(Post.user_id == id).count()

        return {
            'name': user.name,
            'date_joined': user.date_joined.strftime('%B %d, %Y'),
            'n_posts': n_posts
        }


user_service = UserService()
