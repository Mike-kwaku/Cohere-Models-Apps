import pandas as pd
import s3fs
df = pd.read_json("books.csv", orient="records", lines=True)
df  = pd.read_json('spaceCompanies.json')

import cohere  
co_client = cohere.Client(cohere_api_key, client_name='mongodb')
# create a dataset in Cohere Platform
dataset = co_client.create_dataset(name='companies',
                                   data=open('spaceCompanies','r'),
                                   keep_fields=["overview","title","year"],
                                   dataset_type="embed-input").wait()


ds=co.datasets.create(name='space', data=open('spaceCompanies.json', 'rb'), keep_fields=['companyName','phone','companyLocation'], dataset_type="embed-input").wait()


my_dataset = co.datasets.create(
	name="space",
	data=open("spaceCompanies.json", "rb"),
	dataset_type="prompt-completion-finetune-input")





import cohere 
import pandas as pd 
cohere_api_key = os.environ["COHERE_API_KEY"]
MONGO_CONN_STR = os.environ["MONGODB_CONNECTION_STR"]
co_client = cohere.Client(cohere_api_key, client_name='mongodb')
dataset = co_client.datasets_create(name='companies',
                                   data=open('spaceCompanies','r'), 
                                   dataset_type="embed-input").wait()

dataset.wait()
dataset

dataset.wait()
# Schedule an Embedding job to run on the entire movies dataset
embed_job = co_client.create_embed_job(dataset_id=dataset.id, 
    input_type='search_document',
    model='embed-english-v3.0', 
    truncate='END')
embed_job.wait()
output_dataset = co_client.get_dataset(embed_job.output.id)
results = list(map(lambda x:{"text":x["text"], "embedding": x["embeddings"]["float"]},output_dataset))
len(results)













co = cohere.Client(api_key='FMGmtPHuF5DeewG7oUANfBGisUlhtlBMIhdRq8R5')



import pandas as pd
import s3fs
df = pd.read_json("s3://ashwin-partner-bucket/cohere/movies_sample_dataset.jsonl", orient="records", lines=True)
df.to_json('spaceCompanies', orient="records", lines=True)
df[:3]

df[:3]

df = pandas.read_csv(books.csv, sep='delimiter', header=None)
df = pd.read_csv('books.csv', encoding='ISO-8859-1')

data = pd.read_csv('books.csv', skiprows=2)
df = pd.read_csv('books.csv', engine='python')

df = pd.read_csv("books.csv",encoding='utf-16')
