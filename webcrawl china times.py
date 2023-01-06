import re
import time
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

def get_web_page(URL):
    resp = requests.get(
        url = URL,
        headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36" }
    )
    if resp.status_code != 200:
        print('Invalide url:', resp.url)
        print('status code:',resp.status_code)
        return None
    else:
        return resp.text

def get_date(date_str):
    pattern = '\d+/\d+'
    match = re.search(pattern, date_str)
    if match is None:
        return date_str
    else:
        return match.group(0)

def get_title(dom, today, yesterday):
    results = []
    soup = BeautifulSoup(dom, 'html.parser')
    page = int(soup.find('span','page-numbers current').text) 
    next_url = 'https://m.ctee.com.tw/livenews/aj?page='+str(page+1)
    newstitles = soup.find_all('p', 'now-title')

    for newstitle in newstitles:
        list_of_newstitle = newstitle.text.strip().replace('            ',"").split('\n')
        title_plus_time = list_of_newstitle[4]
        if get_date(title_plus_time) == today or get_date(title_plus_time) == yesterday:
            href = newstitle.find_all('a')[1]['href']
            time = list_of_newstitle[-1].split('  | ')[-1]
            title = list_of_newstitle[-1].split('  | ')[-2]
            results.append({
                'Title': title,
                'Publish Time': time,
                'Link': href
            })
            
    return results, next_url


currentpage = get_web_page('https://ctee.com.tw/livenews/aj')

if currentpage:
    now = datetime.now()
    yesterdayformat = now- timedelta(days=1)
    yesterday = yesterdayformat.strftime("%m/%d")
    today = now.strftime("%m/%d")
    
    articles = []
    currentpagenews, next_url = get_title(currentpage, today, yesterday)
    
    while currentpagenews: #只要還有辦法跑出current_articles, 還有result, result不是空的while就會執行。簡單來說只要你這一頁有今天跟昨天的時間點就還會執行
        articles += currentpagenews
        currentpage = get_web_page(next_url)
        currentpagenews, next_url = get_title(currentpage, today, yesterday)

    op = input('Please enter the keyword you are looking for：')
    print('Please enter the keyword you are looking for：',op)

    count = 0
    for a in articles:
        
        if op in a['Title']:
            print(a['Title'],a['Publish Time'])
            print(a['Link'],'\n')
            count+=1
    
    if count ==0:
        print('Sorry, there are no news related to this keyword in the past two days.')
            