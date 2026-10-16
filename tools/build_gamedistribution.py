#!/usr/bin/env python3
"""GameDistribution paketi üretir: dist/gamedistribution/ ve dist/DemirAglar-gamedistribution.zip

Önce android/prepare_assets.py çalışmış olmalı.
Oyun kimliği (Game ID) GameDistribution panelinden alınır ve GD_GAME_ID ortam değişkeniyle verilir;
verilmezse paket yine üretilir ama yer tutucu kimlikle (yüklemeden önce kimlik girilmeli).

Farklar:
- GD HTML5 SDK yüklenir; reklam olayları oyundaki DA_GD bloğuna bağlanır
  (SDK_GAME_PAUSE: oyun durur + ses kapanır, SDK_GAME_START: devam, SDK_REWARDED_WATCH_COMPLETE: ödül).
- Android titreşim köprüsü ve service worker çıkarılır.
"""
import os
import pathlib
import re
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "android" / "app" / "src" / "main" / "assets" / "www"
OUT = ROOT / "dist" / "gamedistribution"
ZIP = ROOT / "dist" / "DemirAglar-gamedistribution.zip"

HEAD = """<script>window.DA_GD=true;window.DA_PORTAL=true;
window.GD_OPTIONS={gameId:"%s",onEvent:function(e){if(window.__gdEvent)window.__gdEvent(e)}};</script>
"""
LOADER = """<script>(function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(d.getElementById(id))return;
js=d.createElement(s);js.id=id;js.src='https://html5.api.gamedistribution.com/main.min.js';fjs.parentNode.insertBefore(js,fjs);
}(document,'script','gamedistribution-jssdk'));</script>
"""


def main() -> int:
    if not (SRC / "index.html").exists():
        print("HATA: önce python3 android/prepare_assets.py çalıştır", file=sys.stderr)
        return 1
    gid = (os.environ.get("GD_GAME_ID") or "").strip() or "GD_GAME_ID_BURAYA"
    if not re.fullmatch(r"[A-Za-z0-9_\-]+", gid):
        print("HATA: GD_GAME_ID geçersiz", file=sys.stderr)
        return 1
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT)
    p = OUT / "index.html"
    html = p.read_text(encoding="utf-8")
    html = re.sub(r"<script>if\(window\.AndroidBridge\)\{navigator\.vibrate=.*?</script>\n?", "", html)
    html = re.sub(r"<script>if\('serviceWorker' in navigator\).*?</script>\n?", "", html)
    html = html.replace("</head>", HEAD % gid + "</head>", 1)
    html = html.replace("</body>", LOADER + "</body>", 1)
    p.write_text(html, encoding="utf-8")
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(OUT).as_posix())
    note = "" if gid != "GD_GAME_ID_BURAYA" else " (UYARI: oyun kimliği girilmedi)"
    print(f"Hazır: {ZIP} ({ZIP.stat().st_size // 1024} KB){note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
