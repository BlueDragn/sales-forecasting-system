import pandas as pd

def preprocessor_data(df):

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    df = df[(df["store"] == 1) & (df["item"] == 1)]

    df = df.reset_index(drop=True)

    return df