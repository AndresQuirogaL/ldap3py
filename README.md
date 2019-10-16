# ldap3py

Crear imagen:

~~~
$ docker build -t "ldap3py" .
~~~

Correr contenedor:

~~~
$ docker run -t -i --rm ldap3py:latest bash
~~~


**Script 1 ( NTLM v2 protocol)**

Autenticación Active Directory:

https://ldap3.readthedocs.io/tutorial_intro.html#logging-into-the-server

Argumentos requeridos para correr script:

servername = servername

user = Domain\\\User

password = password

correr script:

~~~
$ python ldap3_authentication.py servername='servername' user='Domain\\User' password='password'
~~~


**Script 2**

Argumentos requeridos para correr script:

address = address

dn = dn (Distinguished Name ej: 'cn=read-only-admin,dc=example,dc=com')

password=password

correr script:

~~~
$ python ldap3_dn.py address='address' dn='dn' password='password'
~~~
