
import json
import requests # pyright: ignore
from supp.config import shards 


def get_by_genre(genre):
    '''
    Get films by genre
    '''
    
    response = requests.get(
        f'{shards[0]["address"]}', params = {'_page': 1, '_limit': 3}
    )
    return (len(response.json()), response.text)



def get_by_director(director):
    '''
    Get films by director
    '''
    
    response = requests.get(
        f'{shards[0]["address"]}', params = {'_page': 1, '_limit': 3}
    )
    return (len(response.json()), response.text)
