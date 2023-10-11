from outbound import Logger
from collections import defaultdict
import pandas as pd
status_dict = defaultdict(lambda: 0)
try:
    logger = Logger(spark, STDOUT_LEVEL="DEBUG")
except Exception as e:
    dbutils.notebook.exit(f"Failure, Error occured while creating Logger Instance.\n{e}")