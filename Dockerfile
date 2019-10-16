FROM python:3.6.5
ARG DJANGO_ENV

WORKDIR /app/

# Install Python requirements.
RUN pip install --upgrade pip; \
	pip install ldap3

# Create user without privilegies.
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app

