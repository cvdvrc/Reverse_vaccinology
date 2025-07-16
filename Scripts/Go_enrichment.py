#!/usr/bin/env python3

##############################################################
## The following script retrieves and prints out
## significantly enriched (FDR < 1%) GO Processes
## for the given set of proteins. 
##
## Requires requests module:
## type "python -m pip install requests" in command line (win)
## or terminal (mac/linux) to install the module
##############################################################

import requests ## python -m pip install requests 
import json
import argparse


parser = argparse.ArgumentParser(description="Download genomic or proteic sequences")
parser.add_argument("-g", "--gene_list",help="Gene list")
parser.add_argument("-r", "--fdr_rate", help="False discovery rate cut-off")
parser.add_argument("-f", "--format", help="Output format")
parser.add_argument("-m", "--method", help="Enrichment method") 
parser.add_argument("-s", "--species", help="")
args = parser.parse_args()

string_api_url = "https://version-12-0.string-db.org/api"
output_format = "json"
method = "enrichment"


##
## Construct the request
##

request_url = "/".join([string_api_url, output_format, method])

##
## Set parameters
##
with open(args.gene_list, 'r') as file:
    my_genes = list(file)

params = {

    "identifiers" : "%0d".join(my_genes), # your protein
    "species" : 60711 # NCB9606/STRING taxon identifier 

}

##
## Call STRING
##

response = requests.post(request_url, data=params)

##
## Read and parse the results
##

data = json.loads(response.text)

for row in data:

    term = row["term"]
    preferred_names = ",".join(row["preferredNames"])
    fdr = float(row["fdr"])
    description = row["description"]
    category = row["category"]
    tax_ID = str(row["ncbiTaxonId"])

    if category == "Process" and fdr < 0.05:

        ## print significant GO Process annotations

        print("\t".join([term, tax_ID, category, preferred_names, str(fdr), description]))
