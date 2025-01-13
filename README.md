## README
En este repositorio se encuentran los códigos utilizados en la práctica, además del informe realizado.
A continuación una breve descripción de cada código.

#TestingFlorence2.ipynb

Es un código creado para realizar inferencias dentro del modelo Florence2 donde
se ponen a prueba todas las tareas indicadas tanto en el modelo base, Large y pesos FineTuned
Las tareas se definen en la input "<task>" están divididas en dos grupos, existen
las tareas con salida en texto y las que entrega una región de la imagen. 
En caso de ser necesario un prompt de texto adicional a la tarea de entrada
como suele ser en tareas que requieren un contexto o definir una región este debe ser definido en
"<text>".

Las tareas con salida en texto son:

<CAPTION>: Descripción de la imagen de entrada.
<DETAILED_CAPTION>: Una descripción más detallada de la imagen de entrada.
<MORE_DETAILED_CAPTION>: Una descripción aún mas detallada de la imagen de entrada.
<REGION_TO_DESCRIPTION>: Una descripción de una determinada región de la imagen de entrada.

Las tareas con salida en región son:

$<OD>$: Detección de objetos.
$<REGION_PROPOSAL>$: Propone una región de interés en la imagen.
<DENSE_REGION_CAPTION>: Realiza detección de objetos con mayor detalle en sus etiquetas.
<CAPTION_TO_PHRASE_GROUNDING>: Detección de objetos aterrizado por contexto.
<REFERRING_EXPRESSION_SEGMENTATION>: Segmentación semántica.
<REGION_TO_SEGMENTATION>: Se realiza segmentación de una región definida.
<OCR_WITH_REGION>: Detectar, identificar y etiquetar el texto dentro de una imagen.
<OPEN_VOCABULARY_DETECTION>: Detección de objetos enfocado en vocabulario.

#FineOwnData.ipynb

Es un código creado para realizar el fine-tuning de Florence2 utilizando un dataset
personalizado, esto es, cargando el dataset y su respectivo jsonl. Donde, mediante LoRa
se puede hacer una cuantización para la utilización de menos recursos en el entrenamiento.
Finalmente, guardando los pesos obtenidos en una dirección personalizada por el usuario.

#jsontojsonl.py

Es un código encargado de realizar la conversión de datos COCO desde una anotación json
a un formato jsonl comúnmente utilizado en aplicaciones de LLM u VLM.
