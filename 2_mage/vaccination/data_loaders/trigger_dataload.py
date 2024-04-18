from mage_ai.orchestration.triggers.api import trigger_pipeline
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
def get_urls(*args, **kwargs):

    # url = "https://data.gov.ua/en/dataset/3fcbfe9e-7cec-4f69-b9ca-be49daae2369"

    # meta_info_links=['https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/5906aa4e-4974-486f-8477-b4749d98542e/download/immunization_legal_entities_info.csv',
    # 'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/b4d8df31-8ecc-4646-a373-95b756fde8ea/download/immunization_vaccine_codes.csv']
    links=[ 
        'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/6e88522b-ad59-48d0-9063-cf5182f325ee/download/immunizations_covid19_1qrt_2024.csv',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/37bdbd0d-88de-4a2e-ae97-c130187681db/download/immunizations_covid19_4qrt_2023.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/440ac222-cc4e-4ab9-9a7a-d1c9377a7d48/download/immunizations_covid19_3qrt_2023.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/4701f565-9893-45d8-a151-1ba2d54e7eeb/download/immunizations_covid19_2qrt_2023.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/e2005fe5-4d4a-407c-9233-b5abe874bda1/download/immunizations_covid19_1qrt_2023.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/5ad3b149-6990-49f2-aad9-14773e484f24/download/immunizations_covid19_4qrt_2022.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/120d4e8d-19fa-4a93-81c1-bc15d73dfb9c/download/immunization_covid19_3qrt_2022.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/2d0b4e83-5a60-4930-8e30-9caa1b261d4c/download/immunization_covid19_2qrt_2022.zip',  #all links up to tihs download weel but after it require more RAM, or advancet load techniques sush as pyspark. or dask.  
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/bee0006e-3be0-40bb-91c8-68a921fc2108/download/immunization_covid19_1qrt_2022.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/7adbccd2-278e-4781-b783-9027b9776ee1/download/immunization_covid19_4qrt_2021.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/df551667-8d41-44e2-8ab7-cabeb15c942b/download/immunization_covid19_3qrt_2021.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/6eaade41-ce97-4a8b-929d-034e8b21e82d/download/immunization_covid19_2qrt_2021.zip',
            'https://data.gov.ua/dataset/4cced549-1a03-4e0b-afbb-461febb26007/resource/85286f5b-2b23-4871-899e-f2a5b33b2471/download/immunization_covid19_1qrt_2021.zip',
            ]
    print(links)

    return links



@data_loader
def trigger(*args, **kwargs):
    """
    Trigger another pipeline to run.

    Documentation: https://docs.mage.ai/orchestration/triggers/trigger-pipeline
    """
    urls = get_urls()
    for url in urls:
        print(f"STARTED FOR {url.split()[-1]}")
        trigger_pipeline(
            'vaccination_ukraine',        # Required: enter the UUID of the pipeline to trigger
            variables={'url': url}, # Optional: runtime variables for the pipeline
            check_status=True,     # Optional: poll and check the status of the triggered pipeline
            error_on_failure=False, # Optional: if triggered pipeline fails, raise an exception
            poll_interval=60,       # Optional: check the status of triggered pipeline every N seconds
            poll_timeout=None,      # Optional: raise an exception after N seconds
            verbose=True,           # Optional: print status of triggered pipeline run
        )
        print(f"FINISHED FOR {url.split()[-1]}")
