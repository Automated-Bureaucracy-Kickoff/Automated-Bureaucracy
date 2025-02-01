import openai
import requests
import os

class AudioProcessingTool:
    def __init__(self, openai_api_key: str, assemblyai_api_key: str, elevenlabs_api_key: str):
        """
        Initializes the audio processing tool with API keys for OpenAI, AssemblyAI, and ElevenLabs.

        Args:
            openai_api_key (str): API key for OpenAI Whisper.
            assemblyai_api_key (str): API key for AssemblyAI.
            elevenlabs_api_key (str): API key for ElevenLabs Speech Synthesis.
        """
        self.openai_api_key = openai_api_key
        self.assemblyai_api_key = assemblyai_api_key
        self.elevenlabs_api_key = elevenlabs_api_key
        openai.api_key = openai_api_key

    def transcribe_audio_openai(self, audio_file_path: str, language: str = None) -> str:
        """
        Transcribes audio using OpenAI Whisper.

        Args:
            audio_file_path (str): Path to the audio file.
            language (str, optional): Language of the audio. Defaults to auto-detect.

        Returns:
            str: Transcribed text.
        """
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file '{audio_file_path}' does not exist.")

        try:
            with open(audio_file_path, "rb") as audio_file:
                transcription = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio_file,
                    language=language
                )
            return transcription['text']
        except Exception as e:
            raise RuntimeError(f"OpenAI Whisper transcription failed: {e}")

    def transcribe_audio_assemblyai(self, audio_file_path: str) -> str:
        """
        Transcribes audio using AssemblyAI.

        Args:
            audio_file_path (str): Path to the audio file.

        Returns:
            str: Transcribed text.
        """
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file '{audio_file_path}' does not exist.")

        headers = {'authorization': self.assemblyai_api_key}
        upload_url = "https://api.assemblyai.com/v2/upload"

        try:
            # Upload file to AssemblyAI
            with open(audio_file_path, 'rb') as audio_file:
                response = requests.post(upload_url, headers=headers, files={'file': audio_file})
                response.raise_for_status()
                upload_data = response.json()
            audio_url = upload_data['upload_url']

            # Transcribe audio
            transcription_url = "https://api.assemblyai.com/v2/transcript"
            transcript_request = {"audio_url": audio_url}
            response = requests.post(transcription_url, headers=headers, json=transcript_request)
            response.raise_for_status()
            transcript_data = response.json()

            # Wait for transcription to complete
            transcript_id = transcript_data['id']
            while True:
                status_url = f"{transcription_url}/{transcript_id}"
                response = requests.get(status_url, headers=headers)
                response.raise_for_status()
                status_data = response.json()
                if status_data['status'] == 'completed':
                    return status_data['text']
                elif status_data['status'] == 'failed':
                    raise RuntimeError("AssemblyAI transcription failed")
        except Exception as e:
            raise RuntimeError(f"AssemblyAI transcription failed: {e}")

    def synthesize_speech_elevenlabs(self, text: str, voice: str = "Adam", output_path: str = "output.mp3") -> None:
        """
        Synthesizes speech using ElevenLabs Speech Synthesis API.

        Args:
            text (str): Text to be converted to speech.
            voice (str, optional): Voice to use. Defaults to "Adam".
            output_path (str, optional): Path to save the output audio file. Defaults to "output.mp3".

        Returns:
            None
        """
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
        headers = {
            "accept": "audio/mpeg",
            "xi-api-key": self.elevenlabs_api_key,
            "Content-Type": "application/json"
        }
        data = {"text": text, "model_id": "eleven_monolingual_v1"}

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            with open(output_path, "wb") as audio_file:
                audio_file.write(response.content)
            print(f"Audio saved to {output_path}")
        except Exception as e:
            raise RuntimeError(f"ElevenLabs speech synthesis failed: {e}")

# Usage Example
if __name__ == "__main__":
    # Replace these API keys with your actual keys
    openai_api_key = "your_openai_api_key"
    assemblyai_api_key = "your_assemblyai_api_key"
    elevenlabs_api_key = "your_elevenlabs_api_key"

    audio_tool = AudioProcessingTool(
        openai_api_key=openai_api_key,
        assemblyai_api_key=assemblyai_api_key,
        elevenlabs_api_key=elevenlabs_api_key
    )

    try:
        # Transcribe using OpenAI Whisper
        transcription_openai = audio_tool.transcribe_audio_openai("path/to/audio.mp3")
        print("OpenAI Whisper Transcription:", transcription_openai)

        # Transcribe using AssemblyAI
        transcription_assemblyai = audio_tool.transcribe_audio_assemblyai("path/to/audio.mp3")
        print("AssemblyAI Transcription:", transcription_assemblyai)

        # Synthesize speech using ElevenLabs
        audio_tool.synthesize_speech_elevenlabs(
            text="Hello, this is a synthesized voice from ElevenLabs.",
            voice="Rachel",
            output_path="synthesized_audio.mp3"
        )
    except Exception as e:
        print(e)
