import requests, re, sys
url = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0'}
html = requests.get(url, headers=headers, timeout=30).text
print('URL', url)
for pat in [r'https://[^"\'\s<>]+\.mp3', r'https://[^"\'\s<>]+\.m4a', r'https://[^"\'\s<>]+/stream/[^"\'\s<>]+', r'https://[^"\'\s<>]+\.mp3\?download=1']:
    matches = re.findall(pat, html, flags=re.I)
    if matches:
        print(pat)
        for m in matches[:10]:
            print(m)
        print('---')
print('done')
