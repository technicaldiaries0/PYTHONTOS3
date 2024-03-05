from flask import Flask, render_template, request, jsonify
import boto3
import os
import config

app = Flask(__name__)

AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_REGION = config.AWS_REGION
S3_BUCKET_NAME = config.S3_BUCKET_NAME

#login(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY, config.AWS_REGION, config.S3_BUCKET_NAME)


# Configure AWS S3 client
s3_client = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_REGION)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Upload image to S3
    s3_client.upload_fileobj(file, S3_BUCKET_NAME, file.filename)
    
    # Generate S3 URL
    s3_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file.filename}"
    
    return jsonify({'link': s3_url})

if __name__ == '__main__':
    app.run(port=8181)
