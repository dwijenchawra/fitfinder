import json
from turtle import clone
import uuid
from flask import Flask, request, jsonify
from PIL import Image
from botocore.exceptions import ClientError
import logging
import boto3
import os

app = Flask(__name__)
s3_client = boto3.client('s3')
dynamo_client = boto3.client('dynamodb')

def upload_image(file_name):
    #RUN ML INFERENCE
    #RUN COLOR DETECTION

    dominantColor = None
    mlCategory = None
    imID = uuid.uuid4()

    clothingName = str(dominantColor).strip().capitalize 
    + str(mlCategory).strip().capitalize()

    toBeSent = {
        "imageID" : imID,
        "name" : clothingName,
        "category" : mlCategory,
        "color" : dominantColor
    }

    try:
        response = s3_client.upload_file(file_name, "helloworld9938", imID)
        response = dynamo_client.put_item(toBeSent)
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
