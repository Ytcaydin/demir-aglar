#!/usr/bin/env python3
"""CrazyGames için web paketi üretir: dist/crazygames/ ve DemirAglar-crazygames.zip

Önce android/prepare_assets.py çalışmış olmalı (three.js ve yazı tipleri oradan alınır).
Farklar:
- CrazyGames SDK v3 yüklenir, oyun SDK hazır olunca başlar (en çok 4 sn beklenir).
- Dil CrazyGames'in verdiği dilden seçilir (oyuncu Ayarlar'dan seçtiyse o kalır).
- Kayıtlar localStorage yerine CrazyGames veri modülüne yazılır (giriş yapan oyuncuda buluta).
- Her zaman tam ekran düzeni; oyunun kendi tam ekran, bildirim ve yedek düğmeleri gizli.
- Ödüllü reklamlar CrazyGames reklamlarıyla gösterilir.
"""
import pathlib
import re
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "android" / "app" / "src" / "main" / "assets" / "www"
OUT = ROOT / "dist" / "crazygames"
ZIP = ROOT / "dist" / "DemirAglar-crazygames.zip"

LOADER = """<script>
(async()=>{const C=window.CrazyGames&&window.CrazyGames.SDK;let store=null;
  try{if(C){
    await Promise.race([C.init(),new Promise(r=>setTimeout(r,4000))]);
    try{C.game.loadingStart()}catch(e){}
    if(C.environment&&C.environment!=='disabled'){store=C.data;
      const si=C.user&&C.user.systemInfo,loc=(si&&(si.locale||si.language||si.countryCode))||'';let o={};
      try{o=JSON.parse(store.getItem('demir-aglar-opt')||'{}')||{}}catch(e){}
      if(!o.lang&&loc&&!/[?&]lang=/.test(location.search))window.DA_LANG=/^tr/i.test(loc)?'tr':'en'}}}catch(e){}
  window.DA_STORE=store||window.localStorage;
  for(const s of [...document.querySelectorAll('script[type="text/da-boot"]')]){const n=document.createElement('script');n.textContent=s.textContent;document.body.appendChild(n)}
})();
</script>
"""


def main() -> int:
    if not (SRC / "index.html").exists():
        print("HATA: önce python3 android/prepare_assets.py çalıştır", file=sys.stderr)
        return 1
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for p in SRC.iterdir():
        if p.name == "index.html":
            continue
        if p.is_dir():
            shutil.copytree(p, OUT / p.name)
        else:
            shutil.copy2(p, OUT / p.name)

    html = (SRC / "index.html").read_text(encoding="utf-8")
    # Android'e özgü titreşim köprüsü gerekmez
    html = re.sub(r"<script>if\(window\.AndroidBridge\)\{navigator\.vibrate=.*?</script>\n?", "", html)
    sdk = '<script src="https://sdk.crazygames.com/crazygames-sdk-v3.js"></script>\n<script>window.DA_CG=true</script>\n'
    html = html.replace("</head>", sdk + "</head>", 1)

    # three.js ve OrbitControls'ten sonraki satır içi betikler SDK hazır olunca çalışsın
    start = html.index('<script src="OrbitControls.js"></script>') + len('<script src="OrbitControls.js"></script>')
    head, tail = html[:start], html[start:]
    n = 0

    def boot(m):
        nonlocal n
        n += 1
        body = m.group(1).replace("localStorage", "DA_STORE")
        return '<script type="text/da-boot">' + body + "</script>"

    tail = re.sub(r"<script>([\s\S]*?)</script>", boot, tail)
    if n < 2:
        print(f"HATA: beklenen betikler bulunamadı ({n})", file=sys.stderr)
        return 1
    tail = tail.replace("</body>", LOADER + "</body>", 1)
    (OUT / "index.html").write_text(head + tail, encoding="utf-8")

    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(OUT.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(OUT).as_posix())
    print(f"Hazır: {ZIP} ({ZIP.stat().st_size // 1024} KB, {n} betik)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
