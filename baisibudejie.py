#短视频爬取
import requests,re,os
import urllib

k = int(input('xiazaiduoshaoye:'))

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
'Referer':'https://www.baidu.com/link?url=aGhcQW8nvLdpV6uUX1bzXxr7zRh5elZj4G2p64vKZsH54nRTwfyBvTuU-JG1Xa5N&wd=&eqid=a248d85f00010724000000055a99245c'
}

def get_url_list(k,headers):
    url = 'http://www.budejie.com/video/{}'.format(k)
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    html = response.text
    reg = re.compile('<a href="(.*?)" target="_blank" download="" class="ipad-down-href" style="border:0;outline: none;">')#匹配url
    #                 <a href="http://svideo.spriteapp.com/video/2018/0228/5a9686082fa11_wpd.mp4" target="_blank" download="" class="ipad-down-href" style="border:0;outline: none;">
    url_list = reg.findall(html)
    #print(url_list)
    m = len(url_list)
    for i in url_list:
        with open('D:\\xx\\%s.mp4' % str(m), 'wb')as f:
            response_list_url = requests.get(i)
            f.write(response_list_url.content)
            f.close()
            # exit()#只进行一次下载
            print('正在下载：%s'%response_list_url)
            m = m-1
    k = k - 1
if __name__ == '__main__':
    get_url_list(k,headers)


