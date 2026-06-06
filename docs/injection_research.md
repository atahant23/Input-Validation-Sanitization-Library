# Research Notes / Araştırma Notları



> Module / Konu: Web Application Injection Vectors & WAF Evasion Techniques / Web Uygulaması Enjeksiyon Vektörleri & WAF Atlatma Teknikleri

> Date / Tarih: 2026-06-06



---



## What I'm Investigating / Araştırdığım Konu



Deep architectural analysis of multi-layer encoding obfuscations used by attackers to bypass basic input firewalls, specifically focusing on XSS context shifting, SQLi token parsing, and RCE operator execution paths.

---

Saldırganların temel girdi güvenlik duvarlarını atlatmak için kullandıkları çok katmanlı kod gizleme işlemlerinin derin mimari analizi; özellikle XSS bağlam kayması, SQLi belirteç ayrıştırma ve RCE operatör yürütme yollarına odaklanılmıştır.



## Resources Found / Bulunan Kaynaklar



- [OWASP Top 10:2021 Core Guidelines](https://owasp.org/www-project-top-ten/) — Structural understanding of security code injection paradigms. / Güvenlik kodu enjeksiyon paradigmalarının yapısal olarak anlaşılması.

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — Practical references for input filtering bypass and validation evasion maps. / Girdi filtreleme bypassı ve doğrulama atlatma haritaları için pratik referanslar.



## Key Findings / Temel Bulgular



1. Attackers routinely employ recursive multi-layer encodings (Hex combined with Double URL loops) to pass signatures under naive single-pass sanitizers. / Saldırganlar, basit tek geçişli temizleyicilerin altından imzaları geçirmek için rutin olarak döngüsel çok katmanlı kodlamalar (Çift URL döngüleriyle birleştirilmiş Hex) kullanırlar.

2. Context-driven data visualization requires dynamic escaping rules; string processing safe within raw text outputs executes immediately if injected into an attribute token. / Bağlam odaklı veri görselleştirme dinamik kaçış kuralları gerektirir; ham metin çıktılarında güvenli olan dize işleme, bir öznitelik belirtecine enjekte edilirse anında yürütülür.



## Dead Ends / Çıkmaz Sokaklar



Things I tried that didn't work and why / Denediğim ama çalışmayan şeyler ve nedenleri:

- Tried relying on basic string replace loops → didn't work because recursive nested constructs (such as `<scr<script>ipt>`) completely bypassed simple single-pass cleaners. / Temel dize değiştirme (replace) döngülerine güvenmeyi denedim → çalışmadı çünkü iç içe geçmiş döngüsel yapılar (örneğin `<scr<script>ipt>`) basit tek geçişli temizleyicileri tamamen atlattı.

- Tried blocking every quotation mark inside query strings → failed because legal names or standard punctuation inputs broke normal platform workflows. / Sorgu dizeleri içindeki her tırnak işaretini engellemeyi denedim → başarısız oldu çünkü meşru isimler veya standart noktalama girdileri normal platform iş akışlarını bozdu.



## Questions Remaining / Kalan Sorular



- [ ] How to effectively optimize large-scale regular expression iterations under heavy multi-threaded production requests? / Yoğun çoklu iş parçacıklı üretim talepleri altında büyük ölçekli düzenli ifade yinelemeleri etkili bir şekilde nasıl optimize edilir?

- [ ] Is it feasible to transition signature matching logic fully into machine-learning token classifiers for zero-day defense? / Sıfırıncı gün savunması için imza eşleştirme mantığını tamamen makine öğrenimi belirteç sınıflandırıcılarına geçirmek fizibil midir?



## 50-Step Breakdown / 50 Adımlık Çözümleme



1. Step 1: What is application input validation? / Adım 1: Uygulama girdi doğrulaması nedir?

2. Step 2: Why do software filters fail against injection vectors? / Adım 2: Yazılım filtreleri enjeksiyon vektörlerine karşı neden başarısız olur?

3. Step 3: What is the core mechanism behind an injection vulnerability? / Adım 3: Bir enjeksiyon zafiyetinin arkasındaki temel mekanizma nedir?

4. Step 4: How does the OWASP Top 10 classification evaluate web injection? / Adım 4: OWASP Top 10 sınıflandırması web enjeksiyonunu nasıl değerlendirir?

5. Step 5: What is a structural query mutation? / Adım 5: Yapısal sorgu mutasyonu nedir?

6. Step 6: How do parameter strings trick database parsing components? / Adım 6: Parametre dizeleri veritabanı ayrıştırma bileşenlerini nasıl aldatır?

7. Step 7: What is the primary role of single quotes in an SQL injection context? / Adım 7: SQL injection bağlamında tek tırnak işaretinin temel rolü nedir?

8. Step 8: How do conditional boolean payloads (such as 1=1) bypass auth routines? / Adım 8: Koşullu mantıksal payload'lar (1=1 gibi) kimlik doğrulama rutinlerini nasıl atlatır?

9. Step 9: What is the risk associated with a blind SQLi vector? / Adım 9: Blind SQLi vektörü ile ilişkili risk nedir?

10. Step 10: How do attackers utilize UNION statements to extract structural database properties? / Adım 10: Saldırganlar yapısal veritabanı özelliklerini çıkarmak için UNION ifadelerini nasıl kullanırlar?

11. Step 11: What is database comment stripping? / Adım 11: Veritabanı yorum satırı temizleme nedir?

12. Step 12: How do operators like hyphens or hashes affect standard syntax lines? / Adım 12: Tire veya kare gibi operatörler standart sözdizimi satırlarını nasıl etkiler?

13. Step 13: Why is static keyword blacklisting fundamentally insufficient? / Adım 13: Statik anahtar kelime kara listeye alması neden temelden yetersizdir?

14. Step 14: What is a Cross-Site Scripting exploit? / Adım 14: Cross-Site Scripting zafiyeti nedir?

15. Step 15: How does Stored XSS execute inside a victim browser? / Adım 15: Stored XSS, kurbanın tarayıcısında nasıl yürütülür?

16. Step 16: What differentiates Reflected XSS from Stored XSS vectors? / Adım 16: Reflected XSS'i Stored XSS vektörlerinden ayıran nedir?

17. Step 17: What is a Document Object Model (DOM) based XSS mutation? / Adım 17: Belge Nesnesi Modeli (DOM) tabanlı XSS mutasyonu nedir?

18. Step 18: How do browsers parse the structural initialization of script elements? / Adım 18: Tarayıcılar script öğelerinin yapısal başlatılmasını nasıl ayrıştırır?

19. Step 19: What is an HTML event handler element? / Adım 19: HTML olay işleyici (event handler) öğesi nedir?

20. Step 20: Why do attackers target elements like onerror or onload for payloads? / Adım 20: Saldırganlar payload'lar için neden onerror veya onload gibi öğeleri hedefler?

21. Step 21: How does a JavaScript pseudo-protocol execution trigger malicious logic? / Adım 21: Bir JavaScript yalancı protokol (pseudo-protocol) yürütmesi zararlı mantığı nasıl tetikler?

22. Step 22: What is an OS Command Injection framework? / Adım 22: OS Komut Enjeksiyonu yapısı nedir?

23. Step 23: How do applications inadvertently expose system shell processing layers? / Adım 23: Uygulamalar sistem kabuğu (shell) işleme katmanlarını bilmeden nasıl açığa çıkarır?

24. Step 24: What constitutes a shell command chaining symbol? / Adım 24: Bir kabuk komut zincirleme sembolünü ne oluşturur?

25. Step 25: How does a semicolon alter operating system instruction flows? / Adım 25: Noktalı virgül işletim sistemi komut akışlarını nasıl değiştirir?

26. Step 26: What is the functionality of logical AND/OR symbols in a command prompt? / Adım 26: Komut satırında mantıksal VE/VEYA sembollerinin işlevi nedir?

27. Step 27: How does an attacker trigger subshell generation using backticks? / Adım 27: Bir saldırgan ters tırnak kullanarak alt kabuk (subshell) üretimini nasıl tetikler?

28. Step 28: What is Server-Side Request Forgery? / Adım 28: Server-Side Request Forgery (SSRF) nedir?

29. Step 29: How do external requests fetch records from an internal infrastructure? / Adım 29: Harici istekler iç altyapıdan kayıtları nasıl getirir?

30. Step 30: What is the structural significance of the cloud metadata IP block? / Adım 30: Bulut meta veri IP bloğunun yapısal önemi nedir?

31. Step 31: What is a Path Traversal exploit mechanism? / Adım 31: Path Traversal sömürü mekanizması nedir?

32. Step 32: How do dot-dot-slash characters bypass directory separation walls? / Adım 32: Nokta-nokta-eğik çizgi (../) karakterleri dizin ayırma duvarlarını nasıl atlatır?

33. Step 33: What is file extension verification manipulation? / Adım 33: Dosya uzantısı doğrulama manipülasyonu nedir?

34. Step 34: Why do double extensions succeed against simple terminal boundaries? / Adım 34: Çift uzantılar basit uç nokta sınırlarına karşı neden başarılı olur?

35. Step 35: What is multi-layered encoding obfuscation strategy? / Adım 35: Çok katmanlı kodlama gizleme stratejisi nedir?

36. Step 36: How does double URL encoding circumvent basic parameter checks? / Adım 36: Çift URL kodlaması temel parametre kontrollerini nasıl atlatır?

37. Step 37: What is the function of HTML entity parsing routines? / Adım 37: HTML varlık (entity) ayrıştırma rutinlerinin işlevi nedir?

38. Step 38: Why must a sanitization engine execute recursive decoding? / Adım 38: Bir temizleme motoru neden döngüsel kod çözme yürütmelidir?

39. Step 39: What is a Web Application Firewall policy matrix? / Adım 39: Web Uygulaması Güvenlik Duvarı politika matrisi nedir?

40. Step 40: How do runtime strictness matrices adjust operational safety blocks? / Adım 40: Çalışma zamanı katılık matrisleri operasyonel güvenlik bloklarını nasıl ayarlar?

41. Step 41: What guarantees does alphanumeric isolation provide under high threat states? / Adım 41: Yüksek tehdit durumlarında alfanumerik izolasyon hangi garantileri sağlar?

42. Step 42: What is context-aware sanitization processing? / Adım 42: Bağlam duyarlı temizleme işlemi nedir?

43. Step 43: Why must an attribute field execute quotation-to-entity translations? / Adım 43: Bir öznitelik alanı neden tırnaktan varlığa (entity) dönüşümleri yürütmelidir?

44. Step 44: How does backslash manipulation protect embedded scripting fields? / Adım 44: Ters eğik çizgi manipülasyonu gömülü betik alanlarını nasıl korur?

45. Step 45: What is signature pattern validation engineering? / Adım 45: İmza kalıbı doğrulama mühendisliği nedir?

46. Step 46: How do regular expressions parse text sequences efficiently? / Adım 46: Düzenli ifadeler metin dizilerini etkili bir şekilde nasıl ayrıştırır?

47. Step 47: What is a false positive error within threat telemetry reporting? / Adım 47: Tehdit telemetri raporlamasında hatalı pozitif (false positive) hata nedir?

48. Step 48: What represents a false negative execution path inside a firewall? / Adım 48: Bir güvenlik duvarı içindeki hatalı negatif (false negative) yürütme yolunu ne temsil eder?

49. Step 49: What is structured event security logging? / Adım 49: Yapılandırılmış olay güvenliği günlüklemesi nedir?

50. Step 50: How can sandbox containment shield deployment platforms from systemic RCE damage? / Adım 50: Sandbox yalıtımı, dağıtım platformlarını sistemik RCE hasarından nasıl koruyabilir?
