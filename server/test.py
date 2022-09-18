import imageio as iio
import requests



if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/process'
    r = requests.post(url, files={'image': open('256x256bb.jpeg', 'rb')})
    print(r.text)