import io
import pandas as pd
import numpy as np
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from pandas.errors import ParserError
import dask.dataframe as dd



@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    download_url=kwargs.get('url')

    print(f'donwloading data from {download_url[-34:]}')
    # sofe files are zipped , some not.
    if 'zip' in download_url:
        compression='zip'
    else:
        compression='infer'


    # hardcoded because the data source has randomly different separator.
    if '_4qrt_2021' in download_url:
        sep=','

    elif '2021' in download_url or '1qrt_2022' in download_url:
        sep=';'
    else:
         sep=','

    if '2021' in download_url:
        division_identifier_value =  'division_id' 
    else:
         division_identifier_value='division_identifier_value'

    print(division_identifier_value, sep)
    data_dtypes=    {
        'temp_immunization_id': str,
        'legal_entity_id': str,
        division_identifier_value: str,
        'status': str,
        'not_given': str,     # sometimes not_given is nan and we cant apply bool dtype
        'vaccine_code': str,
        'patient_age_group': str,
        'patient_gender': str,
        'manufacturer': str,
        'lot_number': str,
        'dose_quantity_unit': str,
        'dose_quantity_value': 'float32',
        'vaccination_protocol_dose_sequence': np.int64,
        'vaccination_protocol_series': str,
        'vaccination_protocol_series_doses': np.int64,
        'vaccination_protocol_target_diseases': str

        }


    usecols=['temp_immunization_id', 'legal_entity_id', \
    division_identifier_value,'status', 'not_given', 'vaccine_code', 'patient_age_group', 'patient_gender',  \
    'manufacturer','lot_number', 'dose_quantity_unit', 'dose_quantity_value', \
    'vaccination_protocol_series', 'updated_at']

    parse_dates=['updated_at']

    # download data using chunking because otherwise, memory error. Try lower chunk_size if fails
    chunk_size = 1000000 # Set the chunk size to 1 million rows
    chunks = []
    for chunk in pd.read_csv(download_url, sep=sep, header=0,  on_bad_lines='warn', usecols=usecols, chunksize=chunk_size):
        print('read chunk')
        chunk=chunk.loc[ (chunk['status']=='Запис коректний') & (chunk['not_given'].str.lower().str[0]=='f') ]
        chunk.dropna(inplace=True)

        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)
    
    print(df.columns)
    print(df.isna().sum())
    print(df.info())


    if  "division_id" in list(df.columns):
        df.rename(columns={"division_id": "division_identifier_value"}, inplace=True)
    print(df.info())
    print(list(df.columns))
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'



@test
def test_output_columns(output, *args) -> None:


    assert set(list(output.columns)) == set(['temp_immunization_id', 'legal_entity_id',
    'division_identifier_value','status', 'not_given', 'vaccine_code', 'immunization_date','patient_age_group', 'patient_gender', 
    'manufacturer', 'lot_number','expiration_date', 'dose_quantity_unit', 'dose_quantity_value', 'vaccination_protocol_sequence'
    'vaccination_protocol_series', 'inserted_at', 'updated_at']), f"The columns dont match {output.columns}"
