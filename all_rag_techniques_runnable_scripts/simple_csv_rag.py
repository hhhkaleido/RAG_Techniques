from langchain_community.document_loaders.csv_loader import CSVLoader
from pathlib import Path
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set the OpenAI API key environment variable
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")


import os
os.makedirs('data', exist_ok=True)

import pandas as pd

file_path = ('data/customers-100.csv') # insert the path of the csv file
data = pd.read_csv(file_path)

#preview the csv file
data.head()

# load and process csv data




loader = CSVLoader(file_path=file_path)
docs = loader.load_and_split()




import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
index = faiss.IndexFlatL2(len(OpenAIEmbeddings().embed_query(" ")))
vector_store = FAISS(
    embedding_function=OpenAIEmbeddings(),
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

# Add the splitted csv data to the vector store

vector_store.add_documents(documents=docs)

# Create the retrieval chain


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter

retriever = vector_store.as_retriever()

# Set up system prompt
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
    
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Create the question-answer chain
rag_chain = (
    {"context": itemgetter("input") | retriever | format_docs, "input": itemgetter("input")}
    | prompt
    | llm
    | StrOutputParser()
)


# Query the rag bot with a question based on the CSV data




answer = rag_chain.invoke({"input": "which company does sheryl Baxter work for?"})
print(answer)
