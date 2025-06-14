from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from openai import OpenAI
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_history = defaultdict(list)

db = FAISS.load_local("vector_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4"),
    retriever=db.as_retriever()
)
