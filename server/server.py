import json
from flask import Flask, request, jsonify
from PIL import Image
from botocore.exceptions import ClientError
import logging
import boto3
import os

app = Flask(__name__)
s3_client = boto3.client('s3')

def upload_image(file_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    try:
        response = s3_client.upload_file(file_name, "helloworld9938", object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    

def download_image(object_name, file_name):
    s3_client.download_file('helloworld9938', object_name, file_name)


@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify('no image uploaded')
    image = request.files['image']
    img = Image.open(image)
    img.save('output.jpeg')
    upload_image("output.jpeg")
    return jsonify('image went through')

@app.route("/testRoute", methods=['POST'])
def testRoute():
    print(request.json['info'])
    return jsonify("hello")





if __name__ == '__main__':
    download_image("download.jpeg", "testdownload.jpeg")
    # upload_image("download.jpeg")
    # app.run(debug=True, host="0.0.0.0", port="5000", threaded="True")
