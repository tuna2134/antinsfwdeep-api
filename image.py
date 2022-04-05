import requests

with open("url.txt", "r") as f:
    lines = f.readlines()
    
for url in lines:
    r = requests.get(url)
    try:
        r.raise_for_status()
    except:
        continue
    else:
        with open("", "wb") as f:
            f.write(r.content)
