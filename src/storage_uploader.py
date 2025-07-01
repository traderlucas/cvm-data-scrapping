import boto3
import io

class StorageUploader():
    def __init__(self):
        self.client = boto3.client('s3')

    def save_to_s3(self, data, bucket, path):
        data = io.BytesIO(data)
        self.client.upload_fileobj(data, bucket, path)
        return 