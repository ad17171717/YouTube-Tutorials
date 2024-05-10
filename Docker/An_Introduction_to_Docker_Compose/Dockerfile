FROM jupyter/base-notebook:latest

#use root to install packages
USER root

#copy requirements.txt file into the image
COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER jovyan