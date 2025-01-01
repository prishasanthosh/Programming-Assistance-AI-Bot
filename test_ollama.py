import requests
import json

def test_ollama():
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "codellama",
                "prompt": "Print 'Hello, World!' in Python",
                "max_tokens": 50
            },
            stream=True  # Enable streaming
        )
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print("Streamed Response Content:")
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                json_response = json.loads(line)
                print(json_response)
                if 'response' in json_response:
                    full_response += json_response['response']
                if json_response.get('done', False):
                    break
        
        print("\nFull Response:")
        print(full_response)
        
    except requests.RequestException as e:
        print(f"An error occurred while making the request: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    test_ollama()

