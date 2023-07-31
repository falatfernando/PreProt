import py3Dmol
from stmol import showmol
import requests
import biotite.structure.io as bsio
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import json

#Função pra renderização 3D usando stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb, 'pdb')
    pdbview.setStyle({"cartoon": {'color': 'spectrum'}})
    pdbview.setBackgroundColor('white')
    pdbview.zoomTo()
    pdbview.center()
    pdbview.spin(True)
    
    
    showmol(pdbview, height= 400, width = 800)

# Função que envia a sequência de DNA pra API do ESM Fold
def update(sequence):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
    name = sequence[:3] + sequence[-3:]
    pdb_string = response.content.decode('utf-8')

    with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)

    struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
    b_value = round(struct.b_factor.mean(), 4)

    return pdb_string, b_value

