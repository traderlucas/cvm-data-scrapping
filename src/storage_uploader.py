import boto3

class storageUploader():
    def __init__(self, data, bucket, path):
        self.client = boto3.client('s3')
        self.data = data
        self.bucket = bucket
        self.path = path