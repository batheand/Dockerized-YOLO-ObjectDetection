# Dockerized-YOLO-ObjectDetection
Using Flask and Yolov4, this project creates a working YOLO model.

Would like to mention that it's not yet tested throughly.

## Before starting

Please run the download_model.py, which will download the onnx model, as the file is around 250 mbs it might take a while.

## Why ONNX?

ONNX acts as a translator for AI models. It allows you to train a model in any framework and then deploy it anywhere, regardless of the hardware, software, or programming language used. This simplifies deployment, reduces complexity, and improves performance.

## How it works:

The model takes requests the image, then handles all the rest in one main method and many helper methods.
