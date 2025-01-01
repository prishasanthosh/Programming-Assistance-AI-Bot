class PracticeProblems:
    def __init__(self, ollama_model):
        self.ollama_model = ollama_model

    def get_problem(self, difficulty):
        prompt = f"Generate a {difficulty} programming problem with hints and a solution:\n\nProblem, hints, and solution:"
        return self.ollama_model.generate_response(prompt)

