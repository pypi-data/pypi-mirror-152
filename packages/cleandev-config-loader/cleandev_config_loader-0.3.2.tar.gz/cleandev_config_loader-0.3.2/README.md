# Properties Loader V 0.3.1 Beta

Esta libreria ofrece una forma facil para cargar archivo de propiedades y usarlo para configurar partes del proyecto
de una forma dinamica y limpia.

# Env vars

| Variables de entorno    | Valores                                          | Descripción                                                                                                                                |
|-------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ROO_PATH                | /xxx/xxx/xxx                                     | Ruta completa de la raiz del proyecto                                                                                                      |
| CONFIG_FILE             | relative path to config file                     | Ruta relativa del fichero de configuración tomando como base la raiz del proyecto                                                          | 

![esquema_clases](docs/diagram_class.png)

# Introduccion:
A continuacion se mostraran el uso de cada clase de esta libreria para que puedas sacarle el maximo partido de una 
forma simple.  

Existen 3 clases y a continuación explicaremos como se usan cada una de ellas.

Todos los ejemplos aqui mencionados van a ser sobre el archivo de ejemplo [properties.ini](properties.ini)
y la ruta raiz de mi proyecto es: "/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader"

## LoadConfig
La clase "LoadConfig" es la encargada de gestionar el orden de prioridad para ubicar el archivo de configuración que
pueden ser de 3 formas.
* Por parametros
* Por variables de entorno
* Por defecto  
---


Este metodo posee una propiedad "path_properties" que retorna la ruta absoluta del archivo de propiedades que se ha
encontrado.


---
### Parametros (root_path, path_file)
La clase "LoadConfig" puede recibir 2 parametros "root_path" y "path_file"
* root_path:
  Se ha de proporcionar la ruta raiz del proyecto.
* path_file: 
  Se ha de proporcionar la ruta relativa a partir de la ruta raiz del proyecto.

#### Ejemplo

```python
from properties_loader import LoadConfigImpl

if __name__ == '__main__':
    load_config: LoadConfigImpl = LoadConfigImpl(
        root_path='/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader',
        path_file='properties.ini'
    )
    print(load_config.path_properties)
```
```
/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader/properties.ini
```

### Variables de entorno
Se pueden definir la ruta raiz "root_path" y la ruta relativa "path_file" mediante las variables de entorno
respectivas.

* ROOT_PATH
* CONFIG_FILE
#### NOTA:
Asegurate de que las variables de entorno esta bien asignadas antes de ejecutar el siguiente ejemplo.

```python
from properties_loader import LoadConfigImpl

if __name__ == '__main__':
    load_config: LoadConfigImpl = LoadConfigImpl()
    print(load_config.path_properties)
```
```
/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader/properties.ini
```

### Valor por defecto
Este caso solo va a funcionar siempre y cuando el archivo de python que es ejecutado esta a la misma altura que el fichero 
"properties.ini"

```python
from properties_loader import LoadConfigImpl

if __name__ == '__main__':
    load_config: LoadConfigImpl = LoadConfigImpl()
    print(load_config.path_properties)
```
```
/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader/properties.ini
```

### Error
En caso de error mostrara un mensaje indicando cual fue la ruta en la que fue a buscar el archivo
y no lo encontro
```
...
properties_loader.exceptions.PropertiesNotFoundError: Error al cargar el archivo de properties -> /home/daniel/Proyectos/CLEANDEV/04-scm/config-loader/properties.ini
```

## Properties
Esta clase hereda de "LoadConfig" por lo que incluye todo lo anterior. Es decir que el control
de la busqueda del archivo de propiedades se aplica a este de la misma forma.  
Posee los mismos parametros para su configuración que el anterior caso y unicamente se mostrara un ejemplo
de lo nuevo que se añade.

```python
from properties_loader import PropertiesImpl

if __name__ == '__main__':
  properties: PropertiesImpl = PropertiesImpl(
    root_path='/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader',
    path_file='properties.ini'
  )
  print(properties.__dict__)
```
```
{'INFO': {'version': '0.1.0', 'name_module': 'config_reader', 'author': 'Daniel Rodriguez Rodriguez', 'enviroment': 'development'}, 'OTHERS': {'url': 'https://gitlab.com/cleansoftware/libs/public/config_reader', 'bug_tracker': 'https://gitlab.com/cleansoftware/libs/public/config_reader/-/issues', 'python_version': '>3.9'}}
```

## PropertiesClassLoader
En esta ocacion pese a que esta clase hereda de "Properties" tiene otro objetivo particular.  

Su objetivo es cargar las propiedades como atributo de la clase hija que herede de esta, veamoslo
con un ejemplo.

```python
from properties_loader import PropertiesClassLoader


class AutoLoad(PropertiesClassLoader):
    pass


if __name__ == '__main__':
    auto_load: AutoLoad = AutoLoad()
    print(auto_load._INFO)
    print(auto_load._OTHERS)
    print(auto_load._INFO['version'])
```
```
{'version': '0.1.0', 'name_module': 'config_reader', 'author': 'Daniel Rodriguez Rodriguez', 'enviroment': 'development'}
{'url': 'https://gitlab.com/cleansoftware/libs/public/config_reader', 'bug_tracker': 'https://gitlab.com/cleansoftware/libs/public/config_reader/-/issues', 'python_version': '>3.9'}
0.1.0

```

#### Nota

---
Como se puede observar el archivo de ejemplo tiene como grupos "INFO" y "OTHERS"
Autoload que hereda de la clase "PropertiesClassLoader" automaticamente tiene como atributos
el nombre de los grupos con el prefijo "_" es decir "_INFO" y "_OTHERS".  

Estos parametros son del tipo dict y en su interior poseen toda la información de ese grupo de propiedades

---

### Filtro
Dado que esta clase añade atributos de forma automatica posee un filtro para agregar unicamente
aquellos grupos que se deseen cargar.

```python
from properties_loader import PropertiesClassLoader


class AutoLoad(PropertiesClassLoader):

    def __init__(self):
        super(AutoLoad, self).__init__(groups=['INFO'])


if __name__ == '__main__':
    auto_load: AutoLoad = AutoLoad()
    print(auto_load._INFO)
    # La siguiente linea arrojara un error
    print(auto_load._OTHERS)

```
```
{'version': '0.1.0', 'name_module': 'config_reader', 'author': 'Daniel Rodriguez Rodriguez', 'enviroment': 'development'}
Traceback (most recent call last):
  File "/home/daniel/Proyectos/CLEANDEV/04-scm/config-loader/main.py", line 14, in <module>
    print(auto_load._OTHERS)
AttributeError: 'AutoLoad' object has no attribute '_OTHERS'
```