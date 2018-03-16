
#爬取代理ip入mysql
import requests,re,os



def getIP(url,headers):
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    html = response.text
    
    reg = re.compile('<tr class="odd">.*?<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
    data = reg.findall(html)

    for i in data:
        ip = i[0]
        duankou = i[1]
        i = list(i)
        #print(ip,duankou)

        with open(r'D:\pyjiaoben\代理ip\ip.txt', 'w')as f:
            f.write(str(i))
            f.close()
            print(i[0], i[1])

        # db = pymysql.connect('localhost','root','cw961017','chenbaba')
        # cursor = db.cursor()
        # sql = 'insert into dailiip（ip，duankou）values("%s","%s")'%(ip,duankou)
        # try:
        #
        #     cursor.execute(sql)
        #     db.commit()
        # except:
        #     db.rollback()
        # #data = cursor.fetchone()
        # #print(data)
        # cursor.close()
        # db.close()

        
url = 'http://www.xicidaili.com/'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
    }
getip = getIP(url,headers)




