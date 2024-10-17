import xml.etree.ElementTree as eT

# Leer el archivo y reemplazar entidades problemáticas
with open('formularioIncidenciasGrupo2.xml', 'r', encoding='utf-8') as f:
    contenido = f.read()

# Parsear el siguiente código
try:
    root = eT.fromstring(contenido)

    # Mostrar información del usuario por cada incidencia que haya en el xml
    for incidencia in root.iter('incidencia'):
        usuario = incidencia.find('usuario')
        mail = usuario.find('mail').text.strip()
        protDatos = usuario.find('protDatos').text.strip()
        nombre = usuario.find('nombre').text.strip()

    # Mostrar información del problema por cada incidencia que haya en el xml
        problema = incidencia.find('problema')
        aula = problema.find('aula').text.strip()
        fecha = problema.find('fecha').text.strip()
        id_ = problema.find('id').text.strip()
        tipoP = problema.find('tipoP').text.strip()
        descripcion = problema.find('descripción').text.strip()
        urgencia = problema.find('urgencia').text.strip()
        #Para la etiqueta propuesta, pedimos que si no encuentra contenido en la palabra propuesta, se indique "No se especifica"
        propuesta = problema.find('propuesta').text.strip() if problema.find('propuesta').text is not None else 'No se especifica.'

#Imprimimos toda la información
        print("\n\033[1m- Información del Usuario.\033[0m")
        print(f"  Nombre: {nombre}")
        print(f"  Mail: {mail}")
        print(f"  Protección de Datos: {protDatos}")
        print("\033[1m- Información del Problema.\033[0m")
        print(f"  ID: {id_}")
        print(f"  Aula: {aula}")
        print(f"  Fecha: {fecha}")
        print(f"  Tipo de Problema: {tipoP}")
        print(f"  Descripción: {descripcion}")
        print(f"  Urgencia: {urgencia}")
        print(f"  Propuesta: {propuesta}")

except eT.ParseError as e:
    print(f"Error al analizar el XML: {e}")