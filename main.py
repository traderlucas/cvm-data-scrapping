import logging

from src.cvm_requests import CvmRequestListedCompanies
from src.cvm_file_reader import CvmFileReaderDre
from src.cvm_file_transformer import CvmFileTransformerDre

def main():

    cvm_request = CvmRequestListedCompanies(year=2024, is_annual=False)
    cvm_reader = CvmFileReaderDre(cvm_request)

    column_mapping = {
    'CNPJ_CIA': 'tx_cnpj',               
    'DT_REFER': 'dt_reference_date',     
    'DENOM_CIA': 'tx_company_name',      
    'CD_CVM': 'cd_cvm_code',             
    'GRUPO_DFP': 'tx_type',              
    'CD_CONTA': 'cd_record_code',        
    'DS_CONTA': 'tx_description',        
    'VL_CONTA': 'nb_reference_value',    
    'ST_CONTA_FIXA': 'fl_fixed_record'   
    }

    keep_columns = ['dt_reference_date', 'tx_cnpj', 'tx_company_name', 'cd_cvm_code', 'tx_type',
                'cd_record_code', 'tx_description', 'nb_reference_value', 'fl_fixed_record']
    
    cvm_transformer = CvmFileTransformerDre(column_mapping=column_mapping, keep_columns=keep_columns)

    try:

        df = cvm_transformer.rename_cvm_file_columns(cvm_reader.exctract_cvm_files(cvm_request))

        logging.info("Data extracted successfully:")              
        print(df.head())

    except Exception as e:
        logging.error(f"Error while extracting data: {e}")


if __name__ == "__main__":
    main()