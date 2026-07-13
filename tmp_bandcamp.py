import requests, re
urls = [
    'https://vade-reprise.bandcamp.com/album/movement-i',
    'https://vade-reprise.bandcamp.com/album/first-one',
    'https://vade-reprise.bandcamp.com/album/jimmy-bizarre-stuff',
    'https://vade-reprise.bandcamp.com/album/unreleased'
]
for u in urls:
    print('URL', u)
    html = requests.get(u, timeout=20).text
    m = re.search(r'album=(\d+)', html)
    print('album_id', m.group(1) if m else 'none')
    m2 = re.search(r'"trackinfo"\s*:\s*\[', html)
    print('has_trackinfo', bool(m2))
    print(html[:2000])
    print('---')
