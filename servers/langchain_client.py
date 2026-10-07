import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
#from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

load_dotenv()

#llm = ChatOpenAI()
llm = ChatOllama(model="qwen3.4b", temperature=0)


async def main():
    print("hello langchain mcp")

if __name__ == "__main__":
    asyncio.run(main())