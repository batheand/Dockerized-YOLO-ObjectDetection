# Base Image
FROM python:3.8-slim  

# Working Directory
WORKDIR /app

# Install Dependencies
COPY requirements.txt ./ 
RUN pip install -r requirements.txt 

# Copy Code to Image
COPY . ./  

# Expose the port on which Flask runs
EXPOSE 5000  

# Command to Run the Application
CMD ["python", "main.py"]  # Assuming your main Flask file is named app.py
