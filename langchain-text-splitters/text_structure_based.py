from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
Space exploration is the investigation of celestial objects and space beyond Earth's atmosphere, utilizing both robotic probes and human spaceflight. It encompasses a wide range of activities, from studying planets and moons within our solar system to searching for potentially habitable exoplanets and even seeking signs of extraterrestrial life. This field is driven by scientific curiosity, technological advancements, and the potential for groundbreaking discoveries that could benefit humanity. 
Key Aspects of Space Exploration:
Scientific Discovery:
Space exploration allows us to study the origins of the universe, the formation of planets, and the potential for life beyond Earth. 
Technological Advancement:
The challenges of space exploration drive innovation in various fields, including rocketry, materials science, robotics, and computing. 
Resource Utilization:
Exploring space could lead to the discovery of new resources and the potential for in-situ resource utilization (ISRU), which could support future space activities. 
Inspiration and Education:
Space exploration inspires young people to pursue careers in STEM fields and captures the public imagination, fostering a sense of wonder and excitement about the universe. 
International Collaboration:
Many space agencies and organizations collaborate on space exploration missions, fostering international cooperation and sharing of knowledge. 
Historical Highlights:
The launch of Sputnik 1 in 1957 marked the beginning of the space age. 
The first human in space, Yuri Gagarin, followed in 1961. 
The Apollo missions, culminating in the first Moon landing in 1969, demonstrated human capabilities in deep space. 
Robotic spacecraft have explored all the major planets and many other celestial bodies in our solar system. 
The International Space Station (ISS) has been a platform for scientific research and international collaboration for over two decades. 
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0 
)
chunks=splitter.split_text(text)

print(len(chunks))
print(chunks[28])