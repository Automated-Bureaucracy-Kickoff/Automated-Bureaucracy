import openai
from typing import Dict, Any


class SentimentAnalysisTool:
    """
    A tool for performing sentiment analysis on textual data using OpenAI's GPT API or other NLP models.
    """

    def __init__(self, openai_api_key: str):
        """
        Initialize the sentiment analysis tool.

        Args:
            openai_api_key (str): The API key for OpenAI.
        """
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def analyze_sentiment_openai(self, text: str) -> Dict[str, Any]:
        """
        Analyze the sentiment of the given text using OpenAI's GPT API.

        Args:
            text (str): The text to analyze.

        Returns:
            Dict[str, Any]: The sentiment analysis result, including sentiment and confidence score.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a sentiment analysis assistant."},
                    {"role": "user", "content": f"Analyze the sentiment of the following text: {text}"}
                ],
                temperature=0.7,
            )
            result = response["choices"][0]["message"]["content"]
            return {"sentiment_analysis": result}
        except Exception as e:
            return {"error": str(e)}

    def analyze_sentiment_custom(self, text: str, custom_model: Any) -> Dict[str, Any]:
        """
        Analyze the sentiment of the given text using a custom NLP model.

        Args:
            text (str): The text to analyze.
            custom_model (Any): The custom model instance.

        Returns:
            Dict[str, Any]: The sentiment analysis result, including sentiment and confidence score.
        """
        try:
            # Custom model's analysis logic (e.g., a pretrained Hugging Face transformer)
            result = custom_model.analyze(text)
            return {"sentiment_analysis": result}
        except Exception as e:
            return {"error": str(e)}

    def batch_analyze_sentiment(self, texts: list, use_openai: bool = True, custom_model: Any = None) -> list:
        """
        Perform batch sentiment analysis on a list of texts.

        Args:
            texts (list): List of texts to analyze.
            use_openai (bool): Whether to use OpenAI API for sentiment analysis.
            custom_model (Any): Custom NLP model instance (if not using OpenAI).

        Returns:
            list: List of sentiment analysis results for each text.
        """
        results = []
        for text in texts:
            if use_openai:
                results.append(self.analyze_sentiment_openai(text))
            elif custom_model:
                results.append(self.analyze_sentiment_custom(text, custom_model))
            else:
                results.append({"error": "No valid analysis method provided."})
        return results


# Example usage
if __name__ == "__main__":
    # Replace with your OpenAI API key
    api_key = "your_openai_api_key"

    tool = SentimentAnalysisTool(openai_api_key=api_key)

    # Single text analysis
    single_result = tool.analyze_sentiment_openai("I love this product! It works wonderfully.")
    print("Single Analysis Result:", single_result)

    # Batch text analysis
    texts = [
        "This is the best day of my life!",
        "I am very disappointed with the service.",
        "The movie was okay, not great but not bad either."
    ]
    batch_results = tool.batch_analyze_sentiment(texts)
    print("Batch Analysis Results:", batch_results)
