---

```markdown
# Media Tools

The `media` module within the `langchain_tools` package provides utilities for handling media-related tasks such as audio processing and text-to-image generation. These tools are designed to integrate seamlessly with LangChain and external APIs to enhance multi-modal AI workflows.

## Directory Structure

```
media/
├── audio_processing_tool.py   # Tools for handling and processing audio files.
├── text_to_image_tool.py      # Tools for generating images from textual prompts.
├── README.md                  # Documentation for the media tools module.
```

## Features

### Audio Processing Tools

The `audio_processing_tool.py` script provides functionality for:
- **Speech-to-Text**:
  - Integration with OpenAI's Whisper API for accurate speech-to-text conversion.
  - Option to use AssemblyAI API for speech recognition as an alternative.
- **Text-to-Speech**:
  - Support for ElevenLabs Speech Synthesis API for generating realistic and distinct voices.

### Text-to-Image Tools

The `text_to_image_tool.py` script enables:
- **Text-to-Image Generation**:
  - Integration with OpenAI's DALL·E API to generate images based on textual descriptions.
  - Option to use Google's Gemini API for enhanced visual outputs (if available).
  - Extensibility to incorporate additional text-to-image APIs for diverse capabilities.

## Usage

### Audio Processing

To use the `audio_processing_tool`:
1. Configure API keys in your environment or a `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ASSEMBLYAI_API_KEY=your_assemblyai_api_key
    ELEVENLABS_API_KEY=your_elevenlabs_api_key
    ```
2. Example code for speech-to-text:
    ```python
    from media.audio_processing_tool import AudioProcessingTool

    audio_tool = AudioProcessingTool(openai_api_key="your_openai_api_key")
    transcript = audio_tool.speech_to_text("path_to_audio_file.wav")
    print(transcript)
    ```
3. Example code for text-to-speech:
    ```python
    audio_tool = AudioProcessingTool(elevenlabs_api_key="your_elevenlabs_api_key")
    audio_tool.text_to_speech("Hello, this is a test.", "output_audio.mp3")
    ```

### Text-to-Image Generation

To use the `text_to_image_tool`:
1. Configure API keys:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    GEMINI_API_KEY=your_gemini_api_key
    ```
2. Example code for generating an image:
    ```python
    from media.text_to_image_tool import TextToImageTool

    image_tool = TextToImageTool(openai_api_key="your_openai_api_key", gemini_api_key="your_gemini_api_key")
    image_tool.generate_image_openai("A futuristic cityscape", "cityscape_openai.png")
    image_tool.generate_image_gemini("A lush green forest with sunlight", "forest_gemini.png")
    ```

## Extensibility

These tools are designed with modularity in mind:
- **Adding New APIs**: To integrate additional APIs, extend the existing classes with appropriate methods for the new API.
- **Custom Workflows**: Combine media tools with LangChain chains to build multi-modal AI pipelines.

## Dependencies

Ensure the following dependencies are installed:
- `openai`
- `requests`
- `dotenv`

Install them using pip:
```bash
pip install openai requests python-dotenv
```

## Contribution

We welcome contributions to enhance the functionality of the media tools. Feel free to open issues or submit pull requests on the project's GitHub repository.

---