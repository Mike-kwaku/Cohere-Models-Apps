# Cohere-RAG-Chatbot

This repository contains the following AI applications built with Cohere [command](https://cohere.com/command?_gl=1*1bccwue*_gcl_au*MTI0ODM1NjY2OS4xNzIwNjIxMjc1*_ga*NDg5MDI2MzAuMTcyMDYyMTI4MQ..*_ga_CRGS116RZS*MTcyMjU4MDUwNi40Ny4wLjE3MjI1ODA1MDYuNjAuMC4w), and [embed](https://cohere.com/embed?_gl=1*5gvy8z*_gcl_au*MTI0ODM1NjY2OS4xNzIwNjIxMjc1*_ga*NDg5MDI2MzAuMTcyMDYyMTI4MQ..*_ga_CRGS116RZS*MTcyMjU4MDYxMi40Ny4wLjE3MjI1ODA2MTIuNjAuMC4w) models.   

[HealthCare Assistant]()

[Q/A Bot]() 

[Semantic Search]() 











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
