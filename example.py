from src.summarizer import BertSummarizer
from transformers import pipeline

# Inicializa la instancia con el modelo por defecto
summarizer = BertSummarizer()

# Sobrescribe el pipeline con un modelo más liviano, por ejemplo, "sshleifer/distilbart-cnn-12-6"
summarizer.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Texto a resumir
texto = """Artificial Intelligence (AI) has rapidly evolved over the past decade, revolutionizing multiple industries and changing the way humans interact with technology. One of the most significant advancements has been in the field of Natural Language Processing (NLP), where AI models can now understand, generate, and summarize text with human-like accuracy. AI-powered summarization tools are widely used in journalism, research, and business intelligence to extract key insights from lengthy articles, reports, and documents.

However, despite its benefits, AI-based summarization also poses several challenges. One of the major concerns is the potential for biases in AI-generated summaries. Since these models are trained on vast datasets that may contain biased information, they can unintentionally reinforce existing prejudices or misrepresent the original content. Moreover, the accuracy of AI-generated summaries depends on the complexity of the text, and in some cases, important nuances may be lost.

Another critical challenge is the ethical use of AI in content summarization. There have been concerns regarding the unauthorized use of AI-generated summaries in academic settings and news reporting, where summarization models may oversimplify or misinterpret crucial information. Additionally, as AI models become more advanced, there is a growing need for regulations and guidelines to ensure transparency and accountability in automated content generation.

Despite these challenges, the future of AI-driven summarization remains promising. Researchers continue to develop more sophisticated models that improve accuracy, reduce biases, and enhance contextual understanding. With further advancements, AI-powered summarization tools will become indispensable in various sectors, enabling users to process vast amounts of information quickly and efficiently.
"""
 
# Genera el resumen
resumen = summarizer.summarize(texto, max_length=150, min_length=25, do_sample=False)
print("Resumen:", resumen)

# Guarda el modelo en un directorio (opcional)
summarizer.save_model("./modelo_guardado")

# Carga el modelo guardado (opcional)
modelo_cargado = BertSummarizer.load_model("./modelo_guardado")
