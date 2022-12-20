# -*- coding: utf-8 -*-

import pandas as pd
import pubchempy as pcp


compounds = ['alanine','asparagine','aspartate','N-acetylalanine','2-aminobutyrate','creatine','creatinine','2-hydroxybutyrate','cysteine','methionine','glutamate']

for compound in compounds:
    c = pcp.get_compounds(compound, 'name')
    print(compound, '-->', c[0].isomeric_smiles)
    

#get it into a dataframe.     
import pandas as pd
import pubchempy as pcp
  
smiles = []

compounds = ["alanine", "asparagine", "aspartate", "N-acetylalanine", "2-aminobutyrate", "creatine", "creatinine", "2-hydroxybutyrate", "cysteine", "methionine", "glutamate"]

for compound in compounds:
    smiles.append(pcp.get_compounds(compound, 'name')[0].isomeric_smiles)

df = pd.DataFrame({"Compound": compounds, "Smiles": smiles})
print(df)
