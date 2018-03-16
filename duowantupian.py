import requests
import re
import os
import random

url = 'http://tu.duowan.com/m/meinv'

def taotu_list_url(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    return html
taotu_html = taotu_list_url(url)
reg = re.compile('<em><a href="(.*?)" target="_blank">(.*?)</a> .*?</em>')
url_list = reg.findall(taotu_html)
#print(url_list[0][0])

for tuzu_url,tuzu_name in url_list:
    #print(tuzu_url,tuzu_name)

    tuzu_response = requests.get(tuzu_url)
    #print(tuzu_url)

    tuzu_response.encoding = 'utf-8'
    tuzu_response_html = tuzu_response.text
    #print(tuzu_response_html)

    taozu_reg = re.compile('<a href="(.*?)" class="picture-list">.*?</a>')
    zuizhuang_taozu_url_list = taozu_reg.findall(tuzu_response_html)
   # print(zuizhuang_taozu_url_list)

    zuizhong_tuzu_url_response = requests.get(zuizhuang_taozu_url_list[0])
    zuizhong_tuzu_url_response.encoding = 'utf-8'
    zuizhong_tuzu_url_html = zuizhong_tuzu_url_response.text
    zuizhong_reg = re.compile('<span class="pic-box-item" data-img="(.*?)" data-mp4=""></span>')
    zuizhong_url_list = zuizhong_reg.findall(zuizhong_tuzu_url_html)
    #print(zuizhong_url_list)
    shuliang = len(zuizhong_url_list)
    print(len(zuizhong_url_list))
    for each_url in zuizhong_url_list:
        print(each_url)
        #print(len(zuizhong_url_list))
        xiazai_response = requests.get(each_url)
        #print(xiazai_response.status_code)
        with open('D:\\pachongtupian\\%s.jpg'%(tuzu_name+str(shuliang)),'wb')as f:
            f.write(xiazai_response.content)
            f.close()
            shuliang = shuliang - 1

    exit()

exit()
