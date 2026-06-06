# Dual-Layer SQLi Prevention Engine / Çift Katmanlı SQLi Engelleme Motoru

## Purpose / Amaç

Detects and blocks structural SQL Injection patterns and quote manipulations before they reach the data layer.
---
SQL Injection kalıplarını ve tırnak manipülasyonlarını veri katmanına ulaşmadan önce tespit eder ve engeller.

## How It Works / Nasıl Çalışır

Step-by-step explanation:
1. Inspects the parameter string and actively strips dangerous SQL commentary sequences like dashes or slash-stars.
2. Normalizes input by doubling single and double quote instances to break escape mechanics.
3. Scans structural input tokens against a greedy signature block targeting malicious commands and boolean bypass loops.
---
Adım adım açıklama:
1. Parametre metnini inceler ve tireler veya eğik çizgi-yıldızlar gibi tehlikeli SQL yorum satırı dizilimlerini aktif olarak temizler.
2. Kaçış mekanizmalarını bozmak için tek ve çift tırnak işaretlerini çiftleyerek girdiyi normalize eder.
3. Zararlı komutları ve mantıksal bypass döngülerini hedef alan agresif bir imza bloğuna karşı yapısal girdi belirteçlerini tarar.

## Usage / Kullanım

```python
from sanitizer import EnterpriseSecurityEngine, SecurityLevel
clean_query = EnterpriseSecurityEngine.sanitize_sqli("admin' OR '1'='1", policy=SecurityLevel.HIGH)

## Output / Çıktı

Blocks execution entirely and returns an error tracking flag, preventing shell subsystem spawning.
Kabuk (shell) alt sisteminin başlatılmasını önleyerek yürütmeyi tamamen engeller ve bir hata izleme bayrağı döndürür.

## Known Limitations / Bilinen Kısıtlamalar

- Legitimate data validation workflows passing logical math pipes or script parameters may get blocked.
- Does not perform structural file system directory access path authentication checks.
- Mantıksal matematik boruları (pipe) veya betik parametreleri geçiren meşru veri doğrulama iş akışları engellenebilir.
- Yapısal dosya sistemi dizin erişim yolu yetkilendirme kontrollerini gerçekleştirmez.
