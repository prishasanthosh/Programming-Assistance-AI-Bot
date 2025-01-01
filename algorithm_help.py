class AlgorithmHelp:
    def __init__(self, ollama_model):
        self.ollama_model = ollama_model

    def explain_algorithm(self, algorithm):
        prompt = f"Explain the following algorithm with a code example:\n\n{algorithm}\n\nExplanation and code:"
        return self.ollama_model.generate_response(prompt)

