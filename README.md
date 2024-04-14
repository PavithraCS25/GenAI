# GenAI
This repository consists of the code to my GenAI projects. Below are the steps to use it.

Clone the repository and add the below folders to your root i.e. GenAIchat folder.
1. appreciations - save all the screenshots of the appreciations that you have received so far
2. brands - save the logo/icon of the brands that you have worked so far
3. certifications - save the images of the certifications that you have completed so far
4. images - save the page images, and the project specific image if any
5. vectorstore/db_faiss - create a folder to store the FAISS vector for retrieval chain

Add the GOOGLE_API_KEY in your terminal
```export GOOGLE_API_KEY='<your api key>'```

Add the AWS secret key from your terminal
```aws configure```
Enter the aws ID, secret key, default region and default file format

pip install -r requirements.txt

streamlit run home.py --server.enableXsrfProtection false

Open the application using the private or public URL displayed
