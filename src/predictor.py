def generate_predictions(model, X_test):
    """
    Generate predictions using the trained model and test data.

    Args:
        model: The trained machine learning model.
        X_test: The test features.
    Returns:
        predictions: The predicted values.
    """
    predictions = model.predict(X_test)
    return predictions