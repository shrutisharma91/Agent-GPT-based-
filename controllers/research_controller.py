from utils.file_utils import process_file
from utils.text_utils import split_text
from utils.citation_utils import format_citation
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import FAISS
from config import OPENAI_API_KEY
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(file):
    text = process_file(file)
    chunks = split_text(text)
    summary = ""
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    for chunk in chunks:
        prompt = f"Summarize the following text:\n\n{chunk}"
        summary += llm.predict(prompt) + "\n"
    return {"summary": summary}

def answer_query(file, query):
    text = process_file(file)
    chunks = split_text(text)
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(chunks, embeddings)
    search_results = docsearch.similarity_search(query, k=1)
    relevant_text = search_results[0].page_content
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    prompt = f"The following is the content of a research paper:\n\n{relevant_text}\n\nUser's query: {query}\n\nProvide a relevant answer based on the research paper."
    answer = llm.predict(prompt)
    return {"answer": answer}

def generate_citation(author, title, year, publisher):
    return {"citation": format_citation(author, title, year, publisher)}