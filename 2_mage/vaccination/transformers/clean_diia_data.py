if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    # data=data.loc[ (data['status']=='Запис коректний') & (data['not_given'].str.lower().str[0]=='f') ]

    # remove columns 
    # sometimes not_given is nan and we cant apply bool dtype
    # data = data.drop(columns=['status', 'not_given'])
    print('start clean')
    data.dropna(inplace=True)
    # data = data.drop(columns=['status',
    #                         'not_given',
    #                         'expiration_date',
    #                         'vaccination_protocol_dose_sequence',
    #                         'vaccination_protocol_series_doses',
    #                         'vaccination_protocol_target_diseases',
    #                         'inserted_at', 
    #                         'immunization_date'])
        #         chunk['updated_at'] = pd.to_datetime(chunk['updated_at'])
    data['updated_at'] = pd.to_datetime(data['updated_at'])


    print(data.info())
    print(f"date range: {data['updated_at'].min(), data['updated_at'].max()}")
    print(data.columns)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    print(output.isna().sum())
    assert output is not None, 'The output is undefined'


@test
def test_output_na(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert sum(output.isna().sum()) == 0


@test
def test_output_columns(output, *args) -> None:
    assert list(output.columns) == ['temp_immunization_id', 'legal_entity_id', 'division_identifier_value', \
       'vaccine_code', 'patient_age_group', 'patient_gender', 'manufacturer', \
       'lot_number', 'dose_quantity_unit', 'dose_quantity_value', \
       'vaccination_protocol_series', 'updated_at']


# @test
# def test_date_range(output, *args) -> None:
#     ...

    
