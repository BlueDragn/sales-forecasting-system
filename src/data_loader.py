import pandas as pd

def load_data(file_path):

    #load dataset from csv file
    df = pd.read_csv(file_path)

    # Validation Checks
    if df.empty:
        raise ValueError("The dataset is empty. Please provide a valid dataset.")

    required_columns = ["date", "store", "item", "sales"]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns]
    if missing_columns:
        raise ValueError(
            f"Missing columns in the dataset: {missing_columns}"
            )

    return df


