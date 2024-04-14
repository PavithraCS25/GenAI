# Importing necessary libraries
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from langchain_community.vectorstores import FAISS
import os
import json
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PIL.Image
import base64

'''
This code written to get inference from Image using Gemini model and to answer questions based on the image using question answering chain.
'''

# Setting content type for image processing
content_type = "image/jpeg"
# Path to save the FAISS vector store
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Function to process image and generate JSON output
def process_image(images):
    for image in images:
        # To read file as bytes:
        image = PIL.Image.open(image)
        result_json = generate_df(image)
    return result_json

# Function to generate detailed JSON output from an image part
def generate_df(part):
    # Initializing GenerativeAI model for image processing
  model = genai.GenerativeModel("gemini-pro-vision")
    # Generating content based on image part and instructions
  responses = model.generate_content(
    [part, """Extract the below details from video and give me result in JSON format. 
    
    Instruction:
    Create a JSON with proper format. avoid using characters which will result in malformed JSON.
    
    Verify the JSON format and then provide the output. Strictly Do not use Markdowns.
    
    Example:
'{
  \"color_tone\": \"The dominant color tone of the image.\",
  \"branding\": \"Is branding present in the image? (\'yes\' or \'no\').\",
  \"logo\": \"is logo is visiblepresent in the image? (\'yes\' or \'no\').\",
  \"logo_position\": \"The average position of the logo within the image.\",
  \"text\": \"is text present present in the image? (\'yes\' or \'no\').\",
  \"text_position\": \"The average position of text within the image.\",
  \"objects\": \"A list of key objects identified.\",
  \"product\": \"A list of key products, such as servers or storage devices, featured in the image.\",
  \"Face\": \"Is face of human visible in the image? (\'Yes\' or \'No\').\",
  \"Human present\": \"Is a person or human being present in the image? (\'Yes\' or \'No\').\",
  \"animal present\": \"Are animals image? (\'Yes\' or \'No\').\",
  \"event\": \"are there any events depicted in the image? (\'Yes\' or \'No\').\",
  \"fictional character\": \"Is fictional characters present in the image? (\'Yes\' or \'No\').\",
  \"text lines\": \"The number of text lines featured throughout the image.\",
  \"web link\": \"Is web link displayed in the image? (\'Yes\' or \'No\').\",
  \"currency\": \"Is currency displayed in the image? (\'Yes\' or \'No\').\",
  \"context\": \"A summary describing the activities or storyline depicted in the video.\"
  }'"""],
    generation_config={
        "max_output_tokens": 1000,
        "temperature": 0.2,
        "top_p": 1,
        "top_k": 32
    },
    safety_settings={
          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    stream=False,
  )
  return responses.text

# Function to get the conversational chain for answering questions
def get_conversational_chain():
    # Prompt template for answering questions
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    # Initializing GenerativeAI chat model
    model = ChatGoogleGenerativeAI(model="gemini-pro",
                               temperature=0.1,
                               max_output_tokens=2048,
                            )
    # Creating a prompt template
    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    # Loading question-answering chain
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

# Function to split text into chunks for vectorization
def get_text_chunks(text):
    # Initializing text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    # Splitting text into chunks
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save vector store from text chunks
def get_vector_store(text_chunks):
    # Initializing GenerativeAI embeddings model
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    # Creating FAISS vector store from text chunks
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    # Saving vector store to local storage
    vector_store.save_local(DB_FAISS_PATH)

# Function to handle user input and generate response
def user_input(user_question):
    # Initializing GenerativeAI embeddings model
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    # Loading FAISS vector store from local storage
    new_db = FAISS.load_local(DB_FAISS_PATH, embeddings,allow_dangerous_deserialization=True)
    # Performing similarity search based on user question
    docs = new_db.similarity_search(user_question)
    # Getting conversational chain for answering questions
    chain = get_conversational_chain()
    # Initializing chat history
    chat_history = []   
    '''
    if query == "exit" or query == "quit" or query == "q":
        print('Exiting')
        sys.exit()
    '''
    # Generating response using conversational chain
    response = chain(
        {"input_documents":docs, "question": user_question,"chat_history": chat_history})

    
    return response


