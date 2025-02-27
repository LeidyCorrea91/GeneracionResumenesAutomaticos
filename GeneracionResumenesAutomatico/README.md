# 📄 Generación de Resúmenes Automáticos en Ingles con BERT

## 📌 Descripción del Proyecto

Este proyecto implementa un modelo de **Inteligencia Artificial** basado en **BERT** para la **generación automática de resúmenes de texto**. Está diseñado para procesar documentos extensos y extraer información clave, reduciendo el contenido sin perder su esencia.  

El modelo utiliza la librería `transformers` de **Hugging Face** y puede ejecutarse dentro de un contenedor Docker. Además, incluye **pruebas automatizadas** para validar su correcto funcionamiento y una arquitectura modular con buena cohesión y acoplamiento.

---

## 🎯 **¿Por qué este proyecto?**

Hoy en día, el volumen de información digital es **abrumador** y leer documentos largos puede ser ineficiente. Este proyecto resuelve ese problema proporcionando **resúmenes automáticos en ingles** que permiten extraer los puntos clave de un texto **rápida y eficientemente**.

**Casos de uso:**
- Automatización de resúmenes en **periodismo y noticias** 📰.
- Procesamiento de documentos extensos en **negocios y análisis de datos** 📊.
- Mejora de la accesibilidad a información científica en **investigación y educación** 📚.

---

## 🏗 **Estructura del Proyecto**

El proyecto sigue un diseño modular basado en **cohesión y bajo acoplamiento**, asegurando que cada componente **tenga una única responsabilidad y pueda modificarse sin afectar el resto**.


---

## 🛠 **Arquitectura**

<details>
  <summary>📌 <strong>summarizer.py (src/)</strong></summary>

  - Contiene la clase `BertSummarizer`, la cual encapsula el modelo de resumen basado en BERT.  
  - Mantiene **alta cohesión**, ya que su única responsabilidad es la generación de resúmenes.  
  - **Bajo acoplamiento**, porque no depende de otros módulos internos, lo que facilita modificaciones sin afectar otras partes del código.  

</details>

<details>
  <summary>🧪 <strong>test_summarizer.py (tests/)</strong></summary>

  - Implementa **pruebas unitarias** con `pytest` para validar que el modelo funciona correctamente.  
  - Se realizan  dos pruebas:
  
   ✅ 1. **Prueba de Generación de Resumen**
        Verificar que el modelo genera un resumen **sin errores** y que el resumen es **más corto** que el texto original. 

   ✅ 2. **Prueba de Guardado del Modelo**
        Verificar que el modelo puede ser **guardado correctamente** en un archivo.

</details>

<details>
  <summary>📝 <strong>example.py</strong></summary>

  - Es un **script de demostración** que permite probar el modelo con distintos textos.  
  - Se puede ejecutar desde la terminal y muestra cómo generar un resumen.  

</details>

---

## 🚀 **Cómo ejecutar el proyecto**

### 1️⃣ **Construir la imagen Docker**
Antes de ejecutar el proyecto, construye la imagen con:

```bash
docker build -t auto_summarizer .

```
### 2️⃣ **Ejecutar en modo interactivo**
Por temas de optimizacion de recursos se recomienda ejecutar comandos dentro del contenedor, ingresando en modo interactivo:

```bash
docker run -it auto_summarizer /bin/bash
```

### 3️⃣ **Ejecutar las pruebas**
Para la ejecucion del test_summarizer.py dentro del contenedor interactivo, se debe:

```bash
pytest -v tests/
```
### 4️⃣ **Ejecutar el script de muestra**
Para la ejecucion del example.py dentro del contenedor interactivo, primero debes ingresar el texto en ingles que quieres resumir y ajustar los parametros de caracteres minimos y maximos antes de hacer la construccion de la imagen de docker, luego debes ejecutar el siguiente comando:

```bash
python example.py
```

### 5️⃣ **Salir del contenedor después de ejecutar los tests**

```bash
exit
```

📩 Contacto
Si tienes dudas o sugerencias, no dudes en contribuir al proyecto o contactarnos.

📌 Jose Israel Perez 📌 Diego Juvinao 📌 Leidy Correa

🚀 ¡Espero que este proyecto sea útil para ti! 🚀

