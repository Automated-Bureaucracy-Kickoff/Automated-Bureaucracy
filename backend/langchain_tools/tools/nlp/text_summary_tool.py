import openai
from typing import Dict, Any, List


class TextSummaryTool:
    """
    A tool for generating text summaries using OpenAI's GPT API or other NLP models.
    """

    def __init__(self, openai_api_key: str):
        """
        Initialize the text summary tool.

        Args:
            openai_api_key (str): The API key for OpenAI.
        """
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def summarize_openai(self, text: str, max_length: int = 100) -> Dict[str, Any]:
        """
        Generate a summary for the given text using OpenAI's GPT API.

        Args:
            text (str): The text to summarize.
            max_length (int): The maximum length of the summary.

        Returns:
            Dict[str, Any]: The summary result.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a text summarization assistant."},
                    {"role": "user", "content": f"Summarize the following text in {max_length} words or less:\n{text}"}
                ],
                temperature=0.7,
            )
            summary = response["choices"][0]["message"]["content"]
            return {"summary": summary}
        except Exception as e:
            return {"error": str(e)}

    def summarize_custom(self, text: str, custom_model: Any, max_length: int = 100) -> Dict[str, Any]:
        """
        Generate a summary for the given text using a custom NLP model.

        Args:
            text (str): The text to summarize.
            custom_model (Any): The custom model instance.
            max_length (int): The maximum length of the summary.

        Returns:
            Dict[str, Any]: The summary result.
        """
        try:
            # Custom model's summarization logic (e.g., Hugging Face model pipeline)
            summary = custom_model.summarize(text, max_length=max_length)
            return {"summary": summary}
        except Exception as e:
            return {"error": str(e)}

    def batch_summarize(self, texts: List[str], use_openai: bool = True, custom_model: Any = None, max_length: int = 100) -> List[Dict[str, Any]]:
        """
        Generate summaries for a list of texts.

        Args:
            texts (List[str]): List of texts to summarize.
            use_openai (bool): Whether to use OpenAI API for summarization.
            custom_model (Any): Custom NLP model instance (if not using OpenAI).
            max_length (int): The maximum length of each summary.

        Returns:
            List[Dict[str, Any]]: List of summary results for each text.
        """
        results = []
        for text in texts:
            if use_openai:
                results.append(self.summarize_openai(text, max_length=max_length))
            elif custom_model:
                results.append(self.summarize_custom(text, custom_model, max_length=max_length))
            else:
                results.append({"error": "No valid summarization method provided."})
        return results


# Example usage
if __name__ == "__main__":
    # Replace with your OpenAI API key
    api_key = "your_openai_api_key"

    tool = TextSummaryTool(openai_api_key=api_key)

    # Single text summarization
    text = "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and act like humans. It has become a rapidly evolving field with applications in various industries, including healthcare, finance, and education. Advances in AI technology continue to transform the way we work and live."
    single_summary = tool.summarize_openai(text, max_length=50)
    print("Single Summary Result:", single_summary)

    # Batch text summarization
    texts = [
        "Machine learning is a subset of AI that focuses on building systems that can learn and improve from experience without being explicitly programmed.",
        "Deep learning, a branch of machine learning, uses neural networks to simulate the human brain in processing data and making predictions.",
        "Natural language processing enables computers to understand, interpret, and respond to human language."
    ]
    batch_summaries = tool.batch_summarize(texts, max_length=40)
    print("Batch Summaries Results:", batch_summaries)
