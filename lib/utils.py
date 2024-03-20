import requests
import json
import numpy as np


def get_data() -> dict:
    '''
    Getting data on the population of Russian cities with opendatasets.
    '''
    tmp1 = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-500/records?select=population%2C%20alternate_names&where=population%20%3E%2060000&limit=100&refine=country%3A%22Russia%22'
    res1 = requests.get(tmp1)
    dct = json.loads(res1.content)['results']
    tmp2 = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-500/records?select=population%2C%20alternate_names&where=population%20%3E%2060000&limit=100&offset=100&refine=country%3A%22Russia%22'
    res2 = requests.get(tmp2)
    dct += json.loads(res2.content)['results']
    tmp3 = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-500/records?select=population%2C%20alternate_names&where=population%20%3E%2060000&limit=100&offset=200&refine=country%3A%22Russia%22'
    res3 = requests.get(tmp3)
    dct += json.loads(res3.content)['results']
    tmp4 = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-500/records?select=population%2C%20alternate_names&where=population%20%3E%2060000&limit=56&offset=300&refine=country%3A%22Russia%22'
    res4 = requests.get(tmp4)
    dct += json.loads(res4.content)['results']
    return dct


def get_city_population(dct: dict, city: str) -> float:
    '''
    Determining the size of a settlement.
    '''
    for i in dct:
        if i['alternate_names'] is not None and city in i['alternate_names']:
            return i['population']
    return 0


def splitting_by_popularity(row: np.array) -> int:
    '''
    Division into groups by population.
    '''
    if row.population <= 100000:
        return 0
    elif row.population > 100000 and row.population <= 500000:
        return 1
    elif row.population > 500000 and row.population <= 1000000:
        return 2
    elif row.population > 1000000:
        return 3
