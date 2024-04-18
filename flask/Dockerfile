FROM python:3.9.19-bullseye
#RUN apt-get update && apt-get upgrade -y
#RUN apt-get install build-essential -y \
#&& apt-get install pkg-config -y \
#&& apt-get install python-dev -y \
#&& apt-get install python3-pip -y \
#&& apt-get install default-libmysqlclient-dev -y
RUN pip3 install --upgrade pip 
RUN pip install flask flask-mysqldb mysql-connector-python
RUN mkdir -p /srv/templates
COPY accueil.html /srv/templates
COPY inscription.html /srv/templates
COPY connexion.html /srv/templates
COPY app.py /srv
CMD ["flask","--app","/srv/app","run","--host=0.0.0.0"]
