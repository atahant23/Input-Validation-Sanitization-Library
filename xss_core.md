# Context-Aware XSS Core / Bağlam Duyarlı XSS Çekirdeği

## Purpose / Amaç

Mitigates Cross-Site Scripting attacks via context-aware sanitation and recursive decoding algorithms.
Cross-Site Scripting (XSS) saldırılarını bağlam duyarlı temizleme ve döngüsel kod çözme algoritmalarıyla engeller.

## How It Works / Nasıl Çalışır

Step-by-step explanation / Adım adım açıklama:
1. Decodes incoming strings using recursive URL unquoting and HTML unescaping to counter obfuscation layers. 
/ Gelen metinleri, kod gizleme katmanlarını bozmak için döngüsel URL ve HTML kod çözme işlemlerinden geçirir.
2. Strips malicious tags (script, iframe, svg, object) using case-insensitive greedy regular expressions.
/ Büyük/küçük harfe duyarsız agresif düzenli ifadeler kullanarak zararlı etiketleri (script, iframe, svg, object) kazır.
3. Evaluates and applies contextual validation rules based on the destination target zone (HTML body, HTML attribute, or JavaScript variable block). 
/ Verinin basılacağı hedef bölgeye göre (HTML gövdesi, HTML özniteliği veya JavaScript değişken bloğu) bağlamsal doğrulama kurallarını değerlendirir ve uygular.

## Usage / Kullanım

```python
# Example usage in Python / Python'da örnek kullanım
from sanitizer import EnterpriseSecurityEngine, SecurityLevel
clean_data = EnterpriseSecurityEngine.sanitize_xss("<script>alert(1)</script>", context="html_body", policy=SecurityLevel.HIGH)

## Output / Çıktı

Returns a completely sanitized HTML string where dangerous tags are removed and malicious event handlers are safely neutralized.
Tehlikeli etiketlerin kaldırıldığı ve zararlı olay tetikleyicilerinin güvenli bir şekilde etkisiz hale getirildiği, tamamen temizlenmiş bir HTML metni döndürür.

## Known Limitations / Bilinen Kısıtlamalar

- Paranoid policy level might aggressively strip legitimate non-alphanumeric punctuation marks.
- Does not automatically parse complex nested JSON schemas unless explicitly serialized to string.
- Paranoid politika seviyesi, meşru olan alfanumerik olmayan noktalama işaretlerini agresif bir şekilde temizleyebilir.
- Açıkça metne (string) dönüştürülmediği sürece karmaşık iç içe geçmiş JSON şemalarını otomatik olarak ayrıştırmaz.
