import ollama

class MultiSkillAgent:
    def __init__(self, model="llama3.2"):
        self.model = model

    def act(self, task_type, data):
        """
        Router interno del agente.
        """
        if task_type == "traducir":
            return self._translate(data["text"], data["source"], data["target"])
        elif task_type == "detectar":
            return self._detect(data["text"])
        elif task_type == "pulir":
            return self._polish(data["text"])
        else:
            return "Habilidad no reconocida."

    def _translate(self, text, src, tgt):
        prompt = f"Translate from {src} to {tgt}. Return ONLY the translation: {text}"
        return self._call_ollama(prompt)

    def _detect(self, text):
        prompt = f"Identify the language of this text. Return ONLY the language name: {text}"
        return self._call_ollama(prompt)

    def _polish(self, text):
        prompt = f"Rewrite this text to be more professional and natural. Return ONLY the result: {text}"
        return self._call_ollama(prompt)

    #Python habla con la IA
    def _call_ollama(self, prompt):
        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response'].strip()
        except Exception as e:
            return f"Error: {str(e)}"