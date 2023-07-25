from app_lampu import db
from datetime import datetime

def waktu_sekarang():
  return datetime.now()

class t_lampu(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  kode_lampu = db.Column(db.String(50), default='TES1')
  status_lampu = db.Column(db.Integer, default=0)
  last_changed = db.Column(db.DateTime, default=waktu_sekarang)