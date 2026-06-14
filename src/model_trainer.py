import pandas as pd

from sklearn.linear_model import LinearRegression



def train_model(df):

    y = df["sales"]
    X = df.drop(columns=["sales", "date"])

    split_index = int(len(df) * 0.8)
    X_train = X[:split_index]
    X_test = X[split_index:]

    y_train = y[:split_index]
    y_test = y[split_index:]

    model = LinearRegression()
    model.fit(X_train, y_train)


    return(
        model,
        X_train,
        X_test,
        y_train,
        y_test
    )
