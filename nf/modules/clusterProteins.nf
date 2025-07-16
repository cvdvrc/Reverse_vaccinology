process CLUSTER {

    tag "$input_fasta"

    input:
    path input_fasta
    val identity

    output:
    path "clustered.faa", emit: out
    path "clustered.faa.clstr"

    script:
    """
    cd-hit -i $input_fasta -o clustered.faa -c $identity -n 5
    """
}

