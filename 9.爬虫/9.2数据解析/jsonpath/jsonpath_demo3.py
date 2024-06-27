import requests
import json
from jsonpath import jsonpath


url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

response = requests.get(url, headers=headers)

data_dict = json.loads(response.text)['content']['data']

# 打印所有的城市名
print(jsonpath(data_dict, '$.allCitySearchLabels.*.*.name'))
print('-' * 40)

# 找到所有以G开头的城市名
print(jsonpath(data_dict, '$.allCitySearchLabels.G.*.name'))
print('-' * 40)

# 找到id 等于666的城市名
print(jsonpath(data_dict, '$.allCitySearchLabels.*[?(@.id==666)].name'))
print('-' * 40)
