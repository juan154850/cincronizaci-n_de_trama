import numpy as np


def read_file(file_name: str) -> str:
    """
    Lee el contenido de un archivo de texto y lo devuelve como una cadena.

    Args:
        file_name (str): El nombre del archivo a leer.

    Returns:
        str: El contenido del archivo como una cadena.
    """
    with open(file_name, "r") as file:
        return file.read()


def validate_sequence(text: str, index: int) -> bool:
    """
    Valida si una secuencia de texto cumple con ciertas condiciones.

    Args:
        text (str): El texto a validar.
        index (int): El índice de inicio de la secuencia a validar.

    Returns:
        bool: True si la secuencia cumple con las condiciones, False de lo contrario.
    """
    if (
        text[index + 1 : index + 8] == text[index + 513 : index + 520]
        and text[index + 1 : index + 8] == text[index + 1025 : index + 1032]
        and text[index + 1 : index + 8] == text[index + 1537 : index + 1544]
    ):
        return True
    else:
        return False


def get_frame_sync(text: str, frame_sync: str) -> int:
    """
    Busca la sincronización de trama en un texto y devuelve su índice.

    Args:
        text (str): El texto en el que se buscará la sincronización de trama.
        frame_sync (str): La secuencia de bits que representa la sincronización de trama.

    Returns:
        int: El índice donde se encuentra la sincronización de trama en el texto.
    """
    # Convertimos el texto en una lista de bits
    text = list(text)
    index_frame_sync = 0

    # Iteramos la lista de bits para encontrar la sincronización de trama
    for i in range(len(text) - 1):
        # Validamos si el bit i+1 corresponde a frame_sync[0]
        if text[i + 1 : i + 8] == list(frame_sync):
            if validate_sequence(text=text, index=i):
                # Se tiene en cuenta que si bien la comparación se hace desde i+1, el canal empieza en i
                index_frame_sync = i
                break
    return index_frame_sync

def convert_channel_information_to_ascii(channel_information: list) -> str:
    """
    Convierte una lista de bits en un string de caracteres ASCII.

    Args:
        channel_information (list): La lista de bits a convertir.

    Returns:
        str: El string resultante con los caracteres ASCII correspondientes.
    """
    # Inicializamos una variable para almacenar el resultado
    result = ""

    # Iteramos sobre la lista en incrementos de 8
    for i in range(0, len(channel_information), 8):
        # Convertimos los 8 bits en un número entero y luego en un carácter ASCII
        ascii_char = chr(int("".join(channel_information[i:i+8]), 2))
        # Concatenamos el carácter al resultado
        result += ascii_char

    return result

def get_channel_information(text: str, channel: int, frame_sync_index: int) -> list:
    """
    Obtiene la información del canal especificado en un texto.

    Args:
        text (str): El texto del que se extraerá la información del canal.
        channel (int): El número del canal que se desea obtener (0-31).
        frame_sync_index (int): El índice donde se encuentra la sincronización de trama en el texto.

    Returns:
        list: Una lista de bits que representa la información del canal especificado.
    """
    # Inicializamos una lista para almacenar la información del canal
    channel_information = []

    # Convertimos el texto en una lista de bits a partir del índice de sincronización de trama
    text = list(text[frame_sync_index:])

    # Iteramos sobre el texto en incrementos de 256 bits (32 bytes) para obtener la información del canal
    for i in range(channel * 8, len(text), 256):
        # Validamos si hay suficientes bits para obtener 8 bits de información del canal
        if i + 8 <= len(text):
            # Agregamos los 8 bits de información del canal a la lista
            channel_information.append(text[i : i + 8])

    # Convertimos la lista de bits en un string de caracteres ASCII y lo devolvemos
    channel_information = np.array(channel_information).ravel().tolist()
    return convert_channel_information_to_ascii(channel_information)

def write_file(output_file_name:str, text_to_write:str):
    """
    Escribe el contenido de una variable string en un archivo de texto codificado como UTF-8

    Args:
        output_file_name (str): El nombre del archivo que contendrá el texto
        text_to_write (str): El texto a escribir en el archivo
    Returns:
        str: El archivo de texto codificado en UTF-8
    """
    with open(output_file_name, "w", encoding='utf-8') as file:
        return file.write(text_to_write)