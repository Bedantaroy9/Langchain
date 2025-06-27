from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_templet = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_hist'), #fetch chat history 
    ('human','{query}')
])

chat_hist = []

with open('chat_hist.txt') as f:
    chat_hist.append(f.readlines())

print(chat_hist)

prompt = chat_templet.invoke({'chat_hist':chat_hist, 'query':'Where is my refund'})

print(prompt)