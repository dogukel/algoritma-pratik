# Algoritma Pratik
Python öğrenirken çözdüğüm algoritma sorularını tuttuğum repo.
## Nasıl çalıştırılır
`python3 ilk_tekrarsiz_karakter.py`
## İlk Tekrar Etmeyen Karakter
**Problem:** Bir kelime girdisinde tekrar etmeyen ilk harfin kaçıncı sırada olduğunu yaz, eğer tekrarsız karakter yoksa -1 çıktısı al.

**Çözüm:** Her harfin kaç kez geçtiğini bir dict'te sayıyorum, ikinci döngüde tekrar etmeyen karakteri bulduğunda döngüyü bitirip kaçıncı index olduğunu return ediyorum. Fonksiyon için iki ayrı döngü var çünkü bir harfin tekrar edip etmediğini görmek için tüm kelimeyi tararız, döngüler birleşik olsaydı kelimeyi tarayamadan döngüyü bitirebilir, hatalı sonuç verebilirdi.