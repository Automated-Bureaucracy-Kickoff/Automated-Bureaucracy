from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path: str):
    loader = PyPDFLoader(path)
    doc = loader.load()
    return doc[0]

def load_dir_of_pdfs(path: str):
    