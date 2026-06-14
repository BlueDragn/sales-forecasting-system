from data_loader import load_data
from feature_engineering import create_time_features
from predictor import generate_predictions
from preprocessor import preprocessor_data
from model_trainer import train_model
from evaluator import evaluate_model

def main():

    df = load_data("data/raw/train.csv")
    df = preprocessor_data(df)
    df = create_time_features(df)

    model, X_train, X_test, y_train, y_test = train_model(df)

    print("Training completed!")

    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)


    predictions = generate_predictions(model, X_test)

    mae, rmse, r2 = evaluate_model(y_test, predictions)

    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2:", r2)





if __name__ == "__main__":
    main()