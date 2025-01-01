class Debugging:
    def __init__(self, ollama_model):
        self.ollama_model = ollama_model

    def debug_code(self, code):
        prompt = f"Identify and fix issues in the following code:\n\n{code}\n\nDebug report and fixed code:"
        return self.ollama_model.generate_response(prompt)

