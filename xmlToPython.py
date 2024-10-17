#b

import xml.etree.ElementTree as ET

# Leer el archivo y reemplazar entidades problemáticas
with open('formularioIncidenciasGrupo2.xml', 'r', encoding='utf-8') as f:
    contenido = f.read()
    contenido = contenido.replace('&', '&amp;')  # Escapar &

# Parsear el contenido modificado
try:
    root = ET.fromstring(contenido)


    def mostrar_xml(elemento, nivel=0):
        indentacion = ' ' * (nivel * 2)
        print(f"{indentacion}<{elemento.tag}>")
        if elemento.text and elemento.text.strip():
            print(f"{indentacion}  {elemento.text.strip()}")
        for hijo in elemento:
            mostrar_xml(hijo, nivel + 1)
        print(f"{indentacion}</{elemento.tag}>")



    mostrar_xml(root)
except ET.ParseError as e:
    print(f"Error al analizar el XML: {e}")