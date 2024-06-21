"""
Create feature CSVs for train and test datasets
"""
import json
import numpy as np
import pandas as pd
from pathlib import Path

def featurization(data_path):
    # Load data-sets
    print("Loading data sets...")
    train_data = pd.read_csv(data_path, header=None, dtype=float)
    print("done.")

    # Normalize the train data
    print("Normalizing data...")
    # We choose all columns except the first, since that is where our labels are
    # Normalize train and test data according to the train data distribution

    print("done.")

    print("Saving processed datasets and normalization parameters...")
    # Save normalized data-sets
    # Save mean and std for future inference
    output_path = Path(data_path).with_suffix('.json')
    with open(output_path, 'w') as f:
        json.dump(train_data.to_records(), f)

    print("done.")


if __name__ == '__main__':
    featurization()
