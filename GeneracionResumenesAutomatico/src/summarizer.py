# src/summarizer.py

import os
from transformers import pipeline

class BertSummarizer:
    def __init__(self):
        """
        Inicializa el pipeline de resumen. Para efectos de este ejemplo se utiliza
        el modelo 'facebook/bart-large-cnn', aunque en el proyecto se denomine "BERT".
        """
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def summarize(self, text: str, **kwargs) -> str:
        """
        Genera un resumen del texto de entrada.

        Parámetros:
            text (str): Texto a resumir.
            kwargs: Parámetros adicionales para el pipeline (por ejemplo, max_length, min_length).

        Retorna:
            str: El resumen generado.
        """
        summary = self.summarizer(text, **kwargs)
        return summary[0]['summary_text']

    def save_model(self, path: str):
        """
        Guarda el modelo y el tokenizador en el directorio especificado.

        Parámetros:
            path (str): Directorio donde se guardará el modelo.
        """
        os.makedirs(path, exist_ok=True)
        self.summarizer.model.save_pretrained(path)
        self.summarizer.tokenizer.save_pretrained(path)
    
    @classmethod
    def load_model(cls, path: str) -> "BertSummarizer":
        """
        Crea una instancia de BertSummarizer a partir de un modelo previamente guardado.

        Parámetros:
            path (str): Directorio donde se encuentra el modelo guardado.

        Retorna:
            BertSummarizer: Instancia con el modelo cargado.
        """
        # Crear una instancia sin ejecutar __init__
        instance = cls.__new__(cls)
        from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
        model = AutoModelForSeq2SeqLM.from_pretrained(path)
        tokenizer = AutoTokenizer.from_pretrained(path)
        instance.summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        return instance
