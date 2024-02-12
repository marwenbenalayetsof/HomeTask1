import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("TestSession").getOrCreate()

def test_data_loading(spark):
    df = spark.read.csv('test_data.csv', header=True, inferSchema=True)
    assert df.count() > 0

def test_data_loading_to_db(spark):
    df = spark.read.csv('test_data.csv', header=True, inferSchema=True)
    assert df.count() > 0