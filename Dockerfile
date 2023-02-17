# base image  
FROM python:3.8

# setup environment variable  
ENV DockerHOME=/django-rest  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip

# copy whole project to your docker directory. 
COPY ./web_interface/ $DockerHOME

# copy wallet to your docker directory. 
COPY ./wallet/ /wallet

# copy whole project to your docker directory. 
COPY setup.sh /

# port where the Django app runs  
EXPOSE 8000

# Get update
RUN apt-get update

# install libreoffice
RUN apt-get install libreoffice -y

# install python devs
RUN apt-get install -y python3-dev python3-venv python3-pip systemd supervisor vim nginx alien libaio1 wget 

# get oracle client 
RUN wget https://download.oracle.com/otn_software/linux/instantclient/215000/oracle-instantclient-basic-21.5.0.0.0-1.x86_64.rpm

# install oracle client
RUN alien -i oracle-instantclient-basic-21.5.0.0.0-1.x86_64.rpm

# create env directory 
RUN mkdir -p /django-rest/env

# install venv
RUN  python3 -m venv /django-rest/env

# install reuirements
RUN /django-rest/env/bin/pip install -r /django-rest/requirements.txt

# start server  
ENTRYPOINT ["/setup.sh"]
