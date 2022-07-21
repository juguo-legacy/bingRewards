import webbrowser
import subprocess
import time
import psutil
import random

def OpenWebsite(url):
    webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open_new_tab(url)

baseUrl = "https://www.bing.com/search?q="
alphabet = "abcdefghijklmnopqrstuvwxyz"

edgeProcess = subprocess.Popen(['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', '-new-tab'])

# edge
for i in range(40):
    newUrl = baseUrl
    for j in range(20):
        newUrl += random.choice(alphabet)
    OpenWebsite(newUrl)
    time.sleep(0.25)

psutil.Process(edgeProcess.pid).kill()