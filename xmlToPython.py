import xml.etree.ElementTree as ET
import json
from colorama import init, Fore

# Inicializamos Colorama
init(autoreset=True)

# Leemos el archivo xml
with open('incidenciasGrupo2.xml', encoding='utf-8') as f:
    contenidoForm = f.read()

# Parseamos el siguiente código
try:
    root = ET.fromstring(contenidoForm)
    # Usamos la variable keep para que se inicialice el bucle cuando se inicia el código por primera vez o cuando el usuario especifique
    # más adelante que quiere seguir
    keep = str('S')
    while keep.upper() == 'S':
        # Preguntamos al usuario si quiere filtrar por año o mostrar todas las incidencias
        year_user = input("Ingresa el año de la incidencia (Formato: YYYY) o escribe 'todas' para ver todas las incidencias: ")

        # Lista para almacenar las incidencias y después generarlas en el json
        lista_incidencias = []

        # Mostramos información del usuario por cada incidencia que haya en el xml
        for incidencia in root.iter('incidencia'):
            usuario = incidencia.find('usuario')
            mail = usuario.find('mail').text.strip()
            protDatos = usuario.find('protDatos').text.strip()
            nombre = usuario.find('nombre').text.strip()

            # Mostramos información del problema por cada incidencia que haya en el xml
            problema = incidencia.find('problema')
            aula = problema.find('aula').text.strip()
            fecha = problema.find('fecha').text.strip()
            id_ = problema.find('id').text.strip()
            tipoP = problema.find('tipoP').text.strip()
            descripcion = problema.find('descripción').text.strip()
            urgencia = problema.find('urgencia').text.strip()
            propuesta = problema.find('propuesta').text.strip() if problema.find('propuesta').text is not None else 'No se especifica.'

            # Creamos la variable year para que recoja el año de la variable fecha y creamos una condición para filtrar por año o mostrar todas
            year = fecha[-4:]
            if year == year_user or year_user.lower() == 'todas':
                # Imprimimos toda la información
                print(Fore.RED + "-" * 85 + "\n" + "-" * 85)
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
                print(Fore.RED + "-" * 85 + "\n" + "-" * 85 + "\n \n")

                # Agregamos la incidencia a la lista
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

        # Verificamos si hay incidencias para guardar
        if lista_incidencias:
            # Guardamos la lista de incidencias como JSON (se genererá el archivo cuando se termine el programa)
            with open('incidencias.json', 'w', encoding='utf-8') as jsonF:
                json.dump(lista_incidencias, jsonF, ensure_ascii=False, indent=4)

        else:
            # No guardamos datos si no hay incidencias en el año ingresado
            print(Fore.YELLOW + "No se han encontrado incidencias en ese año. No se guardaron datos.")
        while True:
            #Preguntamos al usuario si quiere volver a ejecutar el código con otro año o finalizar el programa
            keep = input("¿Quieres buscar incidencias de otros años? (S/N) ")
            if keep.upper() == 'S':
                break
            if keep.upper() == 'N':
                if lista_incidencias:
                    print(Fore.CYAN + "Datos guardados en 'incidencias.json'.")
                    break
                break
            else:
                print('Tienes que escribir "S" o "N".')

# Mostramos mensaje de error si ocurre algún problema con el xml
except ET.ParseError as e:
    print(f"Error al analizar el XML: {e}")