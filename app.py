#!/usr/bin/env python3

from flask import Flask, Response, request, abort, render_template, jsonify, send_from_directory

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
    return jsonify(routines)