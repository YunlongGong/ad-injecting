# -*- coding:utf-8 -*-


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def get_data(url):
    response_str = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(response_str, 'html.parser')  # 解析网页
    content_raw = soup.article.get_text()
    content = "".join(content_raw.split())
    return content


if __name__ == "__main__":
    get_data('https://www.sohu.com/a/227962203_118792?_f=index_businessnews_0_2')