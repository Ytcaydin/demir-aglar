# Demir Ağlar: Demiryolu Patronu

Türk şehirleriyle, şehirlerin ihtiyaçlarını taşıyarak büyüttüğün bir demiryolu tycoon oyunu. Yeni oyunda iki başlangıç var: **1856 Osmanlı** (Anadolu'nun ilk demiryolu İzmir–Aydın'ı inşa ederek) ya da **1927 Cumhuriyet** (İstanbul–Eskişehir hattıyla).

## Osmanlı dönemi (1856–1922)

- 23 Eylül 1856'da İzmir–Aydın imtiyazıyla başlarsın. Hat 1857'de başlayıp 1866'da tamamlanan inşaatı kısa bir prologla izlersin; yolda Alsancak Garı ve zorlu arazi için kararlar verirsin. İstersen "Hızlandır" ya da "Açılışa geç".
- Hat açılınca oyun başlar. Yolda Süveyş Kanalı (1869), Şark Demiryolları'nın İstanbul–Edirne hattıyla rakip olarak gelişi (1873), Osmanlı'nın iflası (1875), 93 Harbi (1877), Düyun-u Umumiye (1881), Anadolu Demiryolu imtiyazı (1888), Ankara'ya demiryolu (1893), Hicaz Demiryolu (1908), Birinci Dünya Savaşı (1914) ve Ankara'da Meclis'in açılışı (1920) karar kartı olarak gelir.
- 6 şehri bağlayınca 1923'e atlayabilirsin. 29 Ekim 1923'te Cumhuriyet ilan edilir; ardından demiryollarının millîleştirilmesi (rakibin hatlarını yarı fiyatına alma) ve Devlet Demiryolları'nın kuruluşu (1927) gelir. Oyun oradan günümüze devam eder.
- İmtiyaz sözleşmesi (kilometre garantisi): Osmanlı döneminde hat bakımının %70'ini ve tren giderlerinin %25'ini devlet üstlenir. Cumhuriyet'ten sonra 12 yıl içinde azalıp biter. Otomatik oyuncuyla yapılan denemelerde bu destek olmadan Osmanlı oyunu 1880'lerde batıyordu (aşağıda "Denge").
- Haritaya Aydın şehri eklendi. Osmanlı döneminde ekran daha koyu bir gravür tonundadır.
- Eski kayıtlar olduğu gibi açılır; 1927 oyunu olarak devam eder.

## Osmanlı senaryoları

Senaryo sekmesinde üç yeni görev var:
- **Ege Ovası (1866):** İzmir–Aydın hattını Denizli'ye ve Antalya'ya uzat, kasayı 1.500 bin ₺'ye çıkar (84 ay).
- **Bağdat Demiryolu (1903):** Konya'dan Toroslar'ı aşıp Adana'ya, oradan Gaziantep'e ulaş, kasayı 1.200 bin ₺'ye çıkar (60 ay).
- **Kurtuluş Savaşı İkmali (1921):** Az parayla Ankara'yı Kayseri ve Sivas'a bağla, kasa eksiye düşmesin (30 ay).

## Dil

Oyun Türkçe ve İngilizce. İlk açılışta cihazın diline göre seçilir (Türkçe değilse İngilizce); Ayarlar'daki "DİL" düğmesiyle değişir. Adrese `?lang=en` ya da `?lang=tr` eklemek de olur.

- Metinler kodda `_t('…')` ya da ``_t`…` `` ile sarılı; İngilizceleri `index.html` başındaki `EN_DICT` sözlüğünde. Anahtar Türkçe metnin kendisi, `{0}`, `{1}` yer tutucuları şablondaki `${…}` değerleri.
- Yeni metin eklerken: metni `_t` ile sar, `EN_DICT`'e İngilizcesini ekle. Eksikleri bulmak için: `npm i --no-save acorn acorn-walk && node tools/i18n-check.js`
- İngilizce mağaza metni: `magaza/listing-en.md`.

## CrazyGames sürümü

Her derlemede GitHub Releases'a APK'nın yanında **DemirAglar-crazygames.zip** da eklenir (`tools/build_crazygames.py`). Bu paket CrazyGames SDK v3 ile çalışır: ödüllü reklamlar CrazyGames reklamı olur, dil oyuncunun diline göre seçilir, kayıt CrazyGames bulutuna yazılır, oyun hep tam ekran düzeninde açılır. Yükleme adımları, kapak görselleri ve İngilizce sayfa metinleri `magaza/crazygames/` klasöründe.

Yatay ekranda (bilgisayar, yatay tablet) tam ekran menüsü sağda panel olarak açılır.

## Ses

Müzik ve tren sesleri çağa göre değişir: Osmanlı'da ud gibi tınlayan hicaz, 1927'de hicaz, Kalkınma'da klarnet gibi rast, Elektrik çağında yumuşak synth, Hızlı Tren çağında çan arpeji. Buharlıda düdük, dizelde korna, elektrikli trenlerde iki tonlu elektronik ses çalar.

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

## Grafik

- **Çağa göre renk tonu:** 1927'de eski fotoğraf (sepya, hafif gren), 1950'lerde kartpostal, 1970'lerde film tonu, günümüzde canlı renkler. Ayarlar (⚙) → Renk tonu ile kapatılabilir.
- **Karayolu ve havayolu rakipleri görünür:** Kalkınma çağından itibaren şehirler arasında yollar, kamyonlar ve otobüsler; Elektrik çağından itibaren havalimanları arasında uçan uçaklar.
- **Hava olayları:** Kar fırtınasıyla kapanan hatta kar yağar, selde yağmur ve kara bulutlar görünür.
- **Fotoğraf modu:** Haritadaki 📷 düğmesi arayüzü gizler. İstediğin açıyı bul, isteğe bağlı şehir adlarıyla 3D fotoğraf çek ve paylaş.
- **Açılış uçuşu:** Yeni oyunda kamera Doğu'dan Ankara'ya, oradan ilk hattına uçar; dönüşte kısa bir iniş yapar. Dokununca atlanır.
- **Büyüme ve inşaat:** Büyüyen şehrin binaları yerden yükselir, yanında bir süre vinç çalışır. Büyük projelerin inşaatı beş aşamada görünür.
- Göller artık su gibi görünür, deniz dalgaları tekrar etmez, ekran kenarındaki etiketler kesilmez.
- Araç, uçak ve yağış miktarı Ayarlar → Grafik seviyesine göre azalır.

## Tam ekran ve tanıtımlar

- Haritanın sağ üstündeki köşeli düğme oyunu **tam ekran** yapar. Tarih, kasa ve hız üstte kalır; Seçim, Görevler, Şirket, Filo, Albüm ve Mağaza alttaki çubuktan açılır. Telefonun geri tuşu önce açık paneli, sonra tam ekranı kapatır.
- Bir şehre dokununca haritada 2-3 cümlelik **şehir tanıtımı** ve yöresel ürünü çıkar. Aynı tanıtım şehir kartında da durur.
- Kapadokya, Pamukkale, Efes, Sümela, Nemrut, Truva ve Şehitler Abidesi etiketlerine ya da modellerine dokununca **turistik yerin kısa tanıtımı** açılır.
- Turistik yerler ziyarete açıldıkları ya da dünyaca tanındıkları yıldan itibaren haritada belirir: Efes 1869, Truva 1871, Nemrut 1953, Pamukkale 1957, Şehitler Abidesi 1960, Kapadokya 1985, Sümela 1986. Kapadokya balonları 1991'den sonra uçar. Açılmamış bir yer, şehir kartında "yakında" diye görünür.

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

**Yedek:** Ayarlar (⚙) → YEDEK. "Kodu kopyala" ya da "Dosya olarak indir" ile bütün ilerlemen (oyun, rekorlar, albüm, nesiller, ayarlar) tek bir metin olur; yeni cihazda "Koddan yükle" ya da "Dosyadan yükle" ile devam edersin. Yükleme, bu cihazdaki oyunun yerine geçer; önce onay ister.

## Denge

Oyunun ekonomisi, tarayıcıda gerçek oyun kodunu çalıştıran otomatik bir oyuncuyla (hat kurar, tren alır, bakım yapar, tren yükseltir) 1866–2026 arası denendi. Bulgular:

- Hat başına 1 tren oynayan oyuncu Osmanlı'dan günümüze rahat geçer; 2 tren/hat dar bir marjla geçer; 3 tren/hat batar. Yani gereğinden fazla tren almak ceza getirir, bu bilerek böyle bırakıldı.
- Osmanlı'da (1866–1923) buharlıdan başka tren olmadığı için ekonomi 1927 başlangıcından daha dardı; bu yüzden imtiyaz sözleşmesi desteği eklendi.
- Otomatik oyuncu mal ihtiyaçlarını (buğday, kömür) yönetmediği için şehirleri büyütemiyor; gerçek oyuncu bunu yaparak çok daha fazla kazanır. Bu yüzden sonuçlar "en kötü makul oyun" gibi okunmalı.

## Android uygulaması (APK)

Her güncellemede GitHub, `android/` klasöründeki projeden APK'yı kendisi derler ve **Releases** sayfasına koyar. En son sürüm her zaman şu adrestedir:

`https://github.com/Ytcaydin/demir-aglar/releases/latest/download/DemirAglar.apk`

Telefonda bu bağlantıyı aç, dosyayı indir ve kur. İlk seferde Android "bilinmeyen kaynaklardan yükleme" izni ister. Uygulama internetsiz çalışır, çünkü 3D kütüphanesi ve yazı tipleri içine gömülüdür. Paylaşım düğmesi telefonun kendi paylaşım menüsünü açar.

Notlar:
- APK, depodaki `demir-aglar-sideload.keystore` test anahtarıyla imzalanır. Böylece yeni sürümler eskisinin üzerine kurulur ve kayıtların silinmez. Bu anahtar herkese açık olduğu için **Play Store'da kullanılmamalı**; Play Store için kendi gizli yükleme anahtarını oluştur ve AAB derle.
- Uygulamada web bildirimleri yok; bildirim düğmesi gizlenir.
- Tarayıcıdaki kayıt uygulamaya taşınmaz; uygulama kendi kaydıyla başlar.

## Play Store için

Play Store'a yüklemek için imzalı bir AAB dosyası gerekir. Hazırlık tamam; senin yapacakların:

1. **Geliştirici hesabı:** play.google.com/console adresinden hesap aç (tek seferlik 25 USD). Kişisel hesapta yayından önce 12 test kullanıcısıyla 14 gün kapalı test şartı var.
2. **Yükleme anahtarı üret** (bilgisayarında bir kez, Java gerekir):
   `keytool -genkeypair -v -keystore demir-aglar-play.keystore -alias demiraglar -keyalg RSA -keysize 2048 -validity 10000`
   Sorulan şifreyi ve dosyayı güvenli bir yere yedekle. Dosyayı kaybedersen Play'e destek isteği açman gerekir; depoya asla koyma.
3. **Anahtarı GitHub'a ver:** dosyayı base64 yap (`base64 -w0 demir-aglar-play.keystore`, Mac'te `base64 -i dosya`). Depo → Settings → Secrets and variables → Actions → New repository secret ile şu dört secret'ı ekle: `PLAY_KEYSTORE_BASE64` (base64 çıktısı), `PLAY_KEYSTORE_PASSWORD`, `PLAY_KEY_ALIAS` (`demiraglar`), `PLAY_KEY_PASSWORD`.
4. **AAB üret:** Actions → "Play Store AAB" → Run workflow. Bitince sayfanın altındaki `DemirAglar-aab` dosyasını indir (zip içinde DemirAglar.aab).
5. Play Console'da uygulamayı oluştur, "Play Uygulama İmzalama"yı kabul et, AAB'yi yükle. Mağaza metinleri `magaza/liste-tr.md` içinde hazır.
6. **Gizlilik politikası adresi:** Depo → Settings → Pages → Branch: main, klasör: / seç. Birkaç dakika sonra `https://ytcaydin.github.io/demir-aglar/gizlilik.html` açılır; bu adresi Play Console'a yaz.

Notlar:
- Uygulama Android 16'yı (API 36) hedefler; Play'in 31 Ağustos 2026 sonrası şartını karşılar.
- APK (telefona elle kurulum) ile AAB (Play Store) farklı anahtarlarla imzalanır; APK, depodaki herkese açık test anahtarını kullanır. Play'e yalnızca AAB gönder.
- Ödüllü reklam (AdMob) Android uygulamasında bağlı. Kimlik verilmezse Google test reklamı çıkar; kendi kimliklerin için `magaza/liste-tr.md` → "AdMob kurulumu". Web sürümünde reklam düğmeleri hâlâ 3 saniyelik demo.
