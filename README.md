# Cohere-RAG-Chatbot

[HealthCare Assistant]()

[Q/A Bot]() 

[Elasticsearch Health Checker]() 


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
