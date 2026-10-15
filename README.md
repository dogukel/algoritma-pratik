# Algoritma Pratik
Python öğrenirken çözdüğüm algoritma sorularını tuttuğum repo.

## İlk Tekrar Etmeyen Karakter
**Problem:** Bir kelime girdisinde tekrar etmeyen ilk harfin kaçıncı sırada olduğunu yaz, eğer tekrarsız karakter yoksa -1 çıktısı al.

**Çözüm:** Her harfin kaç kez geçtiğini bir dict'te sayıyorum, ikinci döngüde tekrar etmeyen karakteri bulduğunda döngüyü bitirip kaçıncı index olduğunu return ediyorum. Fonksiyon için iki ayrı döngü var çünkü bir harfin tekrar edip etmediğini görmek için tüm kelimeyi tararız, döngüler birleşik olsaydı kelimeyi tarayamadan döngüyü bitirebilir, hatalı sonuç verebilirdi.

**Karmaşıklık:** Zaman O(n) - Alan O(n)

**Örnek:** `"elma"` → `0`, `"aabb"` → `-1`

**Nasıl çalıştırılır:** `python3 ilk_tekrarsiz_karakter.py`

## Parantez Dengesi
**Problem:** Bir parantez dizisinde her açılan parantezin aynı tipte ve doğru sırayla kapanıp kapanmadığını kontrol et, sonucu True/False döndür.

**Çözüm:** Stack kullanılır. Açılış parantezleri stack'e eklenir. Kapanış parantezi geldiğinde stack'in en üstündeki açılışla eşleşmesi gerekir, stack boşsa ya da üstteki eşi değilse False döner, eşse üstteki çıkarılır. Döngü sonunda stack boşsa tüm parantezler kapanmıştır ve True döner.

**Karmaşıklık:** Zaman O(n) - Alan O(n)

**Örnek:** `"([]{})"` → `True`, `"([)]"` → `False`

**Nasıl çalıştırılır:** `python3 parantez_dengesi.py`

## Two Sum
**Problem:** Bir sayı listesi ve bir hedef sayı veriliyor. Toplamı hedef sayıya eşit olan iki sayının index'lerini döndür. Her girdide tam bir çözüm olduğu varsayılır ve aynı eleman iki kez kullanılamaz.

**Çözüm 1(Brute Force):** İç içe döngü kullanılır(Brute Force denmesinin sebebi tüm sayı çiftlerinin tek tek denenmesidir). İç döngüde tüm girdiyi gezerek üst döngüdeki sayı toplanıp target'a eşit mi bakılır, bu sayıların index'leri döner.

**Karmaşıklık:** Zaman O(n^2) - Alan O(1)

**Çözüm 2(Hash Map):** Dict kullanılır(Avantajı; liste bir kez gezilir). Tamamlayıcı değişkeni tanımlanarak dict içinde bu tamamlayıcı var mı sorgusu yapılır. Varsa iki sayının toplamı olan index'ler return edilir, yoksa şu anki sayı index'iyle dict'e kaydedilir.

**Karmaşıklık:** Zaman O(n) - Alan O(n)

**Örnek:** `[2, 7, 11, 15], 9` → `[0, 1]`

**Nasıl çalıştırılır:** `python3 two_sum.py`