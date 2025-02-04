
from langchain_community.document_loaders import JSONLoader

from langchain_core.tools import tool

@tool
def load_json(path: str, jq_schema: str = ".messages[].content", text_content: bool = False):
    """
    Load a JSON file from the given path and extract content using the provided jq schema.

    Parameters:
        path (str): The file path to the JSON file.
        jq_schema (str): The jq query used to extract document content.
                         Defaults to ".messages[].content".
        text_content (bool): Whether to treat the extracted content as text.
                             Defaults to False.

    Returns:
        List[Document]: A list of Document objects loaded from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        RuntimeError: If loading the JSON fails.
    """
    loader = JSONLoader(
        file_path=path,
        jq_schema=jq_schema,
        text_content=text_content,
    )
    
    docs = loader.load()
    return docs