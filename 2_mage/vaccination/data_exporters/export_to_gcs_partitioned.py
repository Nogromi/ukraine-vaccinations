from os import path
import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

    
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/sa-vaccination-mage.json'
project_id = 'vaccination-ukraine-1'
bucket_name = 'vaccination-ukraine-1'


@data_exporter
def export_data(df, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
        # df['tpep_pickup_date'] = df['tpep_pickup_datetime'].dt.date

    df['date'] = df['updated_at'].dt.date
    df.drop(columns=['updated_at'], inplace=True)
    # download_url=kwargs.get('url')
    # table_name = os.path.basename(download_url).replace('.zip', '')
    table_name = 'vaccination'
    root_path = f'{bucket_name}/{table_name}'
    table = pa.Table.from_pandas(df)
    print("table.schema", table.schema.to_string())

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['date'],
        filesystem=gcs
    )



