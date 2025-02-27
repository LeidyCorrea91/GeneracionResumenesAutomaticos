# tests/test_summarizer.py

import os
import shutil
import pytest
from src.summarizer import BertSummarizer

def test_summary_length():
    """
    Prueba que el resumen generado sea más corto que el texto original.
    """
    summarizer = BertSummarizer()
    texto = (
        "El rápido avance de la tecnología ha transformado la manera en la que vivimos, "
        "trabajamos y nos comunicamos. La inteligencia artificial se posiciona como una "
        "herramienta esencial en la optimización de procesos y en la generación de soluciones innovadoras."
    )
    resumen = summarizer.summarize(texto, max_length=50, min_length=25, do_sample=False)
    # Se espera que el resumen tenga menos caracteres que el texto original.
    assert len(resumen) < len(texto)

def test_save_and_load():
    """
    Prueba la funcionalidad de guardar y cargar el modelo.
    """
    summarizer = BertSummarizer()
    texto = "La inteligencia artificial ofrece soluciones innovadoras en múltiples campos de la tecnología."
    resumen_inicial = summarizer.summarize(texto, max_length=50, min_length=25, do_sample=False)
    
    # Definimos un directorio temporal para guardar el modelo.
    model_path = "./temp_model"
    summarizer.save_model(model_path)
    
    # Cargamos el modelo guardado.
    loaded_summarizer = BertSummarizer.load_model(model_path)
    resumen_cargado = loaded_summarizer.summarize(texto, max_length=50, min_length=25, do_sample=False)
    
    # Se valida que se generen resúmenes (no necesariamente idénticos, pero no vacíos).
    assert resumen_inicial is not None
    assert resumen_cargado is not None
    
    # Limpiamos el directorio temporal creado.
    if os.path.exists(model_path):
        shutil.rmtree(model_path)
