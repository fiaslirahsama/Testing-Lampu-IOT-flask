import os, pymysql
from os.path import realpath
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database

# # set the base directory
# basedir = os.path.abspath(os.path.dirname(__file__))

# set the base directory
BASEDIR = os.path.abspath(os.path.dirname(realpath(__file__)))
def validateDatabase(DATABASE_FILE, DB_NAME):
    engine = create_engine(DATABASE_FILE)
    if not database_exists(engine.url): # Checks for the first time  
        create_database(engine.url)     # Create new DB    
        print(f"{DB_NAME} Database Created") # Verifies if database is there or not.
    else:
        print(f"Database {DB_NAME} Running")


# Create the super class
class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  
# Create the development config
class DevelopmentConfig(Config):
  DEBUG = True
  FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST')
  FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
  HOST = str(os.environ.get("DB_HOST"))
  DATABASE = str(os.environ.get("DB_DATABASE"))
  USERNAME = str(os.environ.get("DB_USERNAME"))
  PASSWORD = str(os.environ.get("DB_PASSWORD"))
  
  DATABASE_FILE = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
    
  validateDatabase(DATABASE_FILE, DATABASE)
  SQLALCHEMY_DATABASE_URI = DATABASE_FILE
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True 
  

  
  
