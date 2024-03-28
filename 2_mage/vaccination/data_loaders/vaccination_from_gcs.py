if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pyarrow as pa
import pyarrow.parquet as pq 
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/sa-vaccination-mage.json'

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    bucket_name = 'vaccination-ukraine-1'
    project_id = 'vaccination-ukraine-1'

    table_name = 'immunizations_covid19'

    root_path = f'{bucket_name}/{table_name}'

    gcs = pa.fs.GcsFileSystem()  # so here's pyarrow will automatically connect with your credentials that you set above

    arrow_df = pq.ParquetDataset(root_path, filesystem=gcs)
    df = arrow_df.read_pandas().to_pandas()
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
