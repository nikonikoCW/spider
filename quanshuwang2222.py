import requests
import re
import os


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
shuru_url= str(input('请输入小说url地址,后面加上“/”：'))

url = shuru_url
response = requests.get(url,headers = headers)
response.encoding = 'gbk'
html = response.text


title = 'xiaoshuo'
fb = open('%s.tx' % title, 'w', encoding='utf-8')
list_reg =re.compile( '<td class="L"><a href="(.*?)">(.*?)</a></td>')
xslist = list_reg.findall(html)



for list in xslist:
    zhangjie_url,zhangjie_name = list
    zhangjie_url = 'http://www.wutuxs.com%s'%zhangjie_url
    #print(zhangjie_url,zhangjie_name)
    #print(zhangjie_url)
    neirong_response = requests.get(zhangjie_url)
    neirong_response.encoding = 'gbk'
    neirong_html = neirong_response.text
    neirong_reg = re.compile('<dd id="contents">([\s\S]*?)</dd>')
    neirong = neirong_reg.findall(neirong_html)
    neirong = str(neirong)
    neirong = neirong.replace('<br />','')
    neirong = neirong.replace('\\n','\n')
    neirong = neirong.replace('\\r', '')
    neirong = neirong.replace('', '')
    neirong = neirong.replace('&nbsp;','')

    fb.write(zhangjie_name)
    fb.write(neirong)
    fb.write('\n\n\n\n')
    print(zhangjie_url)
