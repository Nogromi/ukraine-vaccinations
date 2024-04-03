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
    data_dtypes=    {
        'legal_entity_id': str,           
        'legal_entity_name': str,         
        'legal_entity_edrpou':str,       
        'care_type': str,                 
        'property_type': str,             
        'legal_entity_email': str,        
        'legal_entity_phone': str,        
        'legal_entity_owner_name': str,   
        'registration_area': str,   
        'registration_settlement': str,
        'registration_address': str,
        'lat': float,
        'lng': float
        }

    legal_entities_url='https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/5906aa4e-4974-486f-8477-b4749d98542e/download/immunization_legal_entities_info.csv'
    legal_entities_df = pd.read_csv(legal_entities_url, header=0, sep=',', quotechar='"', dtype=data_dtypes)
    print(legal_entities_df.isna().sum())
    legal_entities_df= legal_entities_df.fillna(0)
    return legal_entities_df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert  sum(output.isna().sum()) == 0, 'there are null values'
