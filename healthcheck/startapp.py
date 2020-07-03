#!/usr/bin/python3
from flask import Flask, render_template, request
import json
from statistics_collector.collectors import Collectors
#import niaasauth

app = Flask(__name__)


@app.route('/status', methods=['GET'])
def message():
    """
    Searches for the mac from the input of the payload,
    if mac is found a dict is returned containing info of its
    location in the network
    """
    response = Collectors.get_errors()
    return response


"""
Start the application if run as main
"""
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
