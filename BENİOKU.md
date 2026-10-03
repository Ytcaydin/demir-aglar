# Demir Ağlar

Türk şehirleriyle, şehirlerin ihtiyaçlarını taşıyarak büyüttüğün bir demiryolu tycoon oyunu. 1927'de İstanbul–Eskişehir hattıyla başlarsın.

## Çağlar

Oyun 4 çağdan geçer: Kuruluş (1927), Kalkınma (1950), Elektrik (1975), Hızlı Tren (2003). Her çağ yeni trenler (Mavi Tren, Elektrikli, YHT), yeni rakipler (karayolu, havayolu) ve daha büyük şehirler getirir. Yeterince şehri bağlayınca Görevler sekmesinden sonraki çağa atlayabilirsin.

## Büyük projeler

Şirket sekmesinden Haydarpaşa Limanı’ndan Marmaray’a 11 büyük yatırım yapabilirsin. Peşinatı ver, kalanı aylık taksitle öde; bittiğinde kalıcı bir kazanç ve şehrin siluetinde yeni bir yapı.

## Tarihten sayfalar

Oyun ilerledikçe Türkiye tarihinden 11 gerçek olay karşına çıkar: Harf Devrimi (1928), demiryolunun Sivas’a ulaşması (1930), Cumhuriyetin 10. yılı (1933), Erzincan depremi (1939), savaş yılları (1940), Marshall yardımı (1951), ilk kalkınma planı (1963), petrol krizi (1973), Marmara depremi (1999), 2001 krizi ve ilk YHT (2009). Her olayda bir karar verirsin; kararın birkaç ay ya da yıl boyunca gelirini, giderini veya tren hızını etkiler. Verdiğin kararlar Albüm sekmesinde birikir.

## Şehir albümü

Bir şehri ağa bağladığında albümüne o şehrin kartı eklenir: yöresel ürünü ve kısa bir tarih bilgisi. Bir bölgenin (Marmara, Ege, Karadeniz…) bütün kartlarını toplarsan ödül alırsın ve o bölgede yolcu geliri kalıcı olarak %5 artar. Albüm yeni oyunlarda da seninle kalır.

## Paylaş ve rekorlar

Şirket sekmesinde **Ağımı paylaş** düğmesi, ağının haritası ve rakamlarıyla bir görsel oluşturur; telefonda doğrudan WhatsApp, Instagram gibi uygulamalara gönderilir. Haftalık kazancın ve tüm zamanların rekoru bu cihazda tutulur. Arkadaşlarla ortak sıralama için sunucu gerekir.

## Yeni Nesil

Günümüze (2026) ulaşınca ya da Hızlı Tren çağında 22 şehri bağlayınca şirketini yeni nesle devredebilirsin. 1927’den yeniden başlarsın, ama başarına göre demiryolcu nişanı kazanırsın. Nişanlarla kalıcı güçler alırsın: daha büyük başlangıç kasası, ucuz hat, hızlı tren, yüksek yolcu geliri, düşük gider.

## Bakım ve arıza

Trenler çalıştıkça yıpranır. Durumu %50’nin altına inen tren yavaşlar, %40’ın altında arızalanıp bir ay yolda kalabilir. Filo sekmesinden bakım yaptırabilir ya da otomatik bakımı açık bırakabilirsin (biraz daha pahalı). Sivas Cer Atölyesi yıpranmayı, lokomotif fabrikası bakım masrafını azaltır.

## Bildirimler

Ayarlar (⚙) menüsünden bildirimleri açabilirsin. Oyun telefona uygulama olarak kuruluysa ve tarayıcı destekliyorsa, uzun süre girmediğinde kasandaki kazancı ve günlük ödülünü hatırlatır. Tarayıcılar bu arka plan hatırlatmasını her cihazda çalıştırmaz; Play Store sürümünde tam desteklenecek. Oyuna geri döndüğünde ayrıca seni bekleyenlerin (günlük ödül, görevler, bakım bekleyen trenler) bir özetini görürsün.

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
