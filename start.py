import requests 
from pprint import pprint


url = 'https://api-crownx.winmart.vn/it/api/web/v3/item/category'
params = {'orderByDesc': True, 
        'pageNumber': 5, 
        'pageSize': 8, 
        'slug': 'rau-cu-trai-cay--c02', 
        'storeCode': 1535, 
        'storeGroupCode': 1998}

resp = requests.get(url, params=params)
if resp.status_code == 200:
    pprint(resp.json())