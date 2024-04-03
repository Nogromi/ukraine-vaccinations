import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = ''
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    download_url=kwargs.get('url')
    data_dtypes=    {
        'temp_immunization_id': str,
        'legal_entity_id': str,
        'division_identifier_value': str,
        'status': str,
        'not_given': bool,
        'vaccine_code': str,
        'patient_age_group': str,
        'patient_gender': str,
        'manufacturer': str,
        'lot_number': str,
        'dose_quantity_unit': str,
        'dose_quantity_value': float,
        'vaccination_protocol_dose_sequence': pd.Int64Dtype(),
        'vaccination_protocol_series': str,
        'vaccination_protocol_series_doses': pd.Int64Dtype(),
        'vaccination_protocol_target_diseases': str
        }
    parse_dates=['immunization_date','expiration_date','inserted_at','updated_at']
    df = pd.read_csv(download_url, compression='zip', header=0, sep=',', quotechar='"', dtype=data_dtypes , parse_dates=parse_dates)
    # df = pd.read_csv(download_url, compression='zip', header=0, sep=',', quotechar='"')
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
