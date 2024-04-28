import vanna
from dotenv import load_dotenv
load_dotenv()

from functools import wraps
from flask import Flask, jsonify, Response, request, redirect, url_for
import flask
import os
# from cache import MemoryCache

from vanna.remote import VannaDefault
import pandas as pd

# SETUP
# Create a model from VannaDefault library using the API Key
my_mod = VannaDefault('my_dummy_model',api_key="015653fc39e04345a35ef027394c6034")

# Connect vanna to the DB
conn = my_mod.connect_to_postgres(host="tenth-snake-14405.7tt.aws-us-east-1.cockroachlabs.cloud", dbname="northwind_db", user="srikarreddy651", password="jTmnTbYPzv-v-zU1rWUmUQ", port="26257")

# Create a function to run sql queries
def run_sql(query):
    df = pd.read_sql_query(query,conn)
    return df

# The information schema query may need some tweaking depending on your database. This is a good starting point.
df_information_schema = my_mod.run_sql("""SELECT * FROM information_schema.columns;""")
# print(df_information_schema)

# This will break up the information schema into bite-sized chunks that can be referenced by the LLM
plan = my_mod.get_training_plan_generic(df_information_schema)
my_mod.train(plan=plan)

# Deploy the trained model on localhost
from vanna.flask import VannaFlaskApp
VannaFlaskApp(my_mod).run()
