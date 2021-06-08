import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO: uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

# ROUTES
@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    if drinks:
        return jsonify({
            'success' : True,
            'drinks' : [drink.short() for drink in drinks]
        }), 200
    else:
        abort(404)


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    drinks = Drink.query.all()
    if drinks:
        return jsonify({
            'success' : True,
            'drinks' : [drink.long() for drink in drinks]
        }), 200
    else:
        abort(404)


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    data = request.get_json()
    try:
        drink = Drink()
        drink.title = data['title']
        drink.recipe = json.dumps(data['recipe'])
        drink.insert()
    except Exception:
        abort(400)
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    }), 200


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, id):
    data = request.get_json()
    drink = Drink.query.filter_by(id=id).one_or_none()
    if not drink:
        abort(404)
    try:
        drink_title = data.get('title')
        drink_recipe = data.get('recipe')
        if drink_title:
            drink.title = drink_title
        if drink_recipe:
            drink.recipe = json.dumps(data['recipe'])
        drink.update()
    except Exception:
        abort(400)
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    }), 200


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    drink = Drink.query.filter_by(id=id).one_or_none()
    if not drink:
        abort(404)
    try:
        drink.delete()
    except Exception:
        abort(400)
    return jsonify({
        'success': True,
        'delete': id
    }), 200

# Error Handling

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'Unprocessable!'
    }), 422


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request!'
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'Unauthorized.'
    }), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Resource Not Found.'
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'Method Not Allowed.'
    }), 405


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal Server Error.'
    }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        'success': False,
        'error': error.status_code,
        'message': error.error['description']
    }), error.status_code
