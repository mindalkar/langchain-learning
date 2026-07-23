import asyncio

from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/mayurindalkar/Documents/learning/langchain/langchain-learning/servers/math_server.py"]
)

async def main():
    print("Hello from langchain-learning!")


if __name__ == "__main__":
    asyncio.run(main()) 