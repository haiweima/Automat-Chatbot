# Automat-Chatbot
---------------------------------------------
Our app is now running on AWS(35.175.123.183:8084)

These are the details:
1. The app.py and requirements.txt runs on an EC2 instance.
2. The required vanna code resides in the app.py file and all the libraries, dependencies are in the requirements.txt file.
3. The dummy(northwind) DB is hosted on a cloud AWS serverless DB on the backend on it's own.
4. The app.py uses the DB credentials to connect to it and train the model.
5. We use the VannaFlaskApp() in-built function to run the app on the VM port 8084.

EC2 VM details:
1. Public IP Address: 35.175.123.183
2. App access with the port: 35.175.123.183:8084

Postgres DB connection credentials:
1. hostname: tenth-snake-14405.7tt.aws-us-east-1.cockroachlabs.cloud
2. dbname: northwind_db
3. username: srikarreddy651
4. password: jTmnTbYPzv-v-zU1rWUmUQ
5. port: 26257
