#!/usr/bin/env python3

from flask import Flask, Response, request, abort, render_template, jsonify, send_from_directory
import collections

app = Flask(__name__, static_folder='static')

# Log messages with Gunicorn
if not app.debug:
    import logging
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)


try:
    from .config import routines
except ImportError:
    from .example_config import routines
    app.logger.warning("Using example config")


@app.route('/')
def index_route():
    return send_from_directory('templates', 'index.html')

@app.route('/routines')
def routines_route():
    return jsonify([r.to_json() for r in routines])

completed = collections.defaultdict(list)

@app.route('/completed')
def completed_route():
    return jsonify(completed)

@app.route('/complete')
def complete_route():
    rid = request.args.get('id')
    day = request.args.get('day')
    print('complete:', rid, day)
    completed[day].append(rid)
    return 'ok'