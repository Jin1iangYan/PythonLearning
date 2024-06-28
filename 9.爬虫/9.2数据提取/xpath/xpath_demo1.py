from lxml import etree

text = '''\
<div>
    <ul>
        <li class="item-1">
            <a href=" ">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a>
        </li>
    </ul>
</div>
'''
# html 数据实例
html = etree.HTML(text)

# 利用xpath 语法 提取数据
# result = html.xpath('xpath 语法字符串')

# 提取 link1.html
result = html.xpath('//li[@class = "item-1"]/a/@href')
print(result)

# 将每个class为item-1的li标签作为1条新闻数据。提取a标签的文本内容以及链接，组装成一个字典。
data_dict = dict(zip(html.xpath('//li[@class = "item-1"]/a/text()'), html.xpath('//li[@class = "item-1"]/a/@href')))
print(data_dict)
