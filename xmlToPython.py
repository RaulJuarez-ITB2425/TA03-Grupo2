import xml.etree.ElementTree as eT
import json
import datetime

# Leer el archivo y reemplazar entidades problemáticas
with open('formularioIncidenciasGrupo2.xml') as f:
    contenidoForm = f.read()

# Lista para almacenar las incidencias en un array
lista_incidencias = []

# Parsear el siguiente código
try:
    root = eT.fromstring(contenidoForm)


    def convertir_fecha(fecha_usu):
        return datetime.strptime(fecha_usu, '%d/%m/%Y')

    fecha_inicio_usu = input("Ingresa la fecha de inicio (DD-MM-YYYY): ")
    fecha_fin_usu = input("Ingresa la fecha de fin (DD-MM-YYYY): ")

    # Mostrar información del usuario por cada incidencia que haya en el xml
    for incidencia in root.iter('incidencia'):
        usuario = incidencia.find('usuario')
        mail = usuario.find('mail').text.strip()
        protDatos = usuario.find('protDatos').text.strip()
        nombre = usuario.find('nombre').text.strip()

    # Mostrar información del problema por cada incidencia que haya en el xml
        problema = incidencia.find('problema')
        aula = problema.find('aula').text.strip()
        fecha_usu = problema.find('fecha').text.strip()
        fecha = convertir_fecha(fecha_usu)
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

        # Agregar la incidencia a la lista
        lista_incidencias.append({
            'usuario': {
                'nombre': nombre,
                'mail': mail,
                'protDatos': protDatos
            },
            'problema': {
                'id': id_,
                'aula': aula,
                'fecha': fecha,
                'tipoP': tipoP,
                'descripcion': descripcion,
                'urgencia': urgencia,
                'propuesta': propuesta
            }
        })

    # Guardar la lista de incidencias como JSON
    with open('incidencias.json', 'w') as jsonF:
        json.dump(lista_incidencias, jsonF, ensure_ascii=False, indent=4)

    print(f"\nDatos guardados en 'incidencias.json'.")

except eT.ParseError as e:
    print(f"Error al analizar el XML: {e}")