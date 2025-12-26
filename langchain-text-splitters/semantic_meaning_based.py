from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter=SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
    
)

sample="""
Agriculture is the backbone of the Indian economy, employing a large portion of the rural population. Farmers rely on seasonal rains and modern techniques to increase their yield.
On the other hand, the Indian Premier League (IPL) is a massive cricketing event that captures the nation's attention every summer. Franchises compete fiercely, and fans passionately support their favorite teams.
Terrorism remains a serious threat to global peace and security. It disrupts societies, causes loss of innocent lives, and spreads fear across communities, demanding constant vigilance and international cooperation.
"""

docs=text_splitter.create_documents([sample])
print(len(docs))
print(docs)