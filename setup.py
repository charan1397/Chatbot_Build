from setuptools import find_packages, setup

setup(
    name="Medical_Chatbot",
    version="0.1.0",
    author="RAM",
    author_email="RAM@GMAIL.COM",
    packages=find_packages(),
    install_requires=[
        "flask==3.1.1",
        "torch",
        "transformers",
        "sentence-transformers==4.1.0",
        "langchain==0.3.26",
        "pypdf==5.6.1",
        "python-dotenv==1.1.0",
        "langchain-pinecone==0.2.8",
        "langchain-openai==0.3.24",        
        "langchain-community==0.3.26",
    ],
)