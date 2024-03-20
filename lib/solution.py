import pandas as pd
import numpy as np
from features import preprocess_cat_features, scaling_and_correlation
from catboost import CatBoostRegressor


def predict(test: pd.DataFrame) -> np.array:
    model = CatBoostRegressor()
    model.load_model("/app/model/model.cbm")
    preds = model.predict(test)
    return preds


if __name__ == '__main__':
    test = pd.read_csv('/app/data/prepared_test.csv')
    features = pd.read_csv('/app/data/features.csv')
    submission = pd.read_csv('/app/data/submission_sample.csv')
    test.drop(columns=['id'], inplace=True)
    test = preprocess_cat_features(test)
    test = scaling_and_correlation(test, features, is_train=False)
    submission['score'] = predict(test)
    submission.to_csv('/app/data/final_submission.csv', index=False)
