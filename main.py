from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for the source used by the agent."""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent's response with source and answer."""
    answer:str = Field(description="The agent's answer to the query")
    source: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer.")


# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result.
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-learning!")
    result = agent.invoke({"messages": HumanMessage(content="Search for three job postings for an AI engineer using langchain in Tampa on linkedin and list their details. ")})
    print(result)


if __name__ == "__main__":
    main()
