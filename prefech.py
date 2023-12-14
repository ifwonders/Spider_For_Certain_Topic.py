# 2023-10-20

import requests

def getcookie():
    # 首先需要获取新浪微博Cookie
    # 发出第一个请求获取tid
    url_for_tid = "https://passport.weibo.com/visitor/genvisitor?cb=gen_callback"
    response_for_tid = requests.get(url=url_for_tid)
    tid = response_for_tid.text[84:130]

    # 发出第二个请求获取Cookie 包含sub和subp
    url_for_cookie = f"https://passport.weibo.com/visitor/visitor?a=incarnate&t={tid}&w=3&c=100&cb=cross_domain&from=weibo"
    response_for_cookie = requests.get(url=url_for_cookie)
    # 根据返回信息截取cookie
    sub = response_for_cookie.text[response_for_cookie.text.find("sub") + 6:response_for_cookie.text.find("subp") - 3]
    subp = response_for_cookie.text[response_for_cookie.text.find("subp") + 7:-5]

    # 制作携带Cookie的headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36",
        "Cookie": f"SUBP={subp}; SUB={sub}; cross_origin_proto=SSL; _s_tentry=passport.weibo.com"
    }

    return headers
