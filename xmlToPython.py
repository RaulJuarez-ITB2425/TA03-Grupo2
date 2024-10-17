import xml.etree.ElementTree as ET

# Leer el archivo y reemplazar entidades problemáticas
with open('formularioIncidenciasGrupo2.xml', 'r', encoding='utf-8') as f:
    contenido = f.read()
    contenido = contenido.replace('&', '&amp;')  # Escapar &

# Parsear el contenido modificado
try:
    root = ET.fromstring(contenido)

    # Mostrar información del usuario
    print("Información del Usuario:")
    for usuario in root.iter('usuario'):
        mail = usuario.find('mail').text.strip().replace('"', '') if usuario.find(
            'mail') is not None else 'No disponible'
        protDatos = usuario.find('protDatos').text.strip().replace('"', '') if usuario.find(
            'protDatos') is not None else 'No disponible'
        nombre = usuario.find('nombre').text.strip().replace('"', '') if usuario.find(
            'nombre') is not None else 'No disponible'

    # Mostrar información del problema
    print("\nInformación del Problema:")
    for problema in root.iter('problema'):
        aula = problema.find('aula').text.strip().replace('"', '')
        fecha = problema.find('fecha').text.strip().replace('"', '') if problema.find(
            'fecha') is not None else 'No disponible'
        id_ = problema.find('id').text.strip().replace('"', '') if problema.find('id') is not None else 'No disponible'
        tipoP = problema.find('tipoP').text.strip().replace('"', '') if problema.find(
            'tipoP') is not None else 'No disponible'
        descripcion = problema.find('descripción').text.strip().replace('"', '') if problema.find(
            'descripción') is not None else 'No disponible'
        urgencia = problema.find('urgencia').text.strip().replace('"', '')
        propuesta = problema.find('propuesta').text.strip().replace('"', '') if problema.find(
            'propuesta') is not None else 'No disponible'


#Imprimos toda la informacion
        print("Usuario:")
        print(f"- Nombre: {nombre}")
        print(f"  Mail: {mail}")
        print(f"  Protección de Datos: {protDatos}")
        print("Problema:")
        print(f"- ID: {id_}")
        print(f"  Aula: {aula}")
        print(f"  Fecha: {fecha}")
        print(f"  Tipo de Problema: {tipoP}")
        print(f"  Descripción: {descripcion}")
        print(f"  Urgencia: {urgencia}")
        print(f"  Propuesta: {propuesta}")
        print(" ")
except ET.ParseError as e:
    print(f"Error al analizar el XML: {e}")