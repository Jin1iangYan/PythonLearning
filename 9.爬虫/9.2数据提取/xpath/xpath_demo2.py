import os
import requests
from lxml import etree

url = 'https://news.sohu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

# request 爬取目标 url 数据
response = requests.get(url, headers=headers)

# xpath  提取 html 中的文字 和图片 的数据
html = etree.HTML(response.text)

imgs = []
text = []

# 找到所有图片和标题

# 左上
left_top_img =  list(map(lambda str: 'https:' + str, html.xpath('//*[@id="block3"]//div[@class="mini-card-content"]//div[@class="container"]/img/@src')))
left_top_text = html.xpath('//*[@id="block3"]//div[@class="mini-card-content"]//div[@class="container"]//div[@class="title-text"]/text()')
# 筛选掉空字符串
left_top_text = [x.strip() for x in left_top_text if not x.isspace()]
# 左下
left_bottom_img =  list(map(lambda str: 'https:' + str, html.xpath('//*[@id="block3"]//div[@class="mini-card-content"]//div[@class="bottomBox"]//img/@src')))
left_bottom_text =  html.xpath('//*[@id="block3"]//div[@class="mini-card-content"]//div[@class="bottomBox"]//div[@class="textBox"]/div/text()')

# 爬取右边热点
right_img = list(map(lambda str: 'https:' + str, html.xpath('//div[@class="HotArticle"]/div[@class="item-wrap"]/div[@class="side_item"]//img/@src')))
right_text = list(html.xpath('//div[@class="HotArticle"]/div[@class="item-wrap"]/div[@class="side_item"]//div[@class="title-text"]/text()'))
right_text = [x.strip() for x in right_text if not x.isspace()] + list(html.xpath('//div[@class="HotArticle"]//div[@class="side_item"]/a/div/div/text()'))

imgs = left_top_img + left_bottom_img + right_img
text = left_top_text + left_bottom_text + right_text

# 保存本地文件
path = './souhu_downloads/'
if (not os.path.exists(path)):
    os.mkdir(path)

for title, img in zip(text, imgs):
    with open(path + title + '.' + img.split('.')[-1], 'wb') as f:
        f.write(requests.get(img, headers=headers).content)
