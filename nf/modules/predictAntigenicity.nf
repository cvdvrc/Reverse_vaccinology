process ANTIGEN {

    tag "$mhc1_peptides"

    input:
    path mhc1_peptides

    output:
    path "antigenicity_scores.tsv", emit: out

    script:
    """
    python3 /usr/bin/IApred $mhc1_peptides antigenicity_scores.tsv
    """
}

