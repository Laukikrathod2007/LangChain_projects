from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

'''temperature is the parameter for deciding the 
creativeness/randomness of your response .
Higher the temperature , more creative or random the response is 
[YOu will get different outputs for same input if temp>1 ]
->useful for creative tasks like writing poems , stories etc .

lower the temperature , more deterministic or focused the response is
->useful for tasks like question answering, summarization etc. 
[ same input k liye same output milega if temp=0]
'''
'''max_completion_tokens is used for setting maximum no. of tokens in output 
(Length of response).'''
result=model.invoke("Tell me a poem on nature")

print(result.content)