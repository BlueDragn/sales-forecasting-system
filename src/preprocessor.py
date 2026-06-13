import pandas as pd

def preprocessor_data(df):

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    df = df.reset_index(drop=True)

    return df