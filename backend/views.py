from app import app
from flask import render_template, request, jsonify
from core import *

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/blueprints/', methods=['GET'])
def blueprints():
	return jsonify(nodeBlueprints);

@app.route('/newnode/', methods=['GET', 'POST'])
def newNode():
	req=parse_request(request)
	return create_node(req.code)

@app.route('/delete/', methods=['POST'])
def delete():
	return jsonify(parse_request(request));


@app.route('/connect/', methods=['POST'])
def connect():
	return '';

@app.route('/disconnect/', methods=['POST'])
def disconnect():
	return '';


def parse_request(request):
	class Req:
		pass

	for field in request.get_json().items():
		setattr(Req, field[0], field[1])
	return Req()
