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
RUN sed -i "s,    test(),#    test()," configure.py
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ./configure.py
RUN ln -s /mhc_ii/mhc_II_binding.py /usr/bin/mhc_II_binding
#RUN true
RUN sed -i 's,my \$PLATFORM = \$ENV{'\''NetMHCIIpanPLAT'\''},my \$PLATFORM = "/mhc_ii/methods/netmhciipan-4.1-executable/netmhciipan_4_1_executable/Linux_x86_64/",' \
    /mhc_ii/methods/netmhciipan-4.1-executable/netmhciipan_4_1_executable/NetMHCIIpan-4.1.pl
RUN dpkg --add-architecture amd64
RUN apt update
RUN apt install -yf binutils:amd64
