import boto3
import io
import zipfile

class RawToBronze():
    def __init__(self):
        self.bucket = "cvmearningsdata"
        self.s3 = boto3.client('s3')

    def raw_to_bronze(self, document, year):
        path = f"raw/{document}/cia_aberta/{year}.zip"

        target_files = [
            f"{document.lower()}_cia_aberta_DRE_con_{year}.csv",
            f"{document.lower()}_cia_aberta_DRE_ind_{year}.csv"]

        zip_obj = self.s3.get_object(Bucket=self.bucket, Key=path)
        zip_body = zip_obj['Body'].read()
        buffer = io.BytesIO(zip_body)

        with zipfile.ZipFile(buffer) as zip_file:
            for name in zip_file.namelist():
                if name in target_files:
                    content = zip_file.read(name)
                    new_path = f"bronze/{document}/cia_aberta/{year}/{name}"
                    self.s3.put_object(Bucket=self.bucket, Key=new_path, Body=content)
                    print(f"Uploaded: {name}")