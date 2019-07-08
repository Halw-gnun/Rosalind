with open("input/rosalind_mprt.txt") as input_file:
    access_ids = input_file.read().strip("\n").split()

#Returns protein sequence for given ID
def fetch_fasta(uniprot_id):
    import urllib.request
    url = "http://www.uniprot.org/uniprot/" + uniprot_id + ".fasta"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return ''.join(response.read().decode('utf-8').split('\n')[1:])

#Returns possition for all N-glycosylation motifs for given list of ID:s
def nglyco_loactions(access_ids):
    protein_dict = {}
    for protein in access_ids:
        possitions = []
        seq = fetch_fasta(protein)
        for pos in range(len(seq)-3):
            if seq[pos] == "N" and seq[pos+1] != "P" and seq[pos+3] != "P" and (seq[pos+2] == "S" or seq[pos+2] == "T"):
                possitions.append(str(pos+1))
        if len(possitions) > 0:
            protein_dict[protein] = possitions
    return protein_dict

with open("output/locations.txt", "w") as output:
    for key, value in nglyco_loactions(access_ids).items():
        output.write(key + "\n" + " ".join(value) + "\n")           

