#!/usr/bin/env python3
"""Oyunun web dosyalarını Android uygulamasının assets/www klasörüne hazırlar.

- index.html ve ikonları kopyalar,
- three.js ve OrbitControls'ü indirip gömer (uygulama internetsiz açılsın),
- Google Fonts yazı tiplerini indirmeyi dener; olmazsa sistem yazı tipleri kullanılır,
- uygulamada gereksiz olan service worker kaydını ve bildirim düğmesini kaldırır,
- titreşimi Android köprüsüne bağlar.
"""
import pathlib
import re
import shutil
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "android" / "app" / "src" / "main" / "assets" / "www"
UA = "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Mobile Safari/537.36"
THREE = "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
ORBIT = "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "icons", OUT / "icons")
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    # 3D kütüphanesi: zorunlu
    (OUT / "three.min.js").write_bytes(get(THREE))
    (OUT / "OrbitControls.js").write_bytes(get(ORBIT))
    for url, local in ((THREE, "three.min.js"), (ORBIT, "OrbitControls.js")):
        pat = re.compile(r'<script src="' + re.escape(url) + r'"[^>]*></script>')
        html, n = pat.subn(f'<script src="{local}"></script>', html)
        if n != 1:
            print(f"HATA: {url} index.html içinde bulunamadı", file=sys.stderr)
            return 1

    # Yazı tipleri: isteğe bağlı
    m = re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)">', html)
    if m:
        try:
            css = get(m.group(1).replace("&amp;", "&")).decode("utf-8")
            (OUT / "fonts").mkdir()
            for i, fu in enumerate(dict.fromkeys(re.findall(r"url\((https://[^)]+)\)", css))):
                name = f"f{i}.woff2"
                (OUT / "fonts" / name).write_bytes(get(fu))
                css = css.replace(fu, f"fonts/{name}")
            (OUT / "fonts.css").write_text(css, encoding="utf-8")
            html = html.replace(m.group(0), '<link rel="stylesheet" href="fonts.css">')
            html = re.sub(r'<link rel="preconnect"[^>]*>\n?', "", html)
            print("Yazı tipleri gömüldü")
        except Exception as e:  # noqa: BLE001
            print(f"Uyarı: yazı tipleri indirilemedi ({e}); sistem yazı tipi kullanılacak")

    # Uygulamada service worker ve web bildirimi yok
    html, n = re.subn(r"<script>if\('serviceWorker' in navigator\).*?</script>\n?", "", html)
    if n != 1:
        print("Uyarı: service worker kaydı bulunamadı")
    html = html.replace('<link rel="manifest" href="manifest.json">\n', "")
    inject = (
        "<style>#ntf{display:none!important}</style>\n"
        "<script>if(window.AndroidBridge){navigator.vibrate=function(p){try{AndroidBridge.vibrate(JSON.stringify(p))}catch(e){}return true}}</script>\n"
    )
    if "</head>" in html:
        html = html.replace("</head>", inject + "</head>", 1)
    else:
        html = html.replace("<style>", inject + "<style>", 1)

    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"Hazır: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
