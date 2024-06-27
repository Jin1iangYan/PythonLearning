# cookie 保持登陆状态，访问需要登陆才能访问的页面
import requests

url = 'https://github.com/JinliangYan'

# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

# 构造cookies字典
cookie_str = r'_octo=GH1.1.1723371117.1718355506; _device_id=469b3c9e06ed5f3dd330f31615b49263; saved_user_sessions=52315768%3AGhb-df4uKKs2R13aFm4Km_p2VeBuiJkrlj_BTp4zzFaqk1NC; user_session=Ghb-df4uKKs2R13aFm4Km_p2VeBuiJkrlj_BTp4zzFaqk1NC; __Host-user_session_same_site=Ghb-df4uKKs2R13aFm4Km_p2VeBuiJkrlj_BTp4zzFaqk1NC; logged_in=yes; dotcom_user=JinliangYan; fileTreeExpanded=true; has_recent_activity=1; preferred_color_mode=dark; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; _gh_sess=pwWYuaVuvFMfxl7lfL4oY489RtRV5nXIiWk35xK4%2F7SST3gj%2F5evsGAjpXLV%2F%2BZJQu5C2NxtzyKkwizb5s7n73HfWD1MTOYimbZSyM11QeiufVEhdJ%2FTH6BWki4Das0RLRgzK%2FNCqEl1skohWOvyVbWEkeYOS7t7QPdiECixu7vOYEai6DqsZ3g9Y3POGbxoVro1cEG09Hw23SvCgYVBkJ8Z7jcgnztLY92qgL968PpDI%2FETChSKGp%2FR0QmduOqGDRUb1xmEVhVSbmEoR7hLyDM2WXsrpkQUo4ylDaYW12wTPqSP9ouKSSeEstM%2Fmamc0Hgz3eMosN6nDgi4aCrpLg96TdhvQG0nS%2Fwh7w%3D%3D--8KOWNjFGnaVRhYU2--kLJ%2BvhXcAHt8kOVuT2CWbQ%3D%3D'
cookie_dict = dict(cookie.split('=', 1) for cookie in cookie_str.split('; '))

# 请求头参数字典中携带cookie字符串
resp = requests.get(url, headers=headers, cookies=cookie_dict)

with open('github_profile.html', 'wb') as f:
    f.write(resp.content)
