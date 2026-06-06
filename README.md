<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="docs/assets/istinye-university-logo.webp" alt="Istinye University" width="180"/>
  </a>

  # Input Validation & Sanitization Library / Girdi Doğrulama & Sanitizasyon Kütüphanesi

  ![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
  ![Language](https://img.shields.io/badge/Language-[Rust|Python|Go]-blue?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
  ![Course](https://img.shields.io/badge/Course-BGT208-purple?style=flat-square)
  ![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)
</div>

---

## 🎓 Instructor / Danışman

| | |
|---|---|
| **Name / Ad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **Email** | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| **LinkedIn** | [keyvanarasteh](https://www.linkedin.com/in/keyvanarasteh/) |
| **Website** | [qline.tech](https://qline.tech) |

---

## 👤 Student / Öğrenci

| | |
|---|---|
| **Name / Ad Soyad** | Atahan Turna |
| **Student ID / Öğrenci No** | `***0191***` |
| **GitHub** | [@katahant23](https://github.com/atahant23) |
| **Email** | [atahanturna@hotmail.com](mailto:atahanturna@hotmail.com) |
| **LinkedIn** | [Atahan Turna](https://www.linkedin.com/in/atahan-turna-077051283//) |


---

## 📚 Course Information / Ders Bilgileri

| | |
|---|---|
| **Course Name / Ders Adı** | Secure Web Development / Güvenli Web Yazılımı Geliştirme |
| **Course Code / Ders Kodu** | BGT208 |
| **Credits / Kredi** | 3 ECTS |
| **Semester / Dönem** | 2025-2026 Spring / 2025-2026 Bahar |
| **Institution / Üniversite** | [Istinye University](https://istinye.edu.tr) |

---

## 📋 Project Overview / Proje Özeti

This project is a lightweight, zero-dependency security library designed to act as a defensive barrier against input-based web vulnerabilities. Built entirely on Python's native modules, it filters and validates raw user data before it reaches the application backend.

Bu proje, girdi tabanlı web zafiyetlerine karşı koruma sağlamak amacıyla geliştirilmiş, hafif yapılı ve harici bağımlılığı olmayan (zero-dependency) bir güvenlik kütüphanesidir. Tamamen Python'ın yerleşik modülleriyle inşa edilen bu yapı, ham kullanıcı verilerini arka uç mantığına ulaşmadan önce filtreler ve doğrular.

---

### 📁 Repository Structure / Repo Yapısı

```text
Input-Validation-Sanitization-Library/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── ROADMAP.md
├── requirements.txt
├── docs/
│   ├── modules/
│   │   ├── rce_shield.md
│   │   ├── sqli_core.md
│   │   └── xss_core.md
│   ├── references/
│   │   ├── .gitkeep
│   │   └── sources.md
│   └── research/
│       └── injection_research.md
├── reports/
│   └── security_alerts.json
└── src/
    ├── .gitkeep
    ├── main.py
    ├── sanitizer.py
    └── test_sanitizer.py
```

## 🚀 Getting Started / Kurulum

```
git clone https://github.com/atahant23/Input-Validation-Sanitization-Library.git
cd https://github.com/atahant23/Input-Validation-Sanitization-Library.git
cp .env.example .env
# Edit .env with your values / .env dosyasını doldurun
docker-compose up -d
```

---

Hiç canını sıkma, aslında bu kısımların hepsini yaptık! image_d44d24.png görselinde gördüğün yerler, hocanın şablon olarak bıraktığı ve senin doldurmanı beklediği taslak (placeholder) kısımları.

Sen kodları yazıp docs/ klasörünün altını doldurdun; şimdi tek yapmamız gereken README.md dosendeki bu "Deliverable 1", "Reference 1" gibi geçici isimleri silip, kendi yaptığın harika işleri oraya yazarak yanlarına kocaman birer ✅ (Tamamlandı) koymak.

README.md dosendeki o eski, taslak bölümü tamamen silip yerine doğrudan aşağıdaki güncel ve kurumsal içeriği yapıştırabilirsin:

Markdown
## 📊 Deliverables / Teslimler

| Item / Teslim Edilen Öğe | Status / Durum |
| :--- | :---: |
| **Context-Aware XSS Core Module** / Bağlam Duyarlı XSS Çekirdeği | ✅ |
| **Dual-Layer SQLi Prevention Engine** / Çift Katmanlı SQLi Motoru | ✅ |
| **RCE / OS Command Injection Shield** / RCE Komut Kalkanı | ✅ |
| **Automated Unittest Suite (`test_sanitizer.py`)** / Otomatik Test Paketi | ✅ |
| **SIEM Telemetry Logs (`security_alerts.json`)** / Real-time Loglama Sistemi | ✅ |
| **Dockerization & Orchestration Setup** / Docker ve Container Altyapısı | ✅ |

---

## 📚 Documentation / Belgeleme

All core architectural documents and research profiles are categorized under the following paths:
Tüm temel mimari belgeler ve araştırma profilleri aşağıdaki yollar altında kategorize edilmiştir:

* **Module Specifications / Modül Detayları:** [`docs/modules/`](./docs/modules/)
* **50-Step Deep Research Notes / 50 Adımlık Çözümleme:** [`docs/research/injection_research.md`](./docs/research/injection_research.md)
* **Official Compliance Sources / Kaynakça Belgesi:** [`docs/references/sources.md`](./docs/references/sources.md)

---

## 🔗 References / Kaynaklar

* [OWASP Top 10:2021 Core Guidelines](https://owasp.org/www-project-top-ten/) — Structural validation rules for code injection paradigms. / Kod enjeksiyon paradigmaları için yapısal doğrulama kuralları.
* [PortSwigger Web Security Academy](https://portswigger.net/web-security) — Core reference maps for advanced input filter evasion techniques. / Gelişmiş girdi filtresi atlatma teknikleri için temel referans haritaları.
* For the complete academic and technical bibliography, please see our dedicated [Sources Directory](./docs/references/sources.md). / Akademik ve teknik kaynakçanın tamamı için lütfen özel kaynak dizinimizi inceleyin.
