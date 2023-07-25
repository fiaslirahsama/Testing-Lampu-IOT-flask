from flask import Blueprint

app_lampu = Blueprint('lampu', __name__, static_folder='static', template_folder='templates')

from app_lampu.lampu import view_lampu