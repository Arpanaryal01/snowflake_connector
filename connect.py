import pandas as pd
import numpy as np
from snowflake.sqlalchemy import URL
from config import *


#creating cursor
curs=conn.cursor()
curs.execute("USE ROLE SYSADMIN")
sql = 'SELECT * FROM "PUBLIC"."SAMPLE_SPECS" '
curs.execute(sql)
# fetching datafrom cursors and deliver it to pandas df
df= curs.fetch_pandas_all()
print(df)
