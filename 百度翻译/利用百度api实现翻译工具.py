# coding=utf-8
import requests
import sys

a = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"
}

post_data = {
    "query":a,
    "from":"zh",
    "to":"en",
}

post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode())