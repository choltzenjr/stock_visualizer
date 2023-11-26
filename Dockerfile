# use official python image as base image
FROM python:3.8-slim-buster

# set the working directory in the container to /app
WORKDIR /app

# copy the contents from current directory into container at /app
COPY . /app


RUN pip install --upgrade pip setuptools wheel cython numpy requests


#install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# installing matplotlib
# RUN apk add g++ jpeg-dev zlib-dev libjpeg make
# RUN pip3 install matplotlib

#set the default commands to run when starting the container
CMD ["python", "app.py"]