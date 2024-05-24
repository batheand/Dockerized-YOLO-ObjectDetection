# Dockerized-YOLO-ObjectDetection
Using Flask and Yolov4, this project creates a working YOLO microservice.

### Before starting

Please run the download_model.py, which will download the onnx model, as the file is around 250 mbs it might take a while.

### Why ONNX?

ONNX acts as a translator for AI models. It allows you to train a model in any framework and then deploy it anywhere, regardless of the hardware, software, or programming language used. This simplifies deployment, reduces complexity, and improves performance.

### How it works?

The model takes requests the image, then handles all the rest in one main method and many helper methods.

## Getting Started

### Download the model 
After downloading the repository, you must first open and run the download_dependencies.ipynb file to download our model.

### Run the Microservice
After downloading the model, you must run the microservice on Docker using the following command on the directory that the repository is in.

    docker-compose up
    
### Quickstart (Optional)
If you want to quickly get your hands wet and test the capabilities of the microservice you can follow the quickstart.ipynb file and see how the microservice performs.

## How to run the microservice?

### Using Postman
To test with Postman:

Set the URL to http://localhost:5001/detect (or http://localhost:5001/detect/{label} if you're testing with a label).
Note: The {label} is a variable for objects like "car", "truck", "sofa" and so on.

Set the method to POST.

Add a file to the request:

Go to the "Body" tab.
Select "form-data".
Add a key named image and set the type to "File".
Upload an image file.
Send the request and check the response.

### Using Python

Here's an example Python script to test the endpoint:

    import requests
    
    URL of the Flask app
    url = 'http://localhost:5001/detect'
    
    Path to the image file
    image_path = 'path_to_your_image_file.jpg'
    
    Read the image file
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
    
    Send the POST request
    response = requests.post(url, files=files)
    
    Print the response
    print(response.json())
    
Replace path_to_your_image_file.jpg with the path to an image file on your system.
