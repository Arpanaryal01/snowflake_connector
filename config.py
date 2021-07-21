import snowflake.connector
from sqlalchemy import create_engine
#creating connection
from os import environ, path
from dotenv import load_dotenv



basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

conn= snowflake.connector.connect(
    user = environ.get("user"),
    password = environ.get("password"),
    account = environ.get("account"),
    warehouse = environ.get("warehouse"),
    database = environ.get("database"),
    schema = environ.get("schema")

)


# #connection string
# engine = create_engine(URL(
#     account = 'jxa24839',
#     user = 'arpan',
#     password = 'aaAA73014@_!',
#     database = 'MRI_SIMMONS_DB1',
#     schema = 'PUBLIC',
#     warehouse = 'COMPUTE_WH',
#     role='SYSADMIN',
# ))

# connection = engine.connect()

# query =  'select * from "PUBLIC"."CLARITAS" '
# data = pd.read_sql(query, connection)
# print(data)

# --------------------------OR----------------#
