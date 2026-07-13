import requests, re, sys
url = sys.argv[1]
html = requests.get(url, timeout=30).text
print('len', len(html))
for pattern in [r'album=(\d+)', r'tralbumid\s*=\s*(\d+)', r'album_id\s*=\s*(\d+)', r'item_id\s*=\s*(\d+)', r'trackinfo\s*=\s*\[']:
    m = re.search(pattern, html)
    if m:
        print(pattern, '->', m.group(1) if m.lastindex else m.group(0))
