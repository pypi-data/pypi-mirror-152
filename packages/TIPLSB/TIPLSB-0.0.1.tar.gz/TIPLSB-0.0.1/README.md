# TIPLSB: Firmas incrementales en imágenes basado en LSB y funciones HASH

TIPLSB (Trace Image Path with LSB) es un algoritmo el cual permite almacenar en una única imagen un
número finito de firmas, estas firmas denotan las distintas "manos" por las cuales ha
pasado una imagen a lo largo del tiempo.

Las distintas firmas que contiene una imagen se encuentran almacenadas de forma
incremental, permitiendo por tanto obtener el recorrido lineal que ha tenido la imagen.
Este recorrido debe ser algo confidencial, por lo que no
cualquier usuario podrá obtenerlo.

Este algoritmo implementa un método con el cual únicamente aquellos usuarios
que haya realizado una firma en la imagen podrán obtener el recorrido. Este siempre
será de las firmas posteriores a la suya, siendo por tanto el autor original el único que
pueda obtener el recorrido completo.

La realización de este proyecto surge de la asignatura de **Trabajo de Fin de
Grado** para la obtención del título en el grado de **Ingeniería Informática - Tecnologías
Informáticas** en la **Universidad de Sevilla**.

## Autor
* **Bruno González** - [brunogonzalezlla](https://github.com/brunogonzalezlla/)

## Tutores
* **Félix Gudiel**
* **Victor Álvarez**

## Tabla de contenido
  * [Instalación](#Instalacion)
  * [Guía de uso](#Guia)
    * [Clase tiplsb](#Clasetiplsb)
      * [Ejemplo](#ClasetiplsbEjemplo)
    * [Función tip_decode](#Funciontipdecode)
      * [Ejemplo](#FunciontipdecodeEjemplo)
  * [Integración con Django](#Integracion)
    * [views.py](#Views)
    * [urls.py](#Urls)
      

<a name = "Instalacion"></a>
## Instalación
Este proyecto está disponible en [PyPI](https://pypi.org/project/TIPLSB/) y pueden instalarlo con:

    pip install TIPLSB

De manera alternativa, puedes instalarlo directamente del repositorio:

    git clone https://github.com/brunogonzalezlla/TIPLSBlib
    cd TIPLSBlib
    python3 setup.py install


<a name = "Guia"></a>
## Guía de uso

Los dos elementos principales de la libería son los siguiente:

* Clase **tiplsb**: esta es la clase principal de la librería. Mediante ella se realizarán las diferentes firmas en 
las imágenes y permitirá la consulta de los detallen asociados.

* Función **tip_decode** : mediante esta función obtendremos el recorrido (firmas realizadas) en una imagen.

<a name = "Clasetiplsb"></a>
### Clase tiplsb

La clase **tiplsb** está compuesta por los siguiente parámetros de entrada

    tiplsb(path, hash='sha256', version='0.0.1', redundancy=5)

El primer parámetro a establecer en la creación de un objeto de tipo **tiplsb** es _path_, 
en ella estableceremos la ruta de la imagen que queremos utilizar.

Siempre que creemos un objeto del tipo **tiplsb** se comprobará de manera automática
si la imagen introducida ya se encuentra inicializada.

Consideramos que una imagen se encuentra inicializada cuando ya se ha realizado una firma
sobre ella.

Es por ello que la clase podrá recibir como entrada tres parámetros extras, los cuales si
la imagen no se encontrase ya inicializada serían utilizados para su configuración. 
Estos tres parámetros de configuración serían los siguientes:

* **hash**: el algoritmo que realiza las firmas hace uso de una función hash. Por defecto
se usa SHA-256, sin embargo la clase permite la utilización de otras funciones:
  * SHA-1: Se deberá establecer 'sha1'.
  * SHA224: Se deberá establecer 'sha224'.
  * SHA256: Se deberá establecer 'sha256'.
  * SHA-384: Se deberá establecer 'sha384'.
  * SHA-512: Se deberá establecer 'sha512'.
  * SHA-256 (Por defecto): Se deberá establecer 'sha256'.


* **version**: el número de versión utilizado para realizar firmas irá incrustado en la
propia imagen. Debido a los posibles cambios que pueda sufrir la librería se permitirá 
la modificación de este parámetro. Por defecto utilizará la versión más reciente.


* **redundancy**: para evitar posibles perdidas de datos cada vez que se realice
una firma esta será replicada un número _n_ de veces. Mediante el parámetro **redundancy**
podremos establecer esta _n_. Por defecto en esta versión estará inicializado a 5.


Una vez que dispongamos de un objeto creado correctamente podremos realizar las siguientes
acciones:

* objeto.**add(author, platform, date=False)**: este método permitirá realizar una firma
sobre la imagen establecida en la creación del objeto. Recibirá los siguiente parámetros:
  * **author**: Se indicará el nombre, correo, id... del usuario que va a realizar la firma.
  * **platform**: Se indicará la plataforma en la cual se ha realizado la firma.
  * **date**: Por defecto cuando se realiza una firma se establece la fecha actual. Sin embargo
  se permite que establecer una fecha que la sustituya.
  

* objeto.**save(path='')**: una vez que hemos realizado una firma podremos generar la
correspondiente imagen en formato **png**. Por defecto la imagen se generará en la ruta
actual, sin embargo podemos personalizar la ruta estableciendo el parámetro _path_.

<a name = "ClasetiplsbEjemplo"></a>
#### Ejemplo
    
    from TIPLSB import tiplsb 
    
    obj = tiplsb("img/600x600.png")
    obj.add("Hola", "PlataformaMundo")
    obj.save()

<a name = "Funciontipdecode"></a>
### Función tip_decode

La  función **tip_decode** está compuesta por los siguiente parámetros de entrada:

    tip_decode(path_original, path_modified)

Esta función permite obtener el recorrido de la imagen. Para poder obtenerlo será 
necesario disponer de dos imágenes.

La ruta de la imagen que introduciremos en **path_modified** será de la cual
queremos obtener el recorrido.

Para poder obtener este recorrido será necesaria una "llave", esta se tratará de la
imagen introducida en **path_original**. 

Podrá ser la imagen original sin firmas (en caso
de querer obtener el recorrido completo de la imagen) o una copia de la imagen en la cual el
número de firmas totales sea menor al de la imagen introducida en **path_modified** 
(en este caso obtendremos las firmas posteriores a la última de _path_original_)

La función devolverá un diccionario en el cual las claves serán enteros empezando por 0 
que denotarán el orden en el cual se han realizado las firmas. Sus valores asociados
serán las firmas.

    {0: Primera firma, 1: Segunda firma, ...}

<a name = "FunciontipdecodeEjemplo"></a>
#### Ejemplo

    from TIPLSB import tip_decode
    
    dec = tip_decode('img/600x600.png', 'img/600x600_2_firmas.png')
    print(dec)
    > {0: 'TIPLSB|Hola|PlataformaMundo|22:43:21.975652', 1: 'TIPLSB|Bruno|TIPLSBapp|23:15:06.175428'}

<a name = "Integracion"></a>
## Integración con Django
TIPLSB está pensada para ser implementada en plataformas que permitan la compartición
de imágenes. Es por ello que se ha desarrollado un ejemplo de integración con el 
framework web Django.

Una vez implementada la librería, cada vez que una página sea cargada todas las
imágenes que aparezcan contendrán una firma con la información del usuario que la
observa.

La forma en la que se identificarán a los usuarios será elección del propio administrador
del sistema.

<a name = "Views"></a>
### views.py
Debemos añadir una vista nueva la cual será la encargada de devolver las imágenes firmadas.

Añadimos el siguiente extracto:

    from TIPLSB import tiplsb
    from PIL import Image
    from django.http import HttpResponseNotFound, HttpResponse
    from os.path import exists

    ...

    def tiplsb_img(request, path):
        # Comprobamos si la imagen solicitada existe
        if exists("static/"+path):
            obj = tiplsb("static/"+path)

            # Debemos establecer el autor con el cual queremos que se realice la firma.
            # También debemos establecer el nombre de nuestra plataforma.
            obj.add("Identificador", "MiWebDjango")
    
            array = obj.img_array.reshape(obj.height, obj.width, 3)
            image = Image.fromarray(array.astype('uint8'), 'RGB')
    
            response = HttpResponse(content_type='image/png')
    
            image.save(response, "PNG")
            return response
        else:
            return HttpResponseNotFound("Image not found")

Como se explica en los comentarios del extracto de código es necesario que el administrador
establezca un criterio a la hora de establecer el autor de la firma.

Un criterio sencillo para establecer un autor a la hora de firmar es el uso
de la IP del usuario que solicita la imagen. Sin embargo lo más recomendable sería
utilizar identificadores para los cuales únicamente el administrador del sistema sea
capaz de obtener la información relevante.

Otro punto a destacar es que debe existir una carpeta _static_ en la raíz de nuestro
proyecto. En esta carpeta deben ubicarse las imágenes utilizadas en el sitio web. 

    settings.py

    ...

    STATIC_URL = 'static/'

    ...

En caso de disponer de una carpeta con otro nombre bastará con modificar
las siguientes líneas

    if exists("mi_carpeta_de_imagenes/"+path):
            obj = tiplsb("mi_carpeta_de_imagenes/"+path)


<a name = "Urls"></a>
### urls.py
En el archivo _urls.py_ deberemos añadir a la variable _urlpatterns_ la siguiente línea:

    urlpatterns = [
        ...
        path('tiplsb_img/<str:path>', views.tiplsb_img, name='tiplsb'),
        ...
    ]

### Ejemplo
Una vez que hayamos realizado los pasos anteriores correctamente ya podremos hacer uso
de las imágenes ubicadas en _static_:

    <img src="/tiplsb_img/img.png">

## Licencia
Este software tiene licencia MIT.