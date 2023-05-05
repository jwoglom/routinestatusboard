#!/usr/bin/env python3

from flask import Flask, Response, request, abort, render_template, jsonify, send_from_directory
import os
import collections


ROUTE_TOKEN = ''
static_url_path = '/static'
if os.getenv('ROUTE_TOKEN'):
    ROUTE_TOKEN = '/' + os.getenv('ROUTE_TOKEN')
    static_url_path = ROUTE_TOKEN + '/static'

app = Flask(__name__, static_folder='static', static_url_path = static_url_path)

# Log messages with Gunicorn
if not app.debug:
    import logging
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

# gunicorn wants one, and flask run the other...
try:
    from models.timedate import Time
    from config import routines, options
except ImportError:
    try:
        from .models.timedate import Time
        from .config import routines, options
    except ImportError:
        app.logger.warning("Using example config")
        try:
            from example_config import routines, options
        except ImportError:
            from .example_config import routines, options

def process_options(orig):
    options = {}
    if 'switchover_time' in orig:
        options['switchover_time'] = Time.of(orig['switchover_time'])

    return options

@app.route(ROUTE_TOKEN + '/')
def index_route():
    return send_from_directory('templates', 'index.html')

@app.route(ROUTE_TOKEN + '/routines')
def routines_route():
    return jsonify([r.to_json() for r in routines])

completed = collections.defaultdict(list)

@app.route(ROUTE_TOKEN + '/completed')
def completed_route():
    return jsonify(completed)

@app.route(ROUTE_TOKEN + '/options')
def options_route():
    return jsonify(process_options(options))

@app.route(ROUTE_TOKEN + '/complete')
def complete_route():
    rid = request.args.get('id')
    day = request.args.get('day')
    print('complete:', rid, day)
    completed[day].append(rid)
    return 'ok'