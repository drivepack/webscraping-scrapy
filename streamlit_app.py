import streamlit as st
from pymongo import MongoClient
import pandas as pd
import urllib.parse  

# Set up MongoDB connection
username = urllib.parse.quote_plus('temidayodeveloper')
password = urllib.parse.quote_plus('temidayodeveloper')
client = MongoClient(f'mongodb+srv://{username}:{password}@cluster0.mongodb.net/?retryWrites=true&w=majority')

# Select the database and collection
db = client['Cluster0']
collection = db['google_shopping']

# Fetch some data from the collection
cursor = collection.find({})  # Fetch all documents

# Convert the cursor into a list
mongo_docs = list(cursor)

# Convert the list of MongoDB documents into a DataFrame
df = pd.DataFrame(mongo_docs)

# Display the DataFrame in Streamlit
st.dataframe(df)

