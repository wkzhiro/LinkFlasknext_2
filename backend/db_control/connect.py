# uname() error回避
import platform
print(platform.uname())

from sqlalchemy import create_engine
import sqlalchemy

# import os
# main_path = os.path.dirname(os.path.abspath(__file__))
# path = os.chdir(main_path)
# print(path)
# engine = create_engine("sqlite:///CRM.db", echo=True)

import config

user = config.DB_USER
port = config.PORT
password = config.PASSWORD
host = config.HOST
db_name = config.DATABASE

engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}")
