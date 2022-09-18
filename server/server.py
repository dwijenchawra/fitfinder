import uuid
from flask import Flask, request, jsonify
from PIL import Image
from botocore.exceptions import ClientError
import logging
import boto3
import os
from colorthief import ColorThief
import webcolors

app = Flask(__name__)
s3_client = boto3.client('s3')
dynamo_client = boto3.client('dynamodb', region_name='us-east-1')



def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def getDominantColor(filepath):
    color_thief = ColorThief(filepath)
    dominant_color = color_thief.get_color(quality=30)
    actual_name, closest_name = get_colour_name(dominant_color)
    return closest_name


def upload_image(file_name):
    #RUN ML INFERENCE
    #RUN COLOR DETECTION

    dominantColor = getDominantColor("output.jpeg")
    mlCategory = "shirt"
    imID = str(uuid.uuid4())
    print(imID)

    clothingName = str(dominantColor).strip().capitalize() + " " + str(mlCategory).strip().capitalize()

    toBeSent = {
        "imageID" : {"S": imID},
        "clothingName" : {"S": clothingName},
        "clothingCategory" : {"S": mlCategory},
        "clothingColor" : {"S": dominantColor}
    }

    try:
        response = s3_client.upload_file(file_name, "helloworld9938", imID)
        response = dynamo_client.put_item(TableName="helloworld", Item=toBeSent)
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
    # download_image("download.jpeg", "testdownload.jpeg")
    # upload_image("download.jpeg")
    app.run(debug=True, host="0.0.0.0", port="5000", threaded="True")
