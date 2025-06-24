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
RUN apt-get update && apt-get install -yf git python3-pip 

RUN git clone https://github.com/sebamiles/IApred.git
WORKDIR /IApred

#RUN pip install -r requirements.txt --break-system-packages
RUN pip install numpy==1.26.4 biopython scikit-learn==1.5.2 joblib imbalanced-learn==0.13.0 scipy seaborn==0.13.2 matplotlib --break-system-packages
#Compiling C-programs
#RUN make && make install

#Display help information
#RUN cd-hit --help
