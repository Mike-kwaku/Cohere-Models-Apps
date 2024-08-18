# Cohere-Models-Apps

![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTojaKMXPTm8FhVKO4YmC-BwNXovBJJZ7x0FVwQcw5auO5QX7t-LZvxxuTFuMibZv75KzU&usqp=CAU)

This repository contains the following AI applications built with Cohere [command](https://cohere.com/command?_gl=1*1bccwue*_gcl_au*MTI0ODM1NjY2OS4xNzIwNjIxMjc1*_ga*NDg5MDI2MzAuMTcyMDYyMTI4MQ..*_ga_CRGS116RZS*MTcyMjU4MDUwNi40Ny4wLjE3MjI1ODA1MDYuNjAuMC4w), and [embed](https://cohere.com/embed?_gl=1*5gvy8z*_gcl_au*MTI0ODM1NjY2OS4xNzIwNjIxMjc1*_ga*NDg5MDI2MzAuMTcyMDYyMTI4MQ..*_ga_CRGS116RZS*MTcyMjU4MDYxMi40Ny4wLjE3MjI1ODA2MTIuNjAuMC4w) models.   

## Application built with Cohere **Command** and **Embed** Models.   


[HealthCare Assistant]() :  This app responds to healthcare queries from users with relevants answers. 

[Q/A Bot]() : This app provides answers to generic questions from users. 

[Semantic Search]() : This app demonstrates how to improve search accuracy - semantically - with Cohere embed using Mondb vector search operator.  


## How It Works 



### Q/A Bot 
![](qa2.gif)


### HealthCare Assistant  

----------------------------------------------------------------------------------
export LANGCHAIN_API_KEY=""


import getpass
import os
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain_core.chat_history import (BaseChatMessageHistory, InMemoryChatMessageHistory)
from langchain_core.runnables.history import RunnableWithMessageHistory

model = ChatCohere(model="command-r-plus")

prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful assistant. Answer all questions to the best of your ability.")])


config = {"configurable": {"session_id": "abc2"}}














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

FMGmtPHuF5DeewG7oUANfBGisUlhtlBMIhdRq8R5


import cohere

co = cohere.Client('FMGmtPHuF5DeewG7oUANfBGisUlhtlBMIhdRq8R5')

# start an embed job
response = co.embed_jobs.create(
    dataset_id='try-0ghs2p',
    name='try',
    input_type="search_document", 
    model="embed-english-v3.0"
)

# poll the server until the job is complete
response = co.wait(job)

print(response)

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
