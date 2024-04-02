from vanna.remote import VannaDefault
import pymysql
from sqlalchemy import create_engine
import pandas as pd

# Create a model from VannaDefault library using the API Key
vn = VannaDefault(model='srikarmodel',api_key='de57f93213764f5ba515d24c7de654c8')

# Connect vanna to the DB
conn = vn.connect_to_postgres(host='localhost', dbname='dvdrental', user='postgres', password='sriklewy42', port=5432)

# Create a function to run sql queries
def run_sql(query):
    df = pd.read_sql_query(query,conn)
    return df

# The information schema query may need some tweaking depending on your database. This is a good starting point.
df_information_schema = vn.run_sql("""SELECT * FROM information_schema.columns;""")
print(df_information_schema)

# This will break up the information schema into bite-sized chunks that can be referenced by the LLM
plan = vn.get_training_plan_generic(df_information_schema)
print(plan)
# vn.train(plan=plan)

# At any time you can inspect what training data the package is able to reference
training_data = vn.get_training_data()

vn.ask("What are the tables in dvdrental?")

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()
