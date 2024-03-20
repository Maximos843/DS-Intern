import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor, Pool
from features import preprocess_cat_features, scaling_and_correlation, split_data
from config import Variables
from sklearn.metrics import mean_absolute_error


def train_model(train_pool: Pool, eval_pool: Pool) -> float:
    params = {'depth': 9,
              'random_seed': 1,
              'l2_leaf_reg': 1.5,
              'iterations': 800,
              'cat_features': Variables.CATEGORIAL_COLUMNS,
              'verbose': True,
              'early_stopping_rounds': 150
        }
    model = CatBoostRegressor(**params)
    model.fit(train_pool, eval_pool)
    model.save_model('/app/model/model.cbm')
    return mean_absolute_error(y_eval, model.predict(X_eval))


if __name__ == '__main__':
    train = pd.read_csv('/app/data/prepared_train.csv')
    features = pd.read_csv('/app/data/features.csv')
    train = preprocess_cat_features(train)
    train = scaling_and_correlation(train, features)
    X, y = split_data(train)
    X_train, X_eval, y_train, y_eval = train_test_split(
        X, y, train_size=0.9, random_state=42, shuffle=True
    )
    train_pool = Pool(X_train, label=y_train, cat_features=Variables.CATEGORIAL_COLUMNS)
    eval_pool = Pool(X_eval, label=y_eval, cat_features=Variables.CATEGORIAL_COLUMNS)
    print(train_model(train_pool, eval_pool))
