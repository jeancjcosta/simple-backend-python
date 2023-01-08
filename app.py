from src.server.instance import server
from src.models.user import *
from src.models.post import *
from src.controllers.init_db import *
from src.controllers.homepage_controller import *
from src.controllers.user_profile_controller import *

if __name__ == '__main__':
    server.run()
