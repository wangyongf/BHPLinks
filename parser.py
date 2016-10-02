# coding=utf-8

# 网页解析器
import json

from bs4 import BeautifulSoup

from Bhp import Bhp
from LinkItem import LinkItem
from MyEncoder import MyEncoder
from Url import Url

html_doc = open('test.html', 'r')
node = BeautifulSoup(html_doc, "lxml")
items = node.select('div.dir-item')
bhp_links = Bhp()
count = 0  # 分类数量

for item in items:
    count += 1
    category = item.select('div.dir-name span')[0].string
    link_item = LinkItem(category)
    links = item.select('div.dir-content div.d-nav-item')
    for link in links:
        title = link.select('a')[0]['title']
        url = link.select('a')[0]['href']
        my_url = Url(url, title)
        link_item.add_link(my_url)
    bhp_links.add_link_item(link_item)

# 序列化json对象
# d = {'a': 'aaa', 'b': ['b1', 'b2', 'b3'], 'c': 100}
print(count)
json_str = json.dumps(bhp_links.get_bhp(), sort_keys=True, indent=4, cls=MyEncoder)
f = open('test.json', 'w')
f.write(json_str)
f.close()
