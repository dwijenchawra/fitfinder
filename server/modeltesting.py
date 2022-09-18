import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf

model = tf.keras.models.load_model('mobilenet.h5')
classes = ['Blazer', 'Body', 'Dress', 'Hat', 'Hoodie', 'Longsleeve', 'Outwear',
 'Pants', 'Polo', 'Shirt', 'Shoes', 'Shorts', 'Skirt', 'T-Shirt', 'Top', 'Undershirt']



def predict_image(path):
    image = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    input_arr = input_arr.astype('float32') / 255.
    predictions = model.predict(input_arr, verbose=0)
    predicted_classes = np.argsort(predictions)
    predictions.sort()
    print(classes[predicted_classes[0][-1]])
    return classes[predicted_classes[0][-1]]
    # plt.title(f"{classes[predicted_classes[0][-1]]} - {round(predictions[0][-1] * 100,2)}% \n{classes[predicted_classes[0][-2]]} - {round(predictions[0][-2] * 100,2)}% \n{classes[predicted_classes[0][-3]]} - {round(predictions[0][-2] * 100,3)}%")
    # plt.imshow(image)
    # plt.axis('off')
    # plt.savefig("test.png")

predict_image("/home/dwijen/mmfashion/IMG_4728.jpeg")