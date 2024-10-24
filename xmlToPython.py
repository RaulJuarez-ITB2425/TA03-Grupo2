import xml.etree.ElementTree as eT
import json
from colorama import init, Fore, Back, Style

# Inicializar Colorama
init(autoreset=True)

# Leer el archivo y reemplazar entidades problemáticas
with open('formularioIncidenciasGrupo2.xml') as f:
    contenidoForm = f.read()

# Lista para almacenar las incidencias
lista_incidencias = []

# Parsear el siguiente código
try:
    root = eT.fromstring(contenidoForm)

    # Preguntar al usuario si quiere filtrar por año o mostrar todas
    year_user = input("Ingresa el año de la incidencia (Formato: YYYY) o escribe 'todas' para ver todas las incidencias: ")

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
        propuesta = problema.find('propuesta').text.strip() if problema.find('propuesta').text is not None else 'No se especifica.'

        year = fecha[-4:]

        # Condición para filtrar por año o mostrar todas
        if year == year_user or year_user.lower() == 'todas':
            # Imprimir toda la información
            print(Fore.RED + "-" * 85)
            print(Fore.RED + "-" * 85)
            print(Fore.BLUE + "\033[1m- Información del Usuario:\033[0m")
            print(f"  Nombre: {nombre}")
            print(f"  Mail: {mail}")
            print(f"  Protección de Datos: {protDatos}")
            print(Fore.GREEN + "\033[1m- Información del Problema:\033[0m")
            print(f"  ID: {id_}")
            print(f"  Aula: {aula}")
            print(f"  Fecha: {fecha}")
            print(f"  Tipo de Problema: {tipoP}")
            print(f"  Descripción: {descripcion}")
            print(f"  Urgencia: {urgencia}")
            print(f"  Propuesta: {propuesta}")
            print(Fore.RED + "-" * 85)
            print(Fore.RED + "-" * 85)
            print(" ")
            print(" ")

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

    # Verificar si hay incidencias para guardar
    if lista_incidencias:
        # Guardar la lista de incidencias como JSON
        with open('incidencias.json', 'w') as jsonF:
            json.dump(lista_incidencias, jsonF, ensure_ascii=False, indent=4)

        print(Fore.CYAN + "Datos guardados en 'incidencias.json'.")
    else:
        # No se guardan datos si no hay incidencias en el año ingresado
        print(Fore.YELLOW + "No se han encontrado incidencias en ese año. No se guardaron datos.")

except eT.ParseError as e:
    print(f"Error al analizar el XML: {e}")



