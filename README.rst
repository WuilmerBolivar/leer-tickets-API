Leer tickets desde API
================

Leer tickets en Github a través de la API.

Ejecutar
================
Desde la ``Terminal:``
    $ python tribus-issues.py

Exportar a un ``Archivo:``
	$ python tribus-issues.py > lista.rst

Si se produce un error al exportar a un archivo:
*UnicodeEncodeError: 'ascii' codec can't encode character u'\xed'*, utilice:
	$ export PYTHONIOENCODING=utf-8

Para solucionarlo.
