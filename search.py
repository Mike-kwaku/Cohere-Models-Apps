import cohere
import streamlit as st 
import os
from pymongo import MongoClient

co = cohere.Client(os.environ["COHERE_API_KEY"])
MONGO_CONN_STR = os.environ["MONGODB_CONNECTION_STR"]
mongo_client = MongoClient(MONGO_CONN_STR)
output_collection = mongo_client

def qvs(q, prefilter = {}, postfilter = {},path="embedding",topK=2):
    ele = co.embed(model="embed-english-v3.0",input_type="search_document",texts=[q])
    query_embedding = ele.embeddings[0]
    vs_query = {
                "index": "default",
                "path": path,
                "queryVector": query_embedding,
                "numCandidates": 10,
                "limit": topK,
            }
    project = {"$project": {"score": {"$meta": "searchScore"},"_id": 0,"title": 1, "release-date": 1, "overview": 1}
    docs = list(output_collection.aggregate([vs_query, project, {"$limit":topK}]))
    
    return vs_query

form = st.form("my form")   
with form:   
  
    
 st.write("Enter your search query here: [Example: romantic comedy movies ] ")

 vq_input = st.text_input("semantic search", key = "vq_input")
 generate_button = form.form_submit_button("Answer Query")

 if generate_button:
    if vq_input == "":
      st.error("Search field cannot be blank")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Query Response:")

      for i in range(1):
          st.markdown("""---""")
          ans = qvs(vq_input)
          st.markdown("##### " + ans)
          st.write(ans)
          my_bar.progress((i+1)/1)  






























