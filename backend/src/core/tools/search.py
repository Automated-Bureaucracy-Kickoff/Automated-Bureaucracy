from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

ddgsearch = DuckDuckGoSearchRun()

@tool
def search(query: str) -> str:
    """Search duck duck go

    Args:
        query (str): query

    Returns:
        str: result
    """
    print(f"Invoking search tool with query: {query}")
    result = ddgsearch.invoke(query)
    return result if result and result.strip() else "No results found."