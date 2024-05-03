import urllib.request
import urllib.error

#Check if the ONNX file is already downloaded
try:
    open('src/yolov4.onnx')
except FileNotFoundError:
    try:
        # URL of the ONNX file on GitHub
        onnx_url = 'https://github.com/onnx/models/raw/main/validated/vision/object_detection_segmentation/yolov4/model/yolov4.onnx'

        # Local path to save the downloaded ONNX file
        local_path = 'src/yolov4.onnx'

        # Download the ONNX file from GitHub
        urllib.request.urlretrieve(onnx_url, local_path)
        print("Download succesful")
    except urllib.error.URLError as e:
        print(f"Error occurred while downloading the file: {e}")

