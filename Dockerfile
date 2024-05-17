# Use the official Python image as a parent image
FROM python:3.8-slim

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    wget \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the ONNX model file into the Docker image
COPY src/yolov4.onnx /app/src/yolov4.onnx

# Expose the port the app runs on
EXPOSE 5000

# Set the entry point to run the application
CMD ["python", "main.py"]
