import openai
import requests
import base64
import os

class TextToImageTool:
    def __init__(self, openai_api_key: str, gemini_api_key: str = None):
        """
        Initializes the TextToImageTool with API keys.

        Args:
            openai_api_key (str): API key for OpenAI.
            gemini_api_key (str, optional): API key for Google's Gemini API. Defaults to None.
        """
        self.openai_api_key = openai_api_key
        self.gemini_api_key = gemini_api_key
        openai.api_key = openai_api_key

    def generate_image_openai(self, prompt: str, output_path: str = "openai_image.png"):
        """
        Generates an image from text using OpenAI's DALL·E API.

        Args:
            prompt (str): The text prompt to generate the image.
            output_path (str, optional): Path to save the generated image. Defaults to "openai_image.png".
        """
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            image_data = requests.get(image_url).content
            with open(output_path, 'wb') as file:
                file.write(image_data)
            print(f"Image saved to {output_path}")
        except Exception as e:
            print(f"An error occurred with OpenAI API: {e}")

    def generate_image_gemini(self, prompt: str, output_path: str = "gemini_image.png"):
        """
        Generates an image from text using Google's Gemini API.

        Args:
            prompt (str): The text prompt to generate the image.
            output_path (str, optional): Path to save the generated image. Defaults to "gemini_image.png".
        """
        if not self.gemini_api_key:
            print("Gemini API key is not provided.")
            return

        try:
            api_url = "https://gemini-api.example.com/v1/generate-image"  # Replace with the actual Gemini API endpoint
            headers = {
                "Authorization": f"Bearer {self.gemini_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "prompt": prompt,
                "image_size": "1024x1024"
            }
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()
            image_data = base64.b64decode(response.json()['image_base64'])
            with open(output_path, 'wb') as file:
                file.write(image_data)
            print(f"Image saved to {output_path}")
        except Exception as e:
            print(f"An error occurred with Gemini API: {e}")

# Example usage
if __name__ == "__main__":
    openai_api_key = "your_openai_api_key"
    gemini_api_key = "your_gemini_api_key"  # Optional

    tool = TextToImageTool(openai_api_key, gemini_api_key)

    prompt = "A futuristic cityscape at sunset."

    # Generate image using OpenAI
    tool.generate_image_openai(prompt, "openai_cityscape.png")

    # Generate image using Gemini (if API key is provided)
    if gemini_api_key:
        tool.generate_image_gemini(prompt, "gemini_cityscape.png")
