def create_time_features(df):

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek

    df["lag_1"] = df["sales"].shift(1)
    df["lag_7"] = df["sales"].shift(7)
    df["lag_30"] = df["sales"].shift(30)


    df["rolling_mean_7"] = df["sales"].rolling(window=7).mean()
    df["rolling_mean_30"] = df["sales"].rolling(window=30).mean()

    df = df.dropna()
    df =  df.reset_index(drop=True)


    return df