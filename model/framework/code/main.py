# imports
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

# run model
outputs, header = predict(checkpoints, smiles=smiles_list, predict_type="rank")

# check input and output have the same length
assert len(smiles_list) == len(outputs)

# write output in a .csv file
write_out(outputs, header, output_file, np.float32)
