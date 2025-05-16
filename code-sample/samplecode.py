#Create a service client by name using the default session.
import json
import os
import sys

import boto3
from langchain_aws import BedrockLLM
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


module_path = ".."
sys.path.append(os.path.abspath(module_path))
bedrock_client = boto3.client('bedrock-runtime',region_name=os.environ.get("AWS_DEFAULT_REGION", None))

# model configuration
modelId = "meta.llama3-8b-instruct-v1:0"
llm = BedrockLLM(
    model_id=modelId,
    model_kwargs={
        "max_gen_len": 2048,
        "temperature": 0,
        "top_p": 1
    },
    client=bedrock_client
)

#get tokens
shareholder_letter = "letter.txt"

with open(shareholder_letter, "r", encoding="utf-8") as file:
    letter = file.read()
    
llm.get_num_tokens(letter)


#chunking
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=100
)

docs = text_splitter.create_documents([letter])

# Set verbose=True if you want to see the prompts being used
summary_chain = load_summarize_chain(llm=llm, chain_type="map_reduce", verbose=False)


#invoke chain
output = ""
try:
    
    output = summary_chain.invoke(docs)

except ValueError as error:
    if  "AccessDeniedException" in str(error):
        print(f"\x1b[41m{error}\
        \nTo troubeshoot this issue please refer to the following resources.\
         \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
         \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")      
        class StopExecution(ValueError):
            def _render_traceback_(self):
                pass
        raise StopExecution        
    else:
        raise error

# print output
print(output['output_text'])
