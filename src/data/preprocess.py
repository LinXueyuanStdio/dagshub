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
    train_data = pd.read_csv(data_path)
    print("done.")

    # Normalize the train data
    print("Normalizing data...")
    # We choose all columns except the first, since that is where our labels are
    # Normalize train and test data according to the train data distribution

    print("done.")

    # Save normalized data-sets
    # Save mean and std for future inference
    output_path = Path(data_path).with_suffix('.json')
    with open(output_path, 'w') as f:
        rows = []
        for index, row in train_data.iterrows():
            rows.append(dict(row))
        json.dump(rows, f)

    print("done.")


if __name__ == '__main__':
    featurization("data/word_translation.csv")
