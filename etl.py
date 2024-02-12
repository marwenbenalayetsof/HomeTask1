from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName('DataEngineerTask')\
    .config("spark.jars", "utils/sqlite-jdbc-3.45.1.0.jar")\
    .getOrCreate()
log4jLogger = spark._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)

logger.info("PySpark job has started.")

# Extract
df = spark.read.csv('WorldEnergyConsumption.csv', header=True, inferSchema=True)

# Load
df.write \
    .format('jdbc') \
    .option('url', 'jdbc:sqlite:my_database.db') \
    .option('dbtable', 'my_table') \
    .option('driver', 'org.sqlite.JDBC') \
    .mode('overwrite') \
    .save()
