# Use an official Python runtime as the base image
FROM python:3-alpine3.12
#Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Mount S3 bucket path containing config.py file as a volume
VOLUME /config

EXPOSE 8181
# Copy the Python script(s) into the container
#COPY app.py .

# Set the entrypoint to run your Python script
CMD ["python", "app.py"]