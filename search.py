import cohere
import streamlit as st 
import os
from pymongo import MongoClient

co = cohere.Client(os.environ["COHERE_API_KEY"])
MONGO_CONN_STR = os.environ["MONGODB_CONNECTION_STR"]
mongo_client = MongoClient(MONGO_CONN_STR)

def query_vector_search(q, prefilter = {}, postfilter = {},path="embedding",topK=2):
    ele = co_client.embed(model="embed-english-v3.0",input_type="search_document",texts=[q])
    query_embedding = ele.embeddings[0]
    vs_query = {
                "index": "default",
                "path": path,
                "queryVector": query_embedding,
                "numCandidates": 10,
                "limit": topK,
            }
    if len(prefilter)>0:
        vs_query["filter"] = prefilter
    new_search_query = {"$vectorSearch": vs_query}
    project = {"$project": {"score": {"$meta": "vectorSearchScore"},"_id": 0,"title": 1, "release_date": 1, "overview": 1,"year": 1}}
    if len(postfilter.keys())>0:
        postFilter = {"$match":postfilter}
        res = list(output_collection.aggregate([new_search_query, project, postFilter]))
    else:
        res = list(output_collection.aggregate([new_search_query, project]))
    return res
































