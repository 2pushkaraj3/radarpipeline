import logging
import sys
import traceback

from radarpipeline import Project
from radarpipeline.common.logger import logger_init
from pyspark.sql import SparkSession

logger_init()

logger = logging.getLogger(__name__)

spark = SparkSession.builder.\
        master('local').\
        appName('foo').\
        getOrCreate()
spark.sparkContext.setLogLevel('WARN')

def run():
    """
    Pipeline entry point.
    """
    try:
        logger.info("Starting the pipeline run...")
        logger.info("Reading and Validating the configuration file...")
        project = Project(input_data="config.yaml")
        logger.info("Fetching the data...")
        project.fetch_data()
        logger.info("Computing the features...")
        project.compute_features()
        logger.info("Exporting the features data...")
        project.export_data()
        logger.info("Pipeline run completed successfully")
    except KeyboardInterrupt:
        logger.info("Pipeline run interrupted by user")
        sys.exit(0)
    except Exception:
        logger.info(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    run()
