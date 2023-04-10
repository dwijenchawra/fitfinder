# FitFinder

### Won Best Use of AWS at Purdue Hello World 2022

![gallery](https://user-images.githubusercontent.com/30065475/210120322-6d63bf88-c449-4fc5-b7d3-1f3ffae0b6f6.jpg)

## Inspiration

I saw my outfit in the mirror one day and thought to myself: I can do better.

## What it does

Users can take pictures of the pieces of clothing in their wardrobe. Then, using an algorithm that considers factors like color and style, our app puts the pieces of clothing together to create visually appealing outfits.

## How we built it

We created the mobile app with React Native. From the app, images of articles of clothing are sent to a Flask server hosted on a Ubuntu server through an HTTP post request. We chose not to use the cloud because we were doing inference on the backend, and all the free tier machines were either too low power, or did not offer GPU support. These images are then uploaded to an AWS S3 Bucket where they are kept for later use. We keep the image metadata in AWS DynamoDB.

## Challenges we ran into

Finding a model or API that could accurately tell us what type of clothing the image contained proved very difficult. Sending images to a flask server through the mobile app was also something we struggled with for a while. Finally, general time management and making sure we finished the project on time was also difficult, as this is a fairly ambitious project.

## Accomplishments that we're proud of

We’re mainly proud of the UI we created for the app and the model we trained for analyzing images of clothing.

## What we learned

We learned more about React Native, Javascript in general, AWS, and Flask.

## What's next for FitFinder

One of our current ideas to improve FitFinder is implementing a feature that can suggest clothes that the user should consider buying. We would additionally like to add a way for the program to also take into account that some clothes have already been used and need to be washed.
