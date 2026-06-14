from data_loader import load_data
from preprocessor import preprocessor_data

def main():

    df = load_data("data/raw/train.csv")

    print("Dataset loaded successfully!")
    print(df.shape)
    print(df.head())


    df = preprocessor_data(df)
    print("Data preprocessing completed!")

    print(df.shape)
    print(df["store"].unique())
    print(df["item"].unique())
    
    print(df.head())

if __name__ == "__main__":
    main()