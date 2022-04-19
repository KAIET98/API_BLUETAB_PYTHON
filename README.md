# API_BLUETAB_PYTHON
Se quiere aprender a crear una API para poder enpaquetarlo en docker y tal.


# Funcionamiento 

Hay un archivo principal "main.py" donde se ejecutan todas las llamadas a las APIs. Además se ha creado un entorno de Python en el ordenador del curro que las dependencias de esta están especificadas en el requirementes.txt. 


Importante para que corra el script aparte de ejecutar el script con las dependencias del main.py, hay que lanzar en la consola: 

```
uvicorn main:app --reload

```

Luego para entrar en la API hay que darle 

```
control + click
```
sobre el enlace de HTTPS, y añadirle en la cola de la URL un "/docs". 

Si entramos a el enlace + docs nos apareceran todos los elementos publicos en la API. 

Si queremos acceder a uno en concreto en la url, tendremos que pasarle el enlace completo: 

```
http://127.0.0.1:8000/get-iris
```







# Entornos virtuales

La gestión de los entornos virtuales se ha llevado por medio de: https://docs.python.org/es/3/tutorial/venv.html


# Tutorial 

tutorial con conocimientos extendidos del blog de Ander Jauregui: https://anderfernandez.com/blog/como-crear-api-en-python/
