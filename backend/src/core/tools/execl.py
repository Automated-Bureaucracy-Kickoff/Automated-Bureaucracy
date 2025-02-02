import logging
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_core.tools import tool

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_excel(file_path: str, mode: str = "elements"):
    """
    Loads an Excel file using UnstructuredExcelLoader.
    
    Parameters:
        file_path (str): Path to the Excel file.
        mode (str): Mode of loading (default is 'elements').
    
    Returns:
        list: List of loaded documents from the Excel file.
    """
    try:
        loader = UnstructuredExcelLoader(
            file_path=file_path,
            mode=mode
        )
        data = loader.load()
        logging.info("Successfully loaded Excel file: %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading Excel file: %s - %s", file_path, str(e))
        return []

# Example usage:
# excel_data = load_excel("example_data/stanley-cups.xlsx", mode="elements")
# print(excel_data[0].metadata["text_as_html"])
