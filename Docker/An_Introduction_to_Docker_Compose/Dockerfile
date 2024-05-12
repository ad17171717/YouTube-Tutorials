FROM jupyter/base-notebook:latest

#copy requirements.txt file into the image
COPY requirements.txt /tmp/

#install the necessary python packages
RUN pip install --no-cache-dir -r /tmp/requirements.txt