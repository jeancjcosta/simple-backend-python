from datetime import datetime
import json
from src.models.post import *


class HomepageService:
    """
    method to create a post instance based on information received on data
    :param data
    :return post: return a post object
    """
    def fill_post(self, data):
        post_instance = Post(
            str(data['content']),
            datetime.strptime(data['created_at'], '%Y-%m-%d'),
            str(data['post_type']),
            int(data['user_id']),
            int(data['post_id']) if 'post_id' in data is not None else None
        )
        return post_instance

    """
    This method queries the posts with pagination.
    """
    def get_posts(self, data):
        post_list = []
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d') if 'end_date' in data else datetime.today().replace(microsecond=0)
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d') if 'start_date' in data else datetime.min
        if data['only_mine'] == 'true':
            posts = Post.query\
                .filter(Post.user_id == int(data['user_id']),
                        Post.created_at >= start_date,
                        Post.created_at <= end_date
                        ).paginate(page=int(data['page_number']), per_page=10).items
        else:
            posts = Post.query \
                .filter(
                        Post.created_at >= start_date,
                        Post.created_at <= end_date
                        ).paginate(page=int(data['page_number']), per_page=10).items
        for item in posts:
            post_list.append(item.as_dict())
        return post_list


homepage_service = HomepageService()
