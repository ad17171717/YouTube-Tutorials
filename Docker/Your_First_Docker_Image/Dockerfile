#build Python 3.12.2 Debian based OS
FROM python:3.12.2-slim-bookworm

#set the working directory
WORKDIR /usr/src/app

#copy all files/directories in current directory into the container
COPY . .

#run the python script
CMD ["python","./sqroot.py"]
