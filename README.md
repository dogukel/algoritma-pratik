# Algoritma Pratik
Python öğrenirken çözdüğüm algoritma sorularını tuttuğum repo.

## İlk Tekrar Etmeyen Karakter
**Problem:** Bir kelime girdisinde tekrar etmeyen ilk harfin kaçıncı sırada olduğunu yaz, eğer tekrarsız karakter yoksa -1 çıktısı al.

**Çözüm:** Her harfin kaç kez geçtiğini bir dict'te sayıyorum, ikinci döngüde tekrar etmeyen karakteri bulduğunda döngüyü bitirip kaçıncı index olduğunu return ediyorum. Fonksiyon için iki ayrı döngü var çünkü bir harfin tekrar edip etmediğini görmek için tüm kelimeyi tararız, döngüler birleşik olsaydı kelimeyi tarayamadan döngüyü bitirebilir, hatalı sonuç verebilirdi.

**Karmaşıklık:** Zaman O(n) - Alan O(n)

**Örnek:** "elma"` → `0`, `"aabb"` → `-1``

**Nasıl çalıştırılır:** `python3 ilk_tekrarsiz_karakter.py`

## Parantez Dengesi
**Problem:** Bir parantez dizisinde her açılan parantezin aynı tipte ve doğru sırayla kapanıp kapanmadığını kontrol et, sonucu True/False döndür.

**Çözüm:** Stack kullanılır. Açılış parantezleri stack'e eklenir. Kapanış parantezi geldiğinde stack'in en üstündeki açılışla eşleşmesi gerekir: stack boşsa ya da üstteki eşi değilse False döner, eşse üstteki çıkarılır. Döngü sonunda stack boşsa tüm parantezler kapanmıştır ve True döner.

**Karmaşıklık:** Zaman O(n) - Alan O(n)

**Örnek:** "([]{})"` → `True`, `"([)]"` → `False``

**Nasıl çalıştırılır:** `python3 parantez_dengesi.py`