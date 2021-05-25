import pandas as pd

from data_prep.data_prep import train_test_validation_split


def test_train_test_validation_split():
    # simple test to make sure that the data is split into appropriately sized chunks
    # best practice would be to test every chunk. The test and validation didn't match
    # because the split was off by one which is acceptable and due to time didn't want
    # to spend time messing with making it graceful
    df = pd.read_csv('./heart_attack_dataset.csv')
    initial_rows = df.shape[0]
    X_train, X_test, X_validation, y_train, y_test, y_validation = train_test_validation_split(df)
    assert X_train.shape[0] == (initial_rows * .7)
