import os
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore
from src.helper import huggingface_embed, load_pdf_file, text_split
from dotenv import load_dotenv
load_dotenv()

PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY

ext_data=load_pdf_file(data="Data/")
text_chunk=text_split(ext_data)
embedding=huggingface_embed()

pc=Pinecone(api_key=PINECONE_API_KEY)
index_name = "medbot"


pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)


docsearch=PineconeVectorStore.from_documents(documents=text_chunk,
                                             index_name=index_name,
                                             embedding=embedding)