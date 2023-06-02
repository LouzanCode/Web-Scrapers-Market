OBJETIVO DEL PROYECTO:

Simular una empresa de servicios técnológicos, en este caso, un sitio web donde la empresa vende software como web scrapers con el objetivo de automatizar tareas web repetitivas.
A parte de la web, mostrar el funcionamiento del webscraping con selenium

STACK TECNOLÓGICO:
- Django
- Selenium
- Sqlite
- Ajax

BASE DE DATOS:

En el caso de Django, tiene muchas funcionalidades por default que nos agilizan el trabajo. La base de datos es definida por el archivo models.py de cada aplicación del proyecto, 
en este archivo, se definen las clases u objetos de los elementos de la base de datos como los productos por ejemplo, luego en alrchivo admin.py registramos los modelos para poder manipularlos en la interfaz de admin.
Django nos ofrece unos models de usuario predeterminados que más adelante mostraremos. Una vez creado los models, para migrarlos a la base de datos se utilizará los comandos migrate y makemigrations, ejecutamos la aplicación e introducimos en la url de la web '/admin' (habrá que crear el superuser previamente),
esto es la gran ventaja de django, una interfaz para el admin donde se puede gestionar la base de datos muy cómodamente.
 
![admin_iniciar](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/admin_iniciar.PNG)
![admin_panel](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/admin_panel.PNG)
![store](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/store_products.PNG)
![products](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/porducto_admin.PNG)

Una vez llegados aquí, podemos añadir, eliminar y editar cada elemento. En el caso de los usuarios se puede añadir o quitar permisos de una manera muy práctica.

APLICACIÓN:
Página principal:

![main](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/menu_principal.PNG)
 
Hacemos click en iniciar sesíon que se encuentra el panel principal y nos lleva al login.

![login](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/login.PNG)

Clicamos en registrarse aquí o en registrarse al lado del carrito, y registramos un usuario que a continuacíon mostraremos en la base de datos.

![registrarse](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/register.PNG)
 
Al clicar registrar nos redirecciona a la página principal, ahora volvamos a la interfaz de admin y vemos como queda registrado el nuevo usuario.

![admin_users](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/admin_users.PNG)
 
Iniciamos sesíon con el usuario recién creado y volvemos a la página principal, en este caso el panel principal cambia ya que el usuario ha iniciado sesíon.

![log](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/menu_log.PNG)
 
Vamos ahora con las categorías, donde se muestran las categorías de manera dinamica en el template.


![categories](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/categories.PNG)
 
Clicamos en una de ellas y nos lleva al template de lista de categoría.
 
Ahora, veamos la ´pagina del producto, hacemos click en uno de los productos.
 
![producto](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/producto.PNG)

Añadimos el producto al carrito y clicamos en carrito en la parte superior a la derecha para ver el template de carrito.


![carrito](https://github.com/LouzanCode/Web-Scrapers-Market/blob/main/imag/carrito.PNG)
 
En el caso de la aplicación del carrito, no usamos el models.py sino que creamos un archivo carrito.py donde declaramos la clase carrito. No queremos registrar el carrito en la base de datos, sino crear una sesíon del usuario cada vez que abra el carrito. En los templates utilizamos AJAX (Asynchronous JavaScript and XML), AJAX es el arte de intercambiar datos con un servidor y actualizar partes de una página web, sin recargar toda la página.

INSTALACIÓN:
Para empezar, iniciaremos el proyecto django en el terminal, con el siguiente comando: django-admin startproject projectname.
Se crearán una carpeta y  el archivo manage.py, esta carpeta, en mi caso la llamo core, es donde se configura y enlaza todas las distintas aplicaciones del proyecto y base de datos, tocaremos dos archivos del core principalmente, el settings.py y el urls.py. El archivo manage.py lo llamaremos desde el terminal cada vez que queramos realizar una acción como crear una app o hacer migraciones.
En settings.py es donde se registran las diferentes aplicaciones, base de datos (ya viene definida por default) y más conceptos. En urls.py se registran las diferentes urls de cada apliacíon que queremos mostrar en nuestra web.
Empezamos por crear la primera aplicación, en mi caso será la tienda, introducimos en el terminal en el mismo nivel que el archivo manage.py el siguiente comando: py manage.py startapp tienda.
Se creará una carpeta y tendrá dos archivos que trabajaremos, models.py y views.py. En el archivo views es donde definimos las funcionalidades de la web, renderizando los templates con el contexto adecuado.
En la carpeta de la app crearemos un archivo urls.py para especificar las urls de nuestras vistas, que se enlazan al archivo urls.py del core.
También crearemos un archivo llamado context_processors.py, su funcíon es tener acceso a un contexto desde cualquier template sin necesidad de declarlo en la funcíon del views.py.
A continuación para registrar las apps, vamos al settings.py y en el modulo de INSTALLED APPS introducimos el nombre de la app, lo mismo con el context processors, en el mudulo TEMPLATES context processors introducimos nombreapp.context­­_processors.clase.
Volvamos a los models, en nuestro caso creamos las clases categorias y productos, una vez creados vamos al terminal e introducimos lo siguiente: py manage.py migrate. Si todo es correcto volvemos al terminal y tecleamos: py manage.py makemigrations, se creará la base de datos. Volvemos al terminal e introducimos: py manage.py createsuperuser, lo creamos y ya tenemos acceso al administrador de django.
Respecto los models de usuario utilizaremos django.contrib.auth.urls donde vienen predefinidos.
Para el diseño, utilizaremos bootstrap, css y javascript, los cuales indicaremos el path en el base.html. 
Respecto la media, indicamos en el settings.py una MEDIA_URL y MEDIA_ROOT, y lo declaramos en el urls.py del core. Con esto definimos una carpeta en el backend donde se alamacenará todas las imágenes o videos que contenga la web.
Para instalar los componentes vamos al terminal e introducimos pip install -r requirements.txt.

CONCLUSÓN:
Utilicé todas las ventajas por default para enseñar mejor las capacidades del framework, lo más importante del proyecto son los scrapers ya que lo he ido moldeano y son muy sostenibles.
Cosas a mejorar, el diseño se puede mejorar mucho, crear unos modelos de usuario que aumenten la seguridad ,añadir app de ordenes y pagos, añadir permisos de usuario que puedan subir sus productos al sitioweb y añadir blog o foro.

 
