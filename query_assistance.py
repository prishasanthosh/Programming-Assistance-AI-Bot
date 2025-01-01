class QueryAssistance:
    def __init__(self, ollama_model):
        self.ollama_model = ollama_model

    def answer_query(self, query):
        prompt = f"Answer the following programming question with an example:\n\n{query}\n\nAnswer:"
        return self.ollama_model.generate_response(prompt)

