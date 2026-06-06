# RCE / OS Command Injection Shield / RCE Kalkanı

## Purpose / Amaç

Prevents Remote Code Execution vulnerabilities by intercepting malicious command chaining operators within system arguments.
---
Sistem argümanları içerisindeki zararlı komut zincirleme operatörlerini engelleyerek RCE açıklarını önler.

## How It Works / Nasıl Çalışır

Step-by-step explanation:
1. Resolves and normalizes string structures by parsing multi-layer text encodings.
2. Validates parameters against a static blacklist signature matrix of operating system instruction chaining symbols.
3. Instantly drops execution chains and sounds security telemetry alarms if an operator sequence matches.
---
Adım adım açıklama:
1. Çok katmanlı metin kodlamalarını ayrıştırarak dize yapılarını çözer ve normalize eder.
2. Parametreleri, işletim sistemi komut zincirleme sembollerinden oluşan statik bir kara liste imza matrisine karşı doğrular.
3. Bir operatör dizilimi eşleşirse yürütme zincirlerini anında düşürür ve güvenlik telemetrisi alarmlarını tetikler.

## Usage / Kullanım

```python
from sanitizer import EnterpriseSecurityEngine, SecurityLevel
clean_cmd = EnterpriseSecurityEngine.sanitize_os_command("127.0.0.1 ; whoami", policy=SecurityLevel.HIGH)

## Output / Çıktı

Blocks execution entirely and returns an error tracking flag, preventing shell subsystem spawning.
Kabuk (shell) alt sisteminin başlatılmasını önleyerek yürütmeyi tamamen engeller ve bir hata izleme bayrağı döndürür.

## Known Limitations / Bilinen Kısıtlamalar

- Legitimate data validation workflows passing logical math pipes or script parameters may get blocked.
- Does not perform structural file system directory access path authentication checks.
- Mantıksal matematik boruları (pipe) veya betik parametreleri geçiren meşru veri doğrulama iş akışları engellenebilir.
- Yapısal dosya sistemi dizin erişim yolu yetkilendirme kontrollerini gerçekleştirmez.
