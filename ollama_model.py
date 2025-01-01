import requests
import json

class OllamaModel:
    def __init__(self, model_name="codellama", api_base="http://localhost:11434"):
        self.model_name = model_name
        self.api_base = api_base

    def generate_response(self, prompt, max_tokens=256):
        try:
            response = requests.post(
                f"{self.api_base}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "max_tokens": max_tokens
                },
                stream=True
            )
            response.raise_for_status()
            
            full_response = ""
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line)
                    if 'response' in json_response:
                        full_response += json_response['response']
                    if json_response.get('done', False):
                        break
            
            return full_response.strip()
        except requests.RequestException as e:
            raise Exception(f"Error communicating with Ollama: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"Error parsing Ollama response: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")

