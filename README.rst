Leer tickets desde API
================

Leer tickets en Github a través de la API.

Ejecutar
================
Desde la Terminal:
	``$ python tribus-issues.py``

Exportar a un Archivo:
	``$ python tribus-issues.py > lista.rst``

Al exportar el resultado a un archivo, este produce el siguiente error:
*UnicodeEncodeError: 'ascii' codec can't encode character u'\xed'*, utilice el
siguiente comando para solucionarlo:
	``$ export PYTHONIOENCODING=utf-8``


