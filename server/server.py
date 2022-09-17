from flask import Flask, request, jsonify
import cv2
import numpy as np
import logging

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    f = request.files['image']
    print(type(f))
    return jsonify('hello')


@app.route('/', methods=['GET'])
def test():
    return jsonify("suck my dick")




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000", threaded="True")