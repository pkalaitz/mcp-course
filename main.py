import asyncio

from dotenv import load_dotenv
from langchain.agents import create_agent
#from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools  # .tools correction
from langchain_ollama import ChatOllama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOllama(model="qwen3:4b", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python",
    args=[r"C:\Users\pkala\myPythonProjects\course_udemy\11_2_MCP_Servers\mcp-crash-course\servers\math_server.py"],

)


async def main():  # make it co-routine
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
