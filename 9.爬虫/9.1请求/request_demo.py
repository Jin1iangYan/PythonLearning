import requests
from requests.cookies import RequestsCookieJar

# 设置请求头，包含自定义的 User-Agent 和携带 cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Cookie': 'name=value; name2=value2'
}

# 设置请求参数
params = {
    'param1': 'value1',
    'param2': 'value2'
}

# 创建一个 RequestsCookieJar 对象，并添加 cookie
cookie_jar = RequestsCookieJar()
# 向 RequestsCookieJar 对象中添加一个名为 name3，值为 value3 的 cookie，并指定该 cookie 的域名和路径。
cookie_jar.set('name3', 'value3', domain='https://httpbin.org/', path='/')
# 设置超时参数，单位是秒
timeout = 5

# 设置代理 IP 参数
proxies = {
    'http': 'http://127.0.0.1:7897',
    'https': 'http://127.0.0.1:7897',
}

# 发送一个 GET 请求，忽略 CA 证书验证
response_get = requests.get('https://httpbin.org/get', headers=headers, params=params, cookies=cookie_jar, timeout=timeout, proxies=proxies, verify=False)

# 打印响应内容
print(response_get.text)

# 发送一个 POST 请求
data = {
    'key1': 'value1',
    'key2': 'value2'
}
response_post = requests.post('https://httpbin.org/post', headers=headers, data=data, cookies=cookie_jar, timeout=timeout, proxies=proxies, verify=False)

# 打印响应内容
print(response_post.text)

# 使用 requests.session 进行状态保持
session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookie_jar)

# 发送一个带状态的 GET 请求
# https://httpbin.org/cookies 这个接口是返回 cookie 数据
response_session_get = session.get('https://httpbin.org/cookies')
# 这样写不返回 cookie 因为根本没有使用 session 的状态保持
# response_session_get = requests.get('https://httpbin.org/cookies')
print(response_session_get.text)

# 发送一个带状态的 POST 请求
response_session_post = session.post('https://httpbin.org/post', data=data)
print(response_session_post.text)

# 将结果写入文件
with open('./result.txt', 'w', encoding='utf-8') as f:
    f.write('# 发送一个 GET 请求，忽略 CA 证书验证\n')
    f.write(response_get.text)
    f.write('# 发送一个 POST 请求\n')
    f.write(response_post.text)
    f.write('# 发送一个带状态的 GET 请求\n')
    f.write(response_session_get.text)
    f.write('# 发送一个带状态的 POST 请求\n')
    f.write(response_session_post.text)
