# ldap3py

Crear imagen:

~~~
$ docker build -t "ldap3py" .
~~~

Correr contenedor:

~~~
$ docker run -t -i --rm ldap3py:latest bash
~~~

Autenticación Active Directory:

https://ldap3.readthedocs.io/tutorial_intro.html#logging-into-the-server

Argumentos requeridos para correr script:

servername=servername

user=Domain\\\User

password=password

correr script:

~~~
$ python ldap3_authentication.py servername=servername user=Domain\\\User password=password
~~~
