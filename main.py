import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
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


async def main():  #make it co-routine so it's creating an object below
    async with stdio_client(stdio_server_params) as (read,write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session Initialized")
            #tools = await session.list_tools()
            tools = await load_mcp_tools(session)
            #print(f"Tools Listed \n{tools}")

            agent = create_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 54 + 2 * 3?")]})
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())

