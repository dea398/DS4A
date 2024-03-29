# import requests

import os
from os.path import exists, join

from flask import Flask, jsonify, make_response, send_from_directory
from flask_cors import CORS

from constants import CONSTANTS
from sample_data import patient_data, patient_data_rank, sample_data

app = Flask(__name__, static_folder='build')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# MasterDetail Page Endpoint
@app.route(CONSTANTS['ENDPOINT']['MASTER_DETAIL'])
def get_master_detail(prob):
    if prob == 'rank':
        return jsonify(patient_data_rank['text_assets'])
    else:
        return jsonify(patient_data['text_assets'])

# Grid Page Endpoint
@app.route(CONSTANTS['ENDPOINT']['GRID'])
def get_grid():
    return jsonify(sample_data['member_assets'])


# @app.after_request
# def add_header(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
#     return response

# Catching all routes
# This route is used to serve all the routes in the frontend application after deployment.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # if app.debug:
    #     return requests.get('http://localhost:3000/{}'.format(path)).text
    file_to_serve = path if path and exists(
        join(app.static_folder, path)) else 'index.html'
    return send_from_directory(app.static_folder, file_to_serve)

# Error Handler
@app.errorhandler(404)
def page_not_found(error):
    json_response = jsonify({'error': 'Page not found'})
    return make_response(json_response, CONSTANTS['HTTP_STATUS']['404_NOT_FOUND'])


if __name__ == '__main__':
    app.run(port=CONSTANTS['PORT'])
