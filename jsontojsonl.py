import json

def normalize_bbox(bbox, width, height):
    """Normaliza las coordenadas del bounding box y las multiplica por 1000."""
    x1, y1, w, h = bbox
    x2 = x1 + w
    y2 = y1 + h
    # Normalización y conversión a enteros entre 0 y 999
    x1n = int((x1 / width) * 1000)
    y1n = int((y1 / height) * 1000)
    x2n = int((x2 / width) * 1000)
    y2n = int((y2 / height) * 1000)
    return f"<loc_{x1n}><loc_{y1n}><loc_{x2n}><loc_{y2n}>"

def process_annotations(coco_data):
    # Crear un diccionario para almacenar anotaciones por imagen
    annotations_by_image = {img['id']: [] for img in coco_data['images']}
    
    # Mapear anotaciones a imágenes correspondientes
    for ann in coco_data['annotations']:
        image_id = ann['image_id']
        annotations_by_image[image_id].append(ann)
    
    jsonl_data = []

    for image in coco_data['images']:
        image_id = image['id']
        width = image['width']
        height = image['height']
        file_name = image['file_name']
        
        annotation_text = ""
        
        if image_id in annotations_by_image:
            for ann in annotations_by_image[image_id]:
                category_id = ann['category_id']
                bbox = ann['bbox']
                loc_text = normalize_bbox(bbox, width, height)
                
                # Determinar la clase basada en el category_id
                if category_id == 1:
                    annotation_text += f"bem{loc_text}"
                elif category_id == 2:
                    annotation_text += f"ripio{loc_text}"
                elif category_id == 3:
                    annotation_text += f"tranque{loc_text}"
                # Agregar más categorías si es necesario
                
        jsonl_data.append({
            "image": file_name.split("/")[-1],  # Tomamos solo el nombre del archivo
            "prefix": "<OD>",
            "suffix": annotation_text
        })

    # Ordenar por el nombre del archivo de la imagen
    jsonl_data_sorted = sorted(jsonl_data, key=lambda x: x['image'])

    return jsonl_data_sorted

def save_to_jsonl(data, output_file):
    with open(output_file, 'w') as f:
        for item in data:
            json.dump(item, f)
            f.write('\n')

# Leer archivo COCO y procesar anotaciones

with open('/data/gabriel_hermosilla/patricio/florencia2/dataset/Test/annotations.coco.json', 'r') as f:
    coco_data = json.load(f)

jsonl_data_sorted = process_annotations(coco_data)

# Guardar el resultado en un archivo JSONL ordenado
save_to_jsonl(jsonl_data_sorted, '/data/gabriel_hermosilla/patricio/florencia2/dataset/Test/result.jsonl')

print("Archivo JSONL generado y ordenado correctamente.")
