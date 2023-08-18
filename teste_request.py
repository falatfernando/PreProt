import requests

def get_protein_function(uniprot_id):
    base_url = "https://www.uniprot.org/uniprot/"
    params = {
        "format": "tab",
        "columns": "function",
    }

    response = requests.get(f"{base_url}{uniprot_id}.txt", params=params)
    
    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        if len(lines) > 1:
            return lines[47]  # The second line contains the function information
    else:
        return "Error: Unable to retrieve protein function."

# Replace "P12345" with the UniProt ID of the protein you're interested in
protein_id = "BTUC_ECOBW"
protein_function = get_protein_function(protein_id)

print("Protein Function:", protein_function)