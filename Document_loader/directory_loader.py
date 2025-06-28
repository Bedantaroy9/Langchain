from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',  #folder name 
    glob='*.pdf',   #what is consist in the folder
    loader_cls=PyPDFLoader # what loader need to runin each files
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)