from data_loader import load_data
from feature_engineering import create_time_features
from preprocessor import preprocessor_data

def main():

    df = load_data("data/raw/train.csv")
    df = preprocessor_data(df)
    df = create_time_features(df)

    print(df.head())
    print(df.columns)

if __name__ == "__main__":
    main()