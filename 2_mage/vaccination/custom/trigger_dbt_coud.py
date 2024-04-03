if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import requests
import os
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('/home/src/.env')
load_dotenv(dotenv_path=dotenv_path)
@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here


    url = "https://cloud.getdbt.com/api/v2/accounts/255136/jobs/564018/run/"
    vaccination_mage = os.getenv('vaccination_mage')

    headers = {
        "Authorization": f"Token {vaccination_mage}",
        "Content-Type": "application/json"
    }
    body = {
        "cause": "Triggered via API"
    }

    response = requests.post(url, headers=headers, json=body)

    print(response.json())
    return {response.status_code}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
