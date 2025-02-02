import logging
from langchain_community.document_loaders.csv_loader import CSVLoader, UnstructuredCSVLoader

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_structured_csv(file_path: str, csv_args: dict):
    """
    Loads a structured CSV file using CSVLoader.
    
    Parameters:
        file_path (str): Path to the CSV file.
        csv_args (dict): Dictionary of CSV arguments (e.g., delimiter, quotechar, fieldnames).
    
    Returns:
        list: List of loaded documents from the CSV file.
    """
    try:
        loader = CSVLoader(
            file_path=file_path,
            csv_args=csv_args
        )
        data = loader.load()
        logging.info("Successfully loaded structured CSV file: %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading structured CSV file: %s - %s", file_path, str(e))
        return []

def load_unstructured_csv(file_path: str, mode: str):
    """
    Loads an unstructured CSV file using UnstructuredCSVLoader.
    
    Parameters:
        file_path (str): Path to the CSV file.
        mode (str): Mode of loading (e.g., 'elements').
    
    Returns:
        list: List of loaded documents from the CSV file.
    """
    try:
        loader = UnstructuredCSVLoader(
            file_path=file_path,
            mode=mode
        )
        data = loader.load()
        logging.info("Successfully loaded unstructured CSV file: %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading unstructured CSV file: %s - %s", file_path, str(e))
        return []

# Example usage:
# structured_data = load_structured_csv("example_data/mlb_teams_2012.csv", {"delimiter": ",", "quotechar": '"', "fieldnames": ["MLB Team", "Payroll in millions", "Wins"]})
# unstructured_data = load_unstructured_csv("example_data/mlb_teams_2012.csv", "elements")
# print(unstructured_data[0].metadata["text_as_html"])
