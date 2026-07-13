import requests, re, sys
url = sys.argv[1]
html = requests.get(url, timeout=30).text
print('URL', url)
for pat in [r'https://[^"\'\s<>]+\.mp3', r'https://[^"\'\s<>]+\.m4a', r'https://[^"\'\s<>]+\.wav', r'https://[^"\'\s<>]+/stream/[^"\'\s<>]+']:
    matches = re.findall(pat, html, flags=re.I)
    if matches:
        print(pat)
        for m in matches[:10]:
            print(m)
        print('---')
print('done')
