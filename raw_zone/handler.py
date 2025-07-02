from .storage_uploader import StorageUploader

class EarningsExtractLoad():
    def __init__(self, bucket):
        self.uploader = StorageUploader()
        self.bucket = bucket

    def extract_load(self, request):
        data = request.get_cvm_data()
        document = request.get_document_type()
        year = request.year

        path = f"raw/{document}/cia_aberta/{year}.zip"

        self.uploader.save_to_s3(data, self.bucket, path)
