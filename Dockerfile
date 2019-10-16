FROM python:3.6.5
ARG DJANGO_ENV

ADD ldap3_authentication.py /app/ldap3_authentication.py
ADD ldap3_dn.py /app/ldap3_dn.py

# Asignamos el directorio de trabajo
WORKDIR /app/

# Install Python requirements.
RUN pip install --upgrade pip; \
	pip install ldap3

# Create user without privilegies.
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
