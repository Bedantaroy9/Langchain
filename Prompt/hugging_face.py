from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="chat-completion"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("hi")
print(result.content)
