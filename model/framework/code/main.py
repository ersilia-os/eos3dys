# imports
import csv
import os
import sys
import numpy as np
from rdkit import Chem

from ersilia_pack_utils.core import read_smiles, write_out
from lazyqsar.api.classifier_predict import predict

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# each run_columns.csv name is also the name of its checkpoint folder
columns_file = os.path.abspath(os.path.join(root, "..", "columns", "run_columns.csv"))
with open(columns_file) as f:
    header = [row["name"] for row in csv.DictReader(f)]
model_dir = {name: os.path.join(checkpoints, name) for name in header}


# my model
def my_model(smiles_list):
    # only parseable molecules go to lazyqsar; the rest are returned as NaN
    valid = [i for i, smi in enumerate(smiles_list) if Chem.MolFromSmiles(smi) is not None]
    outputs = np.full((len(smiles_list), len(header)), np.nan)
    if valid:
        # a single call so descriptors are computed once and shared across tasks
        R, cols = predict(model_dir, smiles=[smiles_list[i] for i in valid], predict_type="rank")
        outputs[valid] = R[:, [cols.index(name) for name in header]]
    return outputs


# read SMILES from .csv file, assuming one column with header
_, smiles_list = read_smiles(input_file)

# run model
outputs = my_model(smiles_list)

# check input and output have the same length
assert len(smiles_list) == len(outputs)

# write output in a .csv file
write_out(outputs, header, output_file, np.float32)
