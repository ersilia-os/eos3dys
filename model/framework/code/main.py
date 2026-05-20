# imports
import csv
import os
import sys
import numpy as np

from ersilia_pack_utils.core import read_smiles, write_out
from lazyqsar.api.classifier_predict import predict

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# read SMILES from .csv file, assuming one column with header
_, smiles_list = read_smiles(input_file)

# build ordered model dict from run_columns.csv
columns_file = os.path.abspath(os.path.join(root, "..", "columns", "run_columns.csv"))
with open(columns_file) as f:
    reader = csv.DictReader(f)
    model_dir = {row["name"]: os.path.join(checkpoints, row["name"]) for row in reader}

# run model
outputs, header = predict(model_dir, smiles=smiles_list, predict_type="rank")

# check input and output have the same length
assert len(smiles_list) == len(outputs)

# write output in a .csv file
write_out(outputs, header, output_file, np.float32)
