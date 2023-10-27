# Sincronización de Trama

Este script de Python decodifica información de un canal específico en un archivo de texto utilizando una sincronización de trama predefinida.

## Requisitos

* Python 3.x
* `functions_lab2.py`

## Uso

1. Coloque el archivo de texto que desea decodificar en la misma carpeta que `lab_2_juan_bermudez.py`.
2. Abra `lab_2_juan_bermudez.py` en un editor de texto o IDE.
3. En la línea 5, reemplace `"flujoE1.txt"` con el nombre del archivo de texto que desea decodificar.
4. En la línea 6, reemplace `"0011011"` con la sincronización de trama que se utiliza en el archivo de texto.
5. En la línea 8, ajuste los parámetros de la función `get_channel_information` **según sea necesario**. El primer parámetro es el texto que se decodificará, el segundo parámetro es el número del canal que se desea obtener (0-31) y el tercer parámetro es el índice donde se encuentra la sincronización de trama en el texto.
6. Ejecute el script. El resultado se escribirá en un archivo llamado `decoded_text.txt` en la misma carpeta que `lab_2_juan_bermudez.py`.

## Créditos

Este script fue desarrollado por [Juan Bermudez](https://github.com/juan154850/ "Juan B") y utiliza las siguientes funciones definidas en `functions_lab2.py`:

* `read_file`
* `get_frame_sync`
* `get_channel_information`
* `write_file`
