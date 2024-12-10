from flask import render_template
from app import app
from analyzer.capture import get_packets

@app.route('/')
def index():
    packets = get_packets()  # Get live packets from capture module
    return render_template('index.html', packets=packets)

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return a 204 (No Content) response for favicon requests
