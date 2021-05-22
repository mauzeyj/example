from sklearn.model_selection import train_test_split


def train_test_validation_split(data):
    """
    wrapper for sklearn train test split that also creates a validation set.
    Build specifically for heart_attack_dataset as it pulls out heart_attack as y
    :param data: pd.DataFrame
    :return:
    """
    #split data into X and y
    y = data['heart_attack']
    data.drop('heart_attack', axis = 1, inplace = True)
    X = data

    # perform split twice to generate both groups needed
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42)
    X_validation, X_test, y_validation, y_test = train_test_split(
        X_test, y_test, test_size=0.50, random_state=42)

    return X_train, X_test, X_validation, y_train, y_test, y_validation

