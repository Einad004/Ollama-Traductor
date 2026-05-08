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
        # Ahora le pasamos también el idioma que viene del selector
            return self._polish(data["text"], data["source"])
        else:
            return "Habilidad no reconocida."

    def _translate(self, text, src, tgt):
        prompt = f"Translate from {src} to {tgt}. Return ONLY the translation: {text}"
        return self._call_ollama(prompt)

    def _detect(self, text):
        prompt = f"Identify the language of this text. Return ONLY the language name: {text}"
        return self._call_ollama(prompt)

    def _polish(self, text, lang):
        """
        Mejora el estilo del texto respetando el idioma original.
        """
        prompt = (
            f"You are a professional editor in {lang}. "
            f"Rewrite the following text in {lang} to be more professional and natural. "
            "Keep the original meaning but improve the flow and vocabulary. "
            f"Return ONLY the improved text in {lang}, do not explain anything."
            f"\n\nText: {text}"
        )
        return self._call_ollama(prompt)

    #Python habla con la IA
    def _call_ollama(self, prompt):
        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response'].strip()
        except Exception as e:
            return f"Error: {str(e)}"