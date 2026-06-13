from data_loader import load_data

def main():

    df = load_data("data/raw/train.csv")

    print("Dataset loaded successfully!")
    print(df.shape)
    print(df.head())
    print(df.info())

if __name__ == "__main__":
    main()