from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)
import urllib.request

#Check if the ONNX file is already downloaded
try:
    open('src/yolov4.onnx')
except FileNotFoundError:
    # URL of the ONNX file on GitHub
    onnx_url = 'https://github.com/onnx/models/raw/main/validated/vision/object_detection_segmentation/yolov4/model/yolov4.onnx'

    # Local path to save the downloaded ONNX file
    local_path = 'src/yolov4.onnx'

    # Download the ONNX file from GitHub
    urllib.request.urlretrieve(onnx_url, local_path)

# Load the pre-trained YOLO model in ONNX format
model = cv2.dnn.readNetFromONNX('src/yolov4.onnx')

@app.route('/detect/<label>', methods=['POST'])
def detect_objects(label):
    # Get the image file from the request
    image_file = request.files['image']

    # Read the image file
    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Preprocess the image for object detection
    image = preprocess_image(image)

    # Perform object detection using the YOLO model
    detected_objects = perform_object_detection(image, label)

    # Draw bounding boxes, labels, and confidence on the image
    draw_bounding_boxes(image, detected_objects, label)

    # Convert the image to base64 encoded string
    image_base64 = convert_image_to_base64(image)

    # Prepare the detection results in JSON format
    detection_results = prepare_detection_results(image_base64, detected_objects)

    return jsonify(detection_results)

def preprocess_image(image):
    # Resize the image to the desired input size of the YOLO model
    resized_image = cv2.resize(image, (416, 416))
    # Normalize the image by scaling pixel values to the range [0, 1]
    normalized_image = resized_image / 255.0
    # Expand dimensions to match the input shape of the YOLO model
    expanded_image = np.expand_dims(normalized_image, axis=0)
    return expanded_image

def perform_object_detection(image, label):
    blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), swapRB=True, crop=False)
    model.setInput(blob)
    output_layers = model.getUnconnectedOutLayersNames()
    outputs = model.forward(output_layers)

    detected_objects = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == label:
                detected_objects.append(detection)

    return detected_objects

def draw_bounding_boxes(image, detected_objects, label):
    for detection in detected_objects:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * image.shape[1])
            center_y = int(detection[1] * image.shape[0])
            width = int(detection[2] * image.shape[1])
            height = int(detection[3] * image.shape[0])
            left = int(center_x - width / 2)
            top = int(center_y - height / 2)
            cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)
            cv2.putText(image, f'{label}: {confidence:.2f}', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def convert_image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    return image_base64

def prepare_detection_results(image_base64, detected_objects):
    detection_results = {
        'image': image_base64,
        'objects': [],
        'count': len(detected_objects)
    }
    return detection_results

if __name__ == '__main__':
    app.run()