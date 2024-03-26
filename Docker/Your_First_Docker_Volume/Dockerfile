#build Python 3.12.2 Debian based OS
FROM python:3.12.2-slim-bookworm

#set the working directory
WORKDIR /usr/src/app

#copy all files in current directory into the container
COPY . .

#install required python modules
RUN pip install -r requirements.txt

#run the python script
CMD ["python","stock_download.py"]