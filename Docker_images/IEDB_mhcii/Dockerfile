#Maintainer: Aminata NDIAYE
#Docker image for IApred
#Webpage: https://github.com/sebamiles/IAPred/blob/main/
#Building: docker build -t amynjaaye/iapred:1.0. .
#Stages to use this image
#1. Pull: docker pull amynjaaye/iapred:1.0.
#2. Running virtually on local machine: docker run -v local_directory_to_mount:/directory_mounted -it amynjaaye/iapred:1.0.0 bash

#Base image
FROM debian

#Install dependencies 
RUN apt-get update && apt-get install -yf git python3-pip wget tcsh gawk perl python3-setuptools python3-distutils

RUN wget https://downloads.iedb.org/tools/mhcii/LATEST/IEDB_MHC_II-3.1.12.tar.gz
RUN tar --extract --file=IEDB_MHC_II-3.1.12.tar.gz --gzip --verbose
WORKDIR mhc_ii
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ./configure.py
RUN true
