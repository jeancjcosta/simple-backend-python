from src.server.instance import server
from src.models.user import *
from src.models.post import *
from src.controllers.init_db import *

if __name__ == '__main__':
    server.run()
