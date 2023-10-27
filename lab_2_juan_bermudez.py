from fuctions_lab2 import read_file, get_frame_sync, get_channel_information, write_file
""" 
1. Lea el archivo FlujoE1.txt en el ambiente de trabajo/desarrollo que prefiera. Debe
crear una variable denominada “FlujoE1” que contenga la secuencia binaria que
contiene el archivo, correspondiente a un flujo E1.
"""
flujoE1 = read_file("flujoE1.txt")
"""
2. Desarrolle un script que realice la sincronización de trama sobre la secuencia binaria
“FlujoE1”, teniendo en cuenta la estructura estándar de PCM Europeo y...
"""
FAS = "0011011"
frame_sync_index = get_frame_sync(text=flujoE1, frame_sync=FAS)

"""
3. El mismo script desarrollado en el punto anterior, debe permitir recuperar cualquier
canal del Flujo E1. Asuma que por dichos canales se transmite texto codificado en
ASCII y recupere al azar algunos de los canales del flujo. 
¿Observa algo particular?
¿Qué encontró?
R / Se observa que el texto recuperado no tiene sentido, esto se debe a que 
por este canal no se esta mandando como tal información que se pueda decodificar como ASCII con sentido.
"""
channel_information = get_channel_information(
    text=flujoE1, channel=11, frame_sync_index=frame_sync_index
)
print(f"El texto encontrado del canal al azar es: {channel_information}")

"""
4. En realidad, el único canal por el cual se está transmitiendo texto inteligible es el
Canal 13. Recupere la información de dicho canal y guarde el resultado en un
archivo .TXT. 
¿Qué encontró? R/ Se encontró un texto
¿Es legible e inteligible el texto recuperado? R/ Si, es legible e inteligible dado que se puede leer y al leerse este tiene sentido.
¿Qué texto es? R/ Cuerpo de mujer, de Pablo Neruda
"""
channel_information = get_channel_information(
    text=flujoE1, channel=13, frame_sync_index=frame_sync_index
)
write_file(output_file_name="decoded_text.txt", text_to_write=channel_information)

"""
5. Intencionalmente, introduzca un error de sincronización temporal igual a un bit y
recupere nuevamente la información del Canal 13. 
¿Qué encontró? ¿Es legible e inteligible el texto recuperado?
R/ Se evidencia que el texto recuperado no es legible ni inteligible, esto se debe a que 
al introducir un error de sincronización temporal se pierde la sincronización de la trama 
y por ende la información que se recupera no tiene sentido.
"""
FAS = "0011111" # Se cambia el FAS para que se encuentre un error de sincronización temporal
frame_sync_index = get_frame_sync(text=flujoE1, frame_sync=FAS)
channel_information = get_channel_information(
    text=flujoE1, channel=13, frame_sync_index=frame_sync_index
)
write_file(output_file_name="decoded_text_with_fast_error.txt", text_to_write=channel_information)

"""
6. Si la información transmitida a través del Flujo E1 fuera audio, ¿qué más debería
haber tenido en cuenta para la recuperación del audio que va por el Canal 13?
R / Se debe tener en cuenta que el audio se transmite en un formato de datos distinto, se debe considerar 
tambien que el ancho de banda para transmitir audio es mayor que el ancho de banda para transmitir texto ya
que este requiere una tasa de muestreo mucho más alta, adicionalemnte, y finalmente, para recuperar el audio
podría hacerse uso de métodos como la transformada de Fourier para analizar la señal y extraer las
frecuencias adecuadas, junto con algunos filtros para poder obtener un audio de calidad adecuado. 
"""