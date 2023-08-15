import pandoc

def convert_document(input_file, output_format):
    try:
        # Leer el contenido del archivo de entrada
        with open(input_file, 'r') as f:
            content = f.read()

        # Crear un documento Pandoc a partir del contenido
        doc = pandoc.read(content)

        # Establecer el formato de salida
        doc.format = output_format

        # Obtener el texto convertido
        converted_text = pandoc.write(doc)

        # Escribir el texto convertido en el archivo de salida
        output_file = f"{input_file}.{output_format}"
        with open(output_file, 'w') as f:
            f.write(converted_text)

        print(f"El archivo se ha convertido a formato {output_format} con éxito.")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")
