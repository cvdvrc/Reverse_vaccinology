#Maintainer: Aminata NDIAYE
#Docker image for BPGA
#Webpage: https://master.dl.sourceforge.net/project/bpgatool/BPGA%20User%20Manual.pdf?viasf=1
#Building: docker build -t bpga:1.3 .
#Stages to use this image
#1. Pull: docker pull amynjaaye/bpga:1.3
#2. Running virtually on local machine: docker run -v local_directory_to_mount:/directory_mounted -it amynjaaye/bpga:1.3 bash

#Base image
FROM debian

#Install dependencies 
RUN apt-get update && apt-get install -yf build-essential wget tar \
					libz-dev cpanminus gnuplot \
					ghostscript wine wget curl pkg-config libx11-dev
###Copy binaries
RUN wget https://sourceforge.net/projects/bpgatool/files/BPGA-1.3-linux-x86_64-0-0-0.tar.gz/download -P . 
WORKDIR . 
RUN tar --extract --file=download --gzip --verbose 
RUN chmod +x BPGA-1.3-linux-x86_64-0-0-0/BPGA-Version-1.3/bin/*
RUN cp BPGA-1.3-linux-x86_64-0-0-0/BPGA-Version-1.3/bin/* /usr/bin

#Copy USEARCH programs
COPY usearch11.0.667_i86linux32 /usr/bin/
