import urllib.request
import re

url = 'https://github.com/AakashGs10/COLLEGE-PROJECTS'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Regex to find links to files/folders in the repo
    matches = re.findall(r'href="/AakashGs10/COLLEGE-PROJECTS/tree/[^/]+/([^"]+)"', html)
    print("Folders:")
    for m in set(matches):
        print(m)
except Exception as e:
    print(e)
