import webbrowser
import subprocess
import psutil
import random
import time

def OpenWebsite(url):
    webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open_new_tab(url)

baseUrl = "https://www.bing.com/search?q="
alphabet = "abcdefghijklmnopqrstuvwxyz"

mobile = subprocess.Popen(['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', '--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'])

time.sleep(2)

# mobile first
for i in range(25):
    newUrl = baseUrl
    for j in range(20):
        newUrl += random.choice(alphabet)
    OpenWebsite(newUrl)
    time.sleep(0.25)

psutil.Process(mobile.pid).kill()