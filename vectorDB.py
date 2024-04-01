from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


# 保存
def save_vector_store(textChunks):
    """将 pdf 读取到的文本向量化以后，通过 FAISS 保存到本地"""
    db = FAISS.from_texts(textChunks, OpenAIEmbeddings())
    db.save_local('faiss')


# 加载
def load_vector_store():
    return FAISS.load_local('faiss', OpenAIEmbeddings())
