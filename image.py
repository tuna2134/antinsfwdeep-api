import requests
import random, string

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

with open("urls_sexy.txt", "r") as f:
    lines = f.readlines()
    
for url in lines:
    r = requests.get(url)
    try:
        r.raise_for_status()
    except:
        continue
    else:
        with open(randomname(10) + ".jpg", "wb") as f:
            f.write(r.content)
