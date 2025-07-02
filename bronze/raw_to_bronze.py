import boto3
import io
import zipfile

class RawToBronze():
    def __init__(self):
        self.bucket = "cvmearningsdata"
        self.s3 = boto3.client('S3')

    def raw_to_bronze(self, document, year):
        path = f"raw/{document}/cia_aberta/{year}.zip"

        zip_obj = self.s3.get_object(Bucket=self.bucket, key=path)
        buffer = io.BytesIO(zip_obj['Body']).read()

        with zipfile.ZipFile(buffer) as z:
            for file in z.namelist():
                file  = z.read(file)
                new_path = "raw/{document}/cia_aberta/{year}/{name}"
                self.s3.put_object(Bucket=self.bucket, Key=new_path, Body=file)