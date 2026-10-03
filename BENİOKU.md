# Demir Ağlar

Türk şehirleriyle, şehirlerin ihtiyaçlarını taşıyarak büyüttüğün bir demiryolu tycoon oyunu. 1927'de İstanbul–Eskişehir hattıyla başlarsın.

## Çağlar

Oyun 4 çağdan geçer: Kuruluş (1927), Kalkınma (1950), Elektrik (1975), Hızlı Tren (2003). Her çağ yeni trenler (Mavi Tren, Elektrikli, YHT), yeni rakipler (karayolu, havayolu) ve daha büyük şehirler getirir. Yeterince şehri bağlayınca Görevler sekmesinden sonraki çağa atlayabilirsin.

## Büyük projeler

Şirket sekmesinden Haydarpaşa Limanı’ndan Marmaray’a 11 büyük yatırım yapabilirsin. Peşinatı ver, kalanı aylık taksitle öde; bittiğinde kalıcı bir kazanç ve şehrin siluetinde yeni bir yapı.

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `index.html` | Oyunun 3D sürümü (asıl oyun) |
| `vitrin-2026.html` | 2026 vitrini: her şey en iyi yapılınca şehirlerin bugünkü hâli |
| `demir-aglar-2d.html` | Eski 2D izometrik sürüm, karşılaştırma için |
| `manifest.json`, `sw.js`, `icons/` | Telefona uygulama gibi kurulabilmesi için PWA dosyaları |

## Bilgisayarda açmak

`index.html` dosyasına çift tıkla. İlk açılışta internet gerekir, çünkü 3D kütüphanesi (three.js) internetten yüklenir.
Not: Dosyayı doğrudan açınca uygulama olarak kurma ve çevrimdışı çalışma devreye girmez; bunlar için siteye koyman gerekir.

## Telefona uygulama gibi kurmak (GitHub Pages ile, ücretsiz)

1. GitHub'da yeni bir depo aç (ör. `demir-aglar`), bu klasördeki her şeyi olduğu gibi yükle (`icons` klasörü dahil).
2. Depoda **Settings → Pages** bölümüne gir, **Branch: main** ve **/(root)** seçip kaydet.
3. Birkaç dakika sonra oyun `https://KULLANICI-ADIN.github.io/demir-aglar/` adresinde açılır.
4. Telefonda Chrome ile bu adresi aç, menüden **Ana ekrana ekle** de. Oyun uygulama gibi tam ekran açılır.
   İlk açılıştan sonra 3D kütüphanesi önbelleğe alınır, internet olmadan da oynanabilir.

## Kayıtlar

İlerleme tarayıcının kendi hafızasında (localStorage) tutulur. Farklı adres veya tarayıcıda açarsan kayıt oradan başlar.

## Play Store için

Play Store'a çıkmak için bu PWA, Bubblewrap veya PWABuilder ile Android uygulamasına (TWA) paketlenebilir. Gerçek reklam (AdMob) ve uygulama içi satın alma o aşamada bağlanır; şu an oyundaki "REKLAM" düğmeleri demo.
