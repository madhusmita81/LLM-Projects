import openai
from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

client= OpenAI()
file= client.files.create(file=open("E:/LLM_Project/openai_examples/data/fine-tune-data.jsonl", "rb"),  purpose="fine-tune")
print(file.id)

fine_tuned_model1= client.fine_tuning.jobs.create(training_file=file.id,
model="gpt-3.5-turbo",hyperparameters={"n_epochs": 9, } 
)

def upload_file(path: str):
    file= client.files.create(file=open(path, "rb"),  purpose="fine-tune")
    return file.id

def retrive_finetune_model(fid):
    fine_tuning_job= client.fine_tuning.jobs.create(training_file=file.id,model="gpt-3.5-turbo",hyperparameters={"n_epochs": 9, } )
    print(fine_tuning_job.id)
    while True:
        fine_tuning_model= client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
        if fine_tuning_model.status == "succeeded":
            fine_tuned_model_id= fine_tuning_model.fine_tuned_model
            break
        sleep(30)
    return fine_tuned_model_id

def get_finetunedmodel():
    path= "data/fine-tune-data.jsonl"
    fid= upload_file(path)
    model= retrive_finetune_model(fid)
    return model