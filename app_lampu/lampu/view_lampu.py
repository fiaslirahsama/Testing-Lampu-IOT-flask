from app_lampu.lampu import app_lampu, controller_lampu
from flask import render_template, redirect, url_for, request, jsonify
import os

@app_lampu.route('/')
def lampu():
  return render_template('lampu.html')

@app_lampu.route('/onoff-init-<kode>', methods=['GET'])
def onoff_init(kode):
  return controller_lampu.initLampu(kode)

@app_lampu.route('/onoff', methods=['POST'])
def onoff():
  return controller_lampu.onOffLampu()

@app_lampu.route('/get-data-lampu-<kode>', methods=['GET'])
def get_data_lampu(kode):
  return controller_lampu.initLampu(kode)
