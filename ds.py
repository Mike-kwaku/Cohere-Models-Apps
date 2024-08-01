import os 
import streamlit as st 
import cohere
import pymongo 

cohere_model='embed'

try:   

#  specify your cohere API key and define cohere model to use.  
   co = cohere.Client(os.environ["COHERE_API_KEY"])
  
except KeyError:  
   cohere_api_key = getpass.getpass("Please enter your COHERE API KEY (hit enter)

# MongoDB connection string
try:
    MONGO_CONN_STR = os.environ["MONGODB_CONNECTION_STR"]
except KeyError:
    MONGO_CONN = getpass.getpass("Please enter your MongoDB Atlas Connection String (hit enter): ")                                    



