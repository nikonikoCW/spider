#coding=utf-8
import requests
import re
import base64
import pyperclip
import os
my_email = input('请输入你的email:')
#my_email = 'hxuzk3qn@ncdidi.tk'
cookie_info = {}
cookie = ''
proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
ssr_dingyue = []
def code(my_email):
    print('设置头,data,链接')
    headers = {
        'authority': 'www.paofucloud.com',
        'method': 'POST',
        'path': '/auth/send',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '28',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__cfduid=d1354086a1ad92f8620d96965c11f358a1570498416; _ga=GA1.2.1770598837.1570498418; _gid=GA1.2.1468450227.1570498418; ip=4bebc3a19783256d580263c6f1a17c7d; expire_in=1571103299; _gat_gtag_UA_90263540_5=1',
        'origin': 'https://www.paofucloud.com',
        'referer': 'https://www.paofucloud.com/auth/register',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
    data = {
        'email': my_email
        }
    url = 'https://www.paofucloud.com/auth/send'
    print('开始获取邮箱码')
    response= requests.post(url,data=data,headers=headers,proxies=proxies)
    print('请查看邮箱',response.status_code)

def regist(my_email):
    headers = {
        'authority': 'www.paofucloud.com',
        'method': 'POST',
        'path': '/auth/send',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '28',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__cfduid=d1354086a1ad92f8620d96965c11f358a1570498416; _ga=GA1.2.1770598837.1570498418; _gid=GA1.2.1468450227.1570498418; ip=4bebc3a19783256d580263c6f1a17c7d; expire_in=1571103299; _gat_gtag_UA_90263540_5=1',
        'origin': 'https://www.paofucloud.com',
        'referer': 'https://www.paofucloud.com/auth/register',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    url2 = 'https://www.paofucloud.com/auth/register'
    email_code = input('请输入邮箱验证码:')
    data2 = {
        'email': my_email,
        'passwd': 'cw18708178851..',
        'repasswd': 'cw18708178851..',
        'code': '0',
        'emailcode': email_code
        }
    print('已经设置信息了准备开始注册')
    response_regist = requests.post(url2,data=data2,headers=headers,proxies=proxies)
    print(response_regist.status_code)
    print('已经注册完成，准备登陆')

def login(my_email,cookie_info):
    global cookie
    headers = {
        'authority': 'www.paofucloud.com',
        'method': 'POST',
        'path': '/auth/send',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '28',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__cfduid=d1354086a1ad92f8620d96965c11f358a1570498416; _ga=GA1.2.1770598837.1570498418; _gid=GA1.2.1468450227.1570498418; ip=4bebc3a19783256d580263c6f1a17c7d; expire_in=1571103299; _gat_gtag_UA_90263540_5=1',
        'origin': 'https://www.paofucloud.com',
        'referer': 'https://www.paofucloud.com/auth/register',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    url = 'https://www.paofucloud.com/auth/login'
    data = {
        'email': my_email,
        'passwd': 'cw18708178851..',
        'code':''
    }

    proxies = {
        'https': 'https://127.0.0.1:1080',
        'http': 'http://127.0.0.1:1080'
    }
    print('已经设置登陆信息，准备登陆')
    response = requests.post(url,data=data,headers=headers,proxies=proxies)
    cookie_data = response.headers['Set-Cookie']
    reg_uid = re.compile('uid=(.*?);')
    reg_email = re.compile('email=(.*?);')
    reg_key = re.compile('key=(.*?);')
    reg_ip = re.compile('ip=(.*?);')
    reg_expire_in = re.compile('expire_in=(.*?);')
    uid = reg_uid.findall(cookie_data)
    email = reg_email.findall(cookie_data)
    key = reg_key.findall(cookie_data)
    ip = reg_ip.findall(cookie_data)
    expire_in = reg_expire_in.findall(cookie_data)
    cookie = '__cfduid=d1354086a1ad92f8620d96965c11f358a1570498416; _ga=GA1.2.1770598837.1570498418; _gid=GA1.2.1468450227.1570498418; _gat_gtag_UA_90263540_5=1; uid=%s; email=%s; key=%s; ip=%s; expire_in=%s; _gat_gtag_UA_90263540_5=1;' % (uid[0], email[0], key[0], ip[0], expire_in[0])
    print('已经登录准备开始购买免费套餐')
def buy_mianfei(cookie):
    url = 'https://www.paofucloud.com/user/buy'
    data = {
        'coupon':'',
        'shop': '21',
        'autorenew': '0',
        'disableothers': '1'
    }

    headers = {
        'authority': 'www.paofucloud.com',
        'method': 'POST',
        'path': '/auth/send',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '28',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': cookie,
        'origin': 'https://www.paofucloud.com',
        'referer': 'https://www.paofucloud.com/auth/register',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    print('已经设置购买的信息，准备购买免费套餐')
    response = requests.post(url,data=data,headers=headers,proxies=proxies)
    if response.status_code == '200':
        print('已经购买免费套餐，准备获取订阅链接')
    else:
        print('购买失败')

def get_ssr_link(cookie):
    url = 'https://www.paofucloud.com/user'
    cookie2 = '__cfduid=d1354086a1ad92f8620d96965c11f358a1570498416; _ga=GA1.2.1770598837.1570498418; uid=59686; email=9goh7qji%40ncdidi.tk; key=108fb13d5a7dc1b62ff210577f921a7090ee416de6a27; ip=e65bd0984b662988ae63dd35468d4fbc; expire_in=1570843597; _gid=GA1.2.1914261401.1570757197; _gat=1; _gat_gtag_UA_90263540_5=1'
    #这个傻逼地址不能完全照搬headers会tm返回值报错，我也不晓得为什么
    headers = {
        'authority': 'www.paofucloud.com',
        'method': 'GET',
        'path': '/user',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'cookie': cookie2,
        'referer': 'https://www.paofucloud.com/user',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    print('已经设置好获取订阅连接的请求头，下一步进行获取数据')
    response = requests.get(url,headers=headers,proxies=proxies)
    r = response.text
    reg_link = re.compile('data-clipboard-text="(.*?)"><i class="malio-ssr"></i> 复制 SSR 订阅链接</a>')
    data_link = reg_link.findall(r)
    ssr_dingyue.append(data_link[0])
    print('已经解码，准备获取数据')
def huoqu_ssr():
    url = ssr_dingyue[0]
    print('开始解析订阅')
    response = requests.get(url, proxies=proxies)
    data = response.text
    print('开始补足加密部分')
    data = data.replace('c3Ny', '==c3Ny')
    data = data[2:]
    data = data + str('==')
    print('开始解密')
    data_b = str.encode(data)
    a = base64.b64decode(data_b)
    cc = str(a, encoding="utf8")
    pyperclip.copy(cc)
    with open('./ssr.txt','w',encoding='utf-8')as f:
        f.write(cc)
    print('已经将所有SSR节点复制到剪贴板,并且已经写到同级目录ssr.txt里了')


code(my_email)
regist(my_email)
login(my_email,cookie_info)
buy_mianfei(cookie)
get_ssr_link(cookie)
huoqu_ssr()