from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_name: Person={'name':'bedanta', 'age':23}

print(new_name)

from langchain_openai import ChatOpenAI
model = ChatOpenAI()
model.with_structured_output