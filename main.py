'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/26 20:28
@Software: PyCharm
@File    : main.py
'''
import requests
import re


def parse_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 '
                      'QQBrowser/10.4.3341.400',
    }
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', text,
                        re.DOTALL)#re.DOTALL = re.S
    # print(titles)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text,
                           re.DOTALL)
    # print(dynasties)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text,
                         re.DOTALL)
    # print(authors)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', text,
                          re.DOTALL)
    contents = []
    for content in content_tags:
        info = re.sub(r'<.*?>', "", content)
        # print(info.strip())
        contents.append(info.strip())

    pomes =[]
    for value in zip(titles,dynasties,authors,contents):
        title, dynasty, author, content = value
        pome = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        pomes.append(pome)

    for pome in pomes:
        print(pome)

def main():
    base_url = "https://www.gushiwen.org/default_{}.aspx"
    for i in range(1, 101):
        url = base_url.format(i)
        print(url)
        parse_page(url)
        # break

    # for i in range(1, 101):
    #     url = "https://www.gushiwen.org/default_%s.aspx" % i
    #     print(url)


if __name__ == '__main__':
    main()
