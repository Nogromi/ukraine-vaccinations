if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


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

    data=data.loc[ (data['status']=='Запис коректний') & (data['not_given']==False) ]

    # remove columns
    data = data.drop(columns=['status',
                            'not_given',
                            'expiration_date',
                            'vaccination_protocol_dose_sequence',
                            'vaccination_protocol_series_doses',
                            'vaccination_protocol_target_diseases',
                            'inserted_at', 
                            'immunization_date'])
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    print(output.isna().sum())
    print(output.shape)
    print(output.info())
    assert output is not None, 'The output is undefined'
