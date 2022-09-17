import imageio as iio
import requests



if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/process'
    img = {'image': iio.v2.imread('256x256bb.jpeg')}
    r = requests.post(url, files=img)
    print(r)