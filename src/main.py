from data_loader import load_data
from preprocessor import preprocessor_data

def main():

    df = load_data("data/raw/train.csv")

    print("Dataset loaded successfully!")
    print(df.shape)
    print(df.head())
    print(df.info())

    df = preprocessor_data(df)
    print("Data preprocessing completed!")
    print(df.head())
    print(df.dtypes)

if __name__ == "__main__":
    main()