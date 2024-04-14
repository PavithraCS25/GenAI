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

content_type = "image/jpeg"
DB_FAISS_PATH = 'vectorstore/db_faiss'
def process_image(images):
    for image in images:
        # To read file as bytes:
        image = PIL.Image.open(image)
        result_json = generate_df(image)
    return result_json

def generate_df(part):
  model = genai.GenerativeModel("gemini-pro-vision")
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
  print(responses.text)
  return responses.text

def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                               temperature=0.1,
                               max_output_tokens=2048,
                            )

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(DB_FAISS_PATH)

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local(DB_FAISS_PATH, embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    
    #To be modified
    chat_history = []   
    '''
    if query == "exit" or query == "quit" or query == "q":
        print('Exiting')
        sys.exit()
    '''
    response = chain(
        {"input_documents":docs, "question": user_question,"chat_history": chat_history})

    
    return response


