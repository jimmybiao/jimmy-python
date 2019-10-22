import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime
import os

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as err:
        print('Error:'+str(err))
        return ''

def getIndexLinks(url):
    #获取主页上所有链接和电影名
    htmltext=getHTMLText(url)
    soup=BeautifulSoup(htmltext,'html.parser')
    sections=soup.find_all('div',class_='co_content222')
    pagelst=[]
    for sec in sections:
        lis=sec.find('ul').find_all('li')
        for li in lis:
            a=li.find('a')
            mlst=[]
            href='https://www.dy2018.com'+a.attrs['href']
            mlst.append(href)
            title=a.attrs['title']
            mlst.append(title)
            pagelst.append(mlst)
    return pagelst

def getlinks(lst):
    #获取单部电影的评分和链接
    for i in lst:
        htmltext=getHTMLText(i[0])
        soup=BeautifulSoup(htmltext,'html.parser')
        rank=soup.find('div',class_='position')
        #rank
        rate=None
        try:
           rate=rank.find('span').find('strong').get_text()
           i.append(float(rate))
        except Exception as err:
            print('Error:'+str(err))
            i.append(None)
        
        item=soup.find('div',id='Zoom')
        try:
            items=item.find_all('table')
            for l in items:
                link=None
                try:
                    link=l.find('tbody').find('tr').find('td').find('a').attrs['href']
                    print(link)
                    i.append(link)
                except Exception as err:
                    print('Error:'+str(err))
                    i.append(link)
        except Exception as err:
            print('Error:'+str(err))
            continue

def write_excel_records(linklist,headers):
    if os.path.exists('links.xlsx'):
        os.remove('links.xlsx')
    wb=Workbook()
    ws=wb.active
    ws.append(headers)
    for row in linklist:
        ws.append(row)
    wb.save('links.xlsx')

if __name__=='__main__':
    starttime=datetime.datetime.now()
    movieurl='https://www.dy2018.com/'
    headers=['页面链接','电影名','豆瓣评分','种子地址']

    linklist=[]
    linklist=getIndexLinks(movieurl)
    getlinks(linklist)
    write_excel_records(linklist,headers)

    endtime=datetime.datetime.now()
    print('共用时'+str(endtime-starttime)+'秒')
    
    
