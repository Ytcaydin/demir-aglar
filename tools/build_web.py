#!/usr/bin/env python3
"""Genel web paketi üretir: dist/web/ ve dist/DemirAglar-web.zip

itch.io, Newgrounds, Game Jolt gibi kendi reklam altyapısı istemeyen siteler içindir.
Önce android/prepare_assets.py çalışmış olmalı (three.js ve yazı tipleri oradan alınır;
paket internetsiz de açılır).

Farklar (Android paketine göre):
- Android titreşim köprüsü çıkarılır.
- Reklam yoktur: ödüllü düğmeler ödülü doğrudan verir (oyun bunu kendisi algılar).
- Service worker / bildirim yoktur (portal iframe'inde çalışmaz).
"""
import pathlib
import re
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "android" / "app" / "src" / "main" / "assets" / "www"
OUT = ROOT / "dist" / "web"
ZIP = ROOT / "dist" / "DemirAglar-web.zip"


def main() -> int:
    if not (SRC / "index.html").exists():
        print("HATA: önce python3 android/prepare_assets.py çalıştır", file=sys.stderr)
        return 1
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT)
    p = OUT / "index.html"
    html = p.read_text(encoding="utf-8")
    html = re.sub(r"<script>if\(window\.AndroidBridge\)\{navigator\.vibrate=.*?</script>\n?", "", html)
    # portal içinde çalıştığını oyuna bildir (kendi sitedeki "uygulama olarak kur" düğmeleri çıkmasın)
    html = html.replace("</head>", "<script>window.DA_PORTAL=true</script>\n</head>", 1)
    if "serviceWorker" in html and "register('sw.js')" in html:
        html = re.sub(r"<script>if\('serviceWorker' in navigator\).*?</script>\n?", "", html)
    p.write_text(html, encoding="utf-8")

    ZIP.parent.mkdir(parents=True, exist_ok=True)
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(OUT).as_posix())
    print(f"Hazır: {ZIP} ({ZIP.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
