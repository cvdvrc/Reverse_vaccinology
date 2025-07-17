#Maintainer: Aminata NDIAYE
#Docker image for phobius
#Webpage: https://phobius.sbc.su.se/instructions.html
#Building: docker build -t amynjaaye/phobius:1.0.0 .
#Stages to use this image
#1. Pull: docker pull amynjaaye/phobius:1.0.0
#2. Running virtually on local machine: docker run -v local_directory_to_mount:/directory_mounted -it amynjaaye/phobius:1.0.0 bash

#Base image
FROM debian

#Install dependencies 
RUN apt-get update && apt-get install perl -yf

#Get tool directory
COPY phobius /usr/local/share/phobius 
RUN ln -s /usr/local/share/phobius/phobius.pl /usr/local/bin/phobius

