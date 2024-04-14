# Suppressing warnings to avoid cluttering the output
import warnings
warnings.filterwarnings('ignore')
# Importing necessary libraries
import os
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import boto3
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.chat_models import BedrockChat
'''
This code block contains code for the chat model built to answer questions from FWD, and Synapxe website
'''

# Create a session with your specific AWS profile
session = boto3.Session(profile_name='myprofile')
# Path to save the FAISS vector store
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Function to initialize and configure the chat model
def demo_chat():
     # Configuration parameters for the chat model
    mistral_inference_modifier = {'max_tokens':300, 
                      "temperature":0.2,
                      "top_p":0.5,
                      "top_k":20,
                   }
     # Initializing the chat model with specified parameters
    llm = BedrockChat(credentials_profile_name="myprofile",
                          region_name="us-east-1",
                        model_id= "mistral.mistral-7b-instruct-v0:2",
                        model_kwargs=mistral_inference_modifier,
                        streaming= True
                        )
    
    return llm


# Function to fetch and process context data from a given URL
def context_db(url):
     # Loading data from the web
    loader = WebBaseLoader(url)
    data = loader.load()
    # Create embeddings using Sentence Transformers
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2',model_kwargs = {"device": "cpu"})
    # Create a FAISS vector store and save embeddings
    db = FAISS.from_documents(data, embeddings)
    db.save_local(DB_FAISS_PATH)
    return embeddings

# Function to create a prompt template for conversation   
def create_prompt_template(prompt_template):
    prompt = PromptTemplate(
        input_variables=["context","chat_history", "question"], template=prompt_template
    )
    return prompt
# Function to initialize and configure conversation memory
def demo_memory():
    llm_data = demo_chat()
    memory = ConversationBufferMemory(llm=llm_data,memory_key="chat_history",input_key="question",return_messages=True)
    memory.human_prefix = "user"
    memory.ai_prefix = "assistant"
    return memory
# Function to filter unwanted phrases from the response
def filter_response(response):
    unwanted_phrases = [
        "created by Mistral",
        # Add any other unwanted phrases here
    ]
    for phrase in unwanted_phrases:
        response = response.replace(phrase, "")
    if "User:" in response:
        response = response.split("User:", 1)[0]
    if "Reply:" in response:
        response = response.split("User:", 1)[1]
    return response

# Function to conduct a conversation chain based on input text, memory, and client type
def demo_chain(input_txt,memory,client):
    llm_data = demo_chat()
    if client == 'synapxe':
        prompt_template = """You will be acting as an HeathAI assistant named Synapxe MediGuide. Your goal is to provide answers based on the context provided. You will
    answer the question without using any
    external knowledge or assumptions. Strictly provide details only about the Synapxe. Provide source links wherever possible. 
    You should maintain a friendly customer service tone and don't say you are referring to text or document while answering.
    Here is the data you should refer to when answering the user questions: {context}
    
    Here are some important RULES for interaction:
    - Stop telling about yourself in every conversation. 
    - Don't provide chat examples as response
    - Speak about you only when asked.
    - Always stay in character, as Synapxe MediGuide
    - If you are unsure how to respond say "Sorry, I didn't understand that. Could you please provide more details?"
    - If someone asks something irrelevant, say, "Sorry, I am Synapxe MediGuide and I give assistance related to Synapxe. Is there anything I can help you with
    today?"

    Here is the conversation history (between the user and you) before answering the question. It could be empty if there is no history:
    {chat_history}
    Here are the user's questions:{question}
    assistant:"""
        url = "https://www.synapxe.sg/about-synapxe/our-role"
        
    elif client == 'fwd':
        prompt_template = """You will be acting as an insurance assistant named FWD InsureBuddy. Your goal is to provide answers based on the context provided. You will
    answer the question without using any
    external knowledge or assumptions. Strictly provide details only about the FWD Insurance. Provide source links wherever possible. 
    You should maintain a friendly customer service tone and don't say you are referring to text or document while answering.
    Here is the data you should refer to when answering the user questions: {context}
    
    Here are some important RULES for interaction:
    - Stop telling about yourself in every conversation. 
    - Speak about you only when asked.
    - Don't provide chat examples as response
    - Always stay in character, as FWD InsureBuddy
    - If you are unsure how to respond say "Sorry, I didn't understand that. Could you please provide more details?"
    - If someone asks something irrelevant, say, "Sorry, I am FWD InsureBuddy and I give assistance related to FWD Insurance. Is there anything I can help you with
    today?"

    Here is the conversation history (between the user and you) before answering the question. It could be empty if there is no history:
    {chat_history}
    Here are the user's questions:{question}
    assistant:"""
        url = ["https://www.fwd.com.sg/corporate/#about-us","https://help.fwd.com.sg/hc/en-us/articles/900007287503-How-do-I-renew-my-FWD-HDB-Fire-insurance","https://help.fwd.com.sg/hc/en-us/articles/4402396161945-How-do-I-cancel-my-policy"]

    embeddings = context_db(url)
    prompt = create_prompt_template(prompt_template)
    # Loading FAISS vector store from local storage
    db = FAISS.load_local(DB_FAISS_PATH, embeddings,allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 3})
     # Initializing conversation chain with LL model, retriever, memory, and prompt
    llm_conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm_data,
                                                                   retriever=retriever,
                                                                   verbose=True,
                                                                   memory = memory,
                                                                   chain_type = "stuff",
                                                                   combine_docs_chain_kwargs={"prompt": prompt})
    history = []
     # Running conversation chain with input text and history
    chat_reply = llm_conversation_chain.run({"question": input_txt,"chat_history": history})
     # Filtering unwanted phrases from the response
    chat_reply = filter_response(chat_reply)
    return chat_reply


