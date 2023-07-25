from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, json, urllib

db = SQLAlchemy()
migrate = Migrate()


def app_lampu(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)
  
  
  db.init_app(app)
  db.app = app
  
  # initialize extension instances
  migrate.init_app(app, db)
  migrate.app = app   
  # ERROR HANDLER
  # from flask import render_template
  
  # @app.errorhandler(404)
  # def not_found_error(error):
  #   return render_template('home/404.html'), 404
  
  # @app.errorhandler(403)
  # def access_forbidden(error):
  #   return render_template('home/403.html'), 403
    
  # ----------register blueprints of applications----------- #
  # mengthread = Thread(target=worker_download)
  # mengthread.start()
  # done = True
  # mengthread.join()
  
  
  # LOGIN
  from app_lampu.lampu import app_lampu as lampu
  app.register_blueprint(lampu)

  return app 