import json
from flask import Flask, request, jsonify
from PIL import Image
from google.cloud import storage
from botocore.exceptions import ClientError
import logging
import boto3
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "neat-dynamo-362802-b8eb099a1f3f.json"

app = Flask(__name__)


def upload_image(file_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, "helloworld9938", object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    

def download_image(blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket("hello_wrdl123")
    blob = bucket.blob(blob_name)
    blob.download_to_filename("download.jpeg")


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
    s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)
    upload_image("download.jpeg")
    # app.run(debug=True, host="0.0.0.0", port="5000", threaded="True")
