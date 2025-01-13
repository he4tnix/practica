# README

En este repositorio se encuentran los códigos utilizados en la práctica, además del informe realizado. A continuación, se proporciona una breve descripción de cada archivo incluido:

## Archivos

### **`TestingFlorence2.ipynb`**

Este notebook está diseñado para realizar inferencias utilizando el modelo Florence2. Permite poner a prueba todas las tareas indicadas en los diferentes modelos disponibles: **Base**, **Large** y con pesos **Fine-Tuned**.  

Las tareas se especifican en el parámetro de entrada `"<task>"` y se dividen en dos categorías:  

1. **Tareas con salida en texto**  
   - `<CAPTION>`: Genera una descripción básica de la imagen de entrada.  
   - `<DETAILED_CAPTION>`: Proporciona una descripción más detallada de la imagen.  
   - `<MORE_DETAILED_CAPTION>`: Ofrece una descripción aún más detallada de la imagen.  
   - `<REGION_TO_DESCRIPTION>`: Describe una región específica de la imagen.  

2. **Tareas con salida en región**  
   - `<OD>`: Detección de objetos.  
   - `<REGION_PROPOSAL>`: Propone una región de interés en la imagen.  
   - `<DENSE_REGION_CAPTION>`: Detecta objetos con etiquetas más detalladas.  
   - `<CAPTION_TO_PHRASE_GROUNDING>`: Detección de objetos basada en un contexto textual.  
   - `<REFERRING_EXPRESSION_SEGMENTATION>`: Realiza segmentación semántica.  
   - `<REGION_TO_SEGMENTATION>`: Segmenta una región previamente definida.  
   - `<OCR_WITH_REGION>`: Detecta, identifica y etiqueta texto dentro de una imagen.  
   - `<OPEN_VOCABULARY_DETECTION>`: Detección de objetos con un vocabulario amplio.  

En las tareas que requieren un contexto adicional o la definición de una región, el prompt de texto debe proporcionarse en el parámetro `"<text>"`.

---

### **`FineOwnData.ipynb`**

Este notebook permite realizar el fine-tuning del modelo Florence2 utilizando un dataset personalizado.  
- **Entrada**: Dataset y archivo de anotaciones en formato JSONL.  
- **Método**: Se utiliza **LoRa** para realizar cuantización, optimizando el uso de recursos durante el entrenamiento.  
- **Salida**: Pesos ajustados, que se guardan en una ubicación personalizada definida por el usuario.

---

### **`jsontojsonl.py`**

Script que convierte anotaciones en formato JSON (como las de COCO) al formato JSONL, comúnmente utilizado en aplicaciones de **LLM** y **VLM**.

---



