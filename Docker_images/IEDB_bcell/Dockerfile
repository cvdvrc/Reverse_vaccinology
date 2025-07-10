#Maintainer: Aminata NDIAYE
#Docker image for IEDB bcell
#Webpage: https://downloads.iedb.org/tools/bcell/LATEST/README.txt
#Building: docker build -t amynjaaye/iedb_bcell:3.1. .
#Stages to use this image
#1. Pull: docker pull amynjaaye/iedb_bcell:3.1.
#2. Running virtually on local machine: docker run -v local_directory_to_mount:/directory_mounted -it amynjaaye/iedb_bcell:3.1 bash

#Base image
FROM debian

#Install dependencies 
RUN apt-get update && apt-get install -yf curl wget tcsh gawk build-essential checkinstall libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

#Install python 3.6.2
RUN wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
RUN tar xvf Python-3.6.2.tar.xz
WORKDIR Python-3.6.2/ 
RUN ./configure 
RUN make -j8 build_all
RUN make -j8 altinstall

#RUN python3.6 -m pip install pip==21.2
#RUN python3.6 -m pip install numpy==1.16.6 matplotlib==2.0.0

#Download and install IEDB bcell tool
RUN wget https://downloads.iedb.org/tools/bcell/LATEST/IEDB_BCell-3.1.tar.gz -O ./IEDB_BCell-3.1.tar.gz
RUN tar --extract --file=./IEDB_BCell-3.1.tar.gz --gzip --verbose
WORKDIR bcell_standalone
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ./configure
RUN true
