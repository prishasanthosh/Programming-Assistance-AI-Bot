class Optimization:
    def __init__(self, llama_model):
        self.llama_model = llama_model

    def optimize_code(self, code):
        prompt = f"Suggest improvements for the following code:\n\n{code}\n\nOptimization suggestions:"
        return self.llama_model.generate_response(prompt)

