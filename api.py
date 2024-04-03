import boto3
import os
# from gevent.pywsgi import WSGIServer

from flask import Flask, jsonify, request

app = Flask(__name__)

# AWS credentials
# AWS_ACCESS_KEY_ID = 'AKIAZSKBNQEVBJS23GFC'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_REGION_NAME = 'ap-northeast-1'

# # S3 bucket details
# S3_BUCKET_NAME = 'bucketlakehouse'
# IMAGES_FOLDER = 'output_images'

# @app.route('/get_image_urls', methods=['GET'])
# def get_image_urls():
#     try:
#         s3_client = boto3.client('s3', 
#                                  aws_access_key_id=AWS_ACCESS_KEY_ID, 
#                                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
#                                  region_name=AWS_REGION_NAME)

#         response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=IMAGES_FOLDER)

#         image_urls = []

#         for obj in response.get('Contents', []):
#             image_key = obj['Key']

#             image_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{image_key}"

#             image_urls.append(image_url)

#         return jsonify({'image_urls': image_urls}), 200

#     except Exception as e:
        # return jsonify({'error': str(e)}), 500
 
@app.route('/alo', methods=['GET'])
def getAlo():
    return jsonify({'alo': 'alo'}), 200

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 33507))  # Get the port from environment variables, default to 5000 if not specified
    # app.run(debug=True, port=port)
    app.run(debug=True)
    


