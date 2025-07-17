#Maintainer: Aminata NDIAYE
#Docker image for CD-HIT Tool
#Webpage: https://github.com/weizhongli/cdhit/releases
#Building: docker build -t cd-hit:4.8.1 .
#Stages to use this image
#1. Pull: docker pull amynjaaye/cd-hit:4.8.1
#2. Running virtually on local machine: docker run -v local_directory_to_mount:/directory_mounted -it amynjaaye/cd-hit:4.8.1 bash

#Base image
FROM debian

#Install dependencies 
RUN apt-get update && apt-get install -yf build-essential libz-dev

#Copy project into container
COPY cdhit-4.8.1 cdhit
WORKDIR /cdhit

#Compiling C-programs
RUN make && make install

#Display help information
#RUN cd-hit --help
