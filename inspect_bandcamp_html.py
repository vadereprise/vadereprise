import requests, re, sys
url = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0'}
html = requests.get(url, headers=headers, timeout=30).text
print('URL:', url)
print('length:', len(html))
for pattern in [r'EmbeddedPlayer', r'trackinfo', r'tracknum', r'track_id', r'track=\d+', r'album=\d+', r'\btralbumid\b', r'\btrack_id\b', r'\btracknum\b', r'\balbum_id\b', r'\bitem_id\b', r'https://[^"\'\s<>]+\.mp3', r'https://[^"\'\s<>]+\.m4a']:
    matches = re.findall(pattern, html, flags=re.I)
    if matches:
        print(pattern, '->', matches[:20])
        print('count', len(matches))
        print('---')
