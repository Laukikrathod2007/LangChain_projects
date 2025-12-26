from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model = ChatOpenAI()
class Review(TypedDict):
    Summary = str
    Sentiment = str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I’ve been using these wireless Bluetooth headphones for a few weeks now, and overall, I’m quite satisfied with the experience. The sound quality is clear with good bass, and the noise isolation works well for everyday use like commuting or studying.""")

print(result)