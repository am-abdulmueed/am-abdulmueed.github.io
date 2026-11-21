# Usage: python3 build.py
# Reads others.json and writes the games straight into index.html (so the page needs no json fetch).
import json, re
games = json.load(open('others.json', encoding='utf-8'))['games']
seen, rows = set(), []
for g in games:
    s = (g.get('slug') or '').strip().lower()
    if not s or re.search(r'\s', s) or s in seen:
        continue
    url = g.get('playgamaGameUrl') or g.get('gameURL') or ''
    if not url.startswith('http'):
        continue
    imgs = g.get('images')
    img = imgs[0] if isinstance(imgs, list) and imgs and str(imgs[0]).startswith('http') else ''
    m = re.match(r'https://img\.arcadrome\.com/([^/]+)/icon\.png$', img)
    desc = (g.get('description') or '').strip()
    if len(desc) > 140:
        desc = desc[:130].rsplit(' ', 1)[0] + '…'
    seen.add(s)
    rows.append([str(g.get('id', '')), s, g.get('title') or s, m.group(1) if m else img,
                 '' if url == 'https://arcadrome.com/embed/' + s else url, desc])
data = json.dumps(rows, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = open('index.html', encoding='utf-8').read()
html = re.sub(r'/\*DATA_START\*/.*?/\*DATA_END\*/', lambda _: '/*DATA_START*/var G=' + data + ';/*DATA_END*/', html, flags=re.S)
open('index.html', 'w', encoding='utf-8').write(html)
print(len(rows), 'games written into index.html')
