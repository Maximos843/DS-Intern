from geopy.geocoders import ArcGIS
from geopy.distance import geodesic
import numpy as np
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.impute import KNNImputer
import pickle
from utils import splitting_by_popularity, get_city_population, get_data
from config import Variables


def add_base_features(df: pd.DataFrame, features: pd.DataFrame) -> pd.DataFrame:
    '''
    Adding features from the features file to the dataset as an average of the indicators
    of the 5 nearest objects on the map.
    '''
    top5_nearest = []
    ind = 0
    for elem in tqdm(df.values):
        nearest_obj = []
        for obj in features.values:
            distance = geodesic((elem[1], elem[2]), (obj[0], obj[1])).kilometers
            nearest_obj.append((obj, distance))
        nearest_obj.sort(key=lambda x: x[1])
        top5_nearest = [i[0][2:-1] for i in nearest_obj[:5]]
        feats = np.array(top5_nearest).mean(axis=0)
        for j in range(len(feats)):
            df.loc[ind, f'feature_{j}'] = feats[j]
        ind += 1
    return df


def add_categories(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Extraction of additional features - city, population, type of object and district.
    '''
    ind = 0
    dct = get_data()
    geolocator_arcgis = ArcGIS()
    for elem in tqdm(df.values):
        location = geolocator_arcgis.reverse((elem[1], elem[2]), exactly_one=True).raw
        df.loc[ind, 'population'] = get_city_population(dct, location['City'])
        ind += 1
        try:
            df.loc[ind, 'territory'] = location['Territory']
            df.loc[ind, 'city'] = location['City']
            df.loc[ind, 'type'] = location['Type']
        except:
            continue
        ind += 1
    df.loc[df.population == 0, 'population'] = df.population.median()
    return df


def preprocess_cat_features(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Converting categorical variables to a numerical format.
    Next, restore the missing values using KNNImputer.
    '''
    df['city_category'] = df['city'].map(
        {Variables.UNIQUE_CITIES[i]: i for i in range(len(Variables.UNIQUE_CITIES))}
        )
    df['territory_category'] = df['territory'].map(
        {Variables.UNIQUE_TERRITORIES[i]: i for i in range(len(Variables.UNIQUE_TERRITORIES))}
        )
    df['type_category'] = df['type'].map(
        {Variables.UNIQUE_TYPES[i]: i for i in range(len(Variables.UNIQUE_TYPES))}
        )
    df['population_category'] = df.apply(splitting_by_popularity, axis=1)
    df.drop(columns=['city', 'territory', 'type', 'population'], inplace=True)
    cols = df.columns
    imputer = KNNImputer(n_neighbors=7)
    df_new = imputer.fit_transform(df)
    df_new = pd.DataFrame(df_new, columns=cols)
    return df_new


def split_data(df: pd.DataFrame) -> tuple[pd.DataFrame]:
    return df.drop(columns=['score', 'id']), df['score']


def scaling_and_correlation(df: pd.DataFrame, features: pd.DataFrame, is_train: bool = True) -> pd.DataFrame:
    '''
    Data normalization and removal of highly correlated features.
    '''
    corr_matrix = features.drop(columns=['lat', 'lon']).corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    feats_high_corr = ['feature_' + column for column in upper.columns if any(upper[column] > 0.9)]
    df.drop(columns=feats_high_corr, inplace=True)

    cols = df.columns
    inds = [col for col in range(2, len(cols)) if cols[col] not in Variables.CATEGORIAL_COLUMNS]
    if is_train:
        scaler = StandardScaler()
        df.iloc[:, inds] = scaler.fit_transform(df.iloc[:, inds])
        with open('/app/model/scaler_config.pkl', 'wb') as file:
            pickle.dump(scaler, file)
    else:
        with open('/app/model/scaler_config.pkl', 'rb') as file:
            scaler = pickle.load(file)
        df.iloc[:, inds] = scaler.transform(df.iloc[:, inds])
    df = pd.DataFrame(df, columns=cols)
    for i in Variables.CATEGORIAL_COLUMNS:
        df[i] = df[i].astype(int)
    return df
