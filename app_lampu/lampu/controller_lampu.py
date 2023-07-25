from flask import request, jsonify
from app_lampu import db
from app_lampu.lampu import model_lampu
from datetime import datetime

def initLampu(kode_lampu):
  query_lampu = db.session.query(model_lampu.t_lampu).with_entities(model_lampu.t_lampu.kode_lampu,
                                                                   model_lampu.t_lampu.last_changed,
                                                                   model_lampu.t_lampu.status_lampu,)\
                                                    .filter(model_lampu.t_lampu.kode_lampu==kode_lampu)\
                                                    .first()
  if query_lampu == None:
    db.session.add(model_lampu.t_lampu(**{'kode_lampu':kode_lampu}))
    db.session.commit()
    query_lampu = db.session.query(model_lampu.t_lampu).with_entities(model_lampu.t_lampu.kode_lampu,
                                                                   model_lampu.t_lampu.last_changed,
                                                                   model_lampu.t_lampu.status_lampu,)\
                                                    .filter(model_lampu.t_lampu.kode_lampu==kode_lampu)\
                                                    .first()
  data_lampu = query_lampu._asdict()
  db.session.close()
  return jsonify(data_lampu)

def onOffLampu():
  status_lampu = request.form.get('value')
  kode_lampu = request.form.get('kode_lampu')
  db.session.query(model_lampu.t_lampu).filter(model_lampu.t_lampu.kode_lampu==kode_lampu).update({'status_lampu':status_lampu, 'last_changed':datetime.now()})
  db.session.commit()
  return initLampu(kode_lampu)