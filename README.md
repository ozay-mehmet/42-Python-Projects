# 🐍 42 Python Projects

Bu repository, 42 School eğitim sürecinde geliştirilen Python projelerini içermektedir. Amaç, Python programlama dilinin temelinden başlayarak daha ileri seviyelere kadar farklı programlama paradigmalarını uygulamalı olarak öğrenmektir.

Projeler, fonksiyonel programlama yaklaşımından başlayarak nesne yönelimli programlamaya (OOP), hata yönetimine, dosya ve veri işlemlerine, modül/paket mimarisine, tasarım desenlerine ve son olarak profesyonel Python ortam yönetimine kadar ilerleyen bir öğrenme sürecini temsil eder.

---

## 📂 Proje Yapısı

Repository, farklı seviyelere ayrılmış modüllerden oluşur:
```bash
42-Python-Projects/
│
├── Python-Module-0/   # Fonksiyonel programlama temelleri
├── Python-Module-1/   # Nesne yönelimli programlama (OOP)
├── Python-Module-2/   # Hata ve istisna (exception) yönetimi
├── Python-Module-3/   # Veri yapıları, argümanlar ve generator'lar
├── Python-Module-4/   # Dosya (I/O) işlemleri
├── Python-Module-5/   # Soyut sınıflar (Abstract Base Class)
├── Python-Module-6/   # Modüller ve paketler
├── Python-Module-7/   # Tasarım desenleri (Factory, Mixin, Strategy)
└── Python-Module-8/   # Sanal ortamlar ve bağımlılık yönetimi
```
Her klasör, belirli bir programlama konseptine odaklanır ve `exN` alt klasörleri o modülün ilerleyen egzersizlerini temsil eder.

---

## 🚀 Python-Module-0 – Fonksiyonel Programlama Temelleri

Bu bölüm, Python’un temel yapı taşlarını öğrenmeye odaklanır. "Garden" (bahçe) temalı küçük egzersizlerle giriş seviyesi kavramlar pekiştirilir.

### 📌 İçerik:
- Ekrana yazdırma ve kullanıcıdan girdi alma (`print`, `input`)
- Fonksiyon tanımlama ve çağırma
- Parametre kullanımı ve tip dönüşümleri (`int`, `str`)
- Koşullu ifadeler (`if` / `else`)
- Döngüler ile tekrarlı işlemler (`while`)
- İteratif ve recursive (özyinelemeli) çözüm yaklaşımları
- Varsayılan parametre değerleri ve return tipleri

### 🎯 Amaç:
Fonksiyon mantığını kavrayarak daha modüler ve okunabilir kod yazabilmek.

---

## 🧠 Python-Module-1 – Nesne Yönelimli Programlama (OOP)

Bu bölümde Python’un nesne yönelimli özellikleri, yine "Garden/Plant" temalı örnekler üzerinden çalışılır.

### 📌 İçerik:
- Sınıf (class) yapısı ve `__init__` metodu
- Nesne (object) oluşturma ve nitelik (attribute) tanımlama
- Encapsulation (kapsülleme) — private/protected alanlar (`_name`, `_height`)
- Factory yaklaşımıyla nesne üretimi
- İç içe (nested) sınıflar ile istatistik/analitik takibi
- Farklı bitki tiplerini modelleyen sınıf hiyerarşileri

### 🎯 Amaç:
Gerçek dünya problemlerini nesne yönelimli yaklaşımla modelleyebilmek.

---

## ⚠️ Python-Module-2 – Hata ve İstisna (Exception) Yönetimi

Bu bölüm, Python’da hataların nasıl yakalanacağı, fırlatılacağı ve yönetileceği üzerine kuruludur.

### 📌 İçerik:
- `try` / `except` blokları ile hata yakalama
- `raise` ile bilinçli olarak hata fırlatma
- Farklı hata (exception) tiplerini ayırt etme (`ValueError`, `TypeError` vb.)
- Kendi özel hata sınıflarını (custom exceptions) tanımlama
- `finally` bloğu ile kaynakların her koşulda temizlenmesi

### 🎯 Amaç:
Sağlam (robust) ve hataya dayanıklı programlar yazabilmek; beklenmeyen durumları öngörülebilir şekilde yönetebilmek.

---

## 🧮 Python-Module-3 – Veri Yapıları, Argümanlar ve Generator'lar

Bu bölümde komut satırı argümanları ve Python’un temel veri yapıları (list, set, dict, tuple) bir araya getirilir.

### 📌 İçerik:
- `sys.argv` ile komut satırı argümanlarını işleme
- Argümanları doğrulama ve hatalı girdileri ayıklama
- `list`, `set`, `dict`, `tuple` veri yapılarını amacına uygun kullanma
- List/set comprehension ile veri dönüştürme
- `random` modülü ile rastgele veri üretimi
- `yield` ve generator fonksiyonları ile "lazy" veri akışları oluşturma
- Type hinting (`typing` modülü) ile fonksiyon imzalarını netleştirme

### 🎯 Amaç:
Veriyi doğru yapı ile modelleyip, bellek ve performans açısından verimli akışlar (generator) tasarlayabilmek.

---

## 📁 Python-Module-4 – Dosya (I/O) İşlemleri

Bu bölüm, dosyaların güvenli biçimde okunması, yazılması ve yönetilmesine odaklanır.

### 📌 İçerik:
- `open()` ile dosya açma, okuma ve kapatma
- Dosya işlemlerinde hata yönetimi (`FileNotFoundError` vb.)
- Akış (stream) yönetimi ve kaynakların serbest bırakılması
- `with` bloğu (context manager) ile güvenli dosya erişimi
- Okuma/yazma modlarını parametreleştirme (`read` / `write`)

### 🎯 Amaç:
Dosya sistemiyle güvenli ve hataya dayanıklı şekilde etkileşime girebilmek.

---

## 🧱 Python-Module-5 – Soyut Sınıflar (Abstract Base Class)

Bu bölümde `abc` modülü kullanılarak soyutlama ve ortak arayüz (interface) tasarımı öğrenilir.

### 📌 İçerik:
- `abc.ABC` ve `@abc.abstractmethod` ile soyut sınıf tanımlama
- Ortak bir arayüz üzerinden farklı veri işleyicileri (`DataProcessor`) türetme
- `typing.Any` ve tip belirteçleriyle esnek ama kontrollü API tasarımı
- Veri doğrulama (`validate`), depolama ve akış (stream/pipeline) mantığının soyutlanması

### 🎯 Amaç:
Ortak bir sözleşme (contract) üzerinden birden fazla somut sınıfın tutarlı biçimde davranmasını sağlayabilmek.

---

## 📦 Python-Module-6 – Modüller ve Paketler

"Alchemy" (simya) temalı bu bölüm, Python’un modül ve paket sistemini derinlemesine ele alır.

### 📌 İçerik:
- `import` ile tekil modüllere erişim
- Paket (`package`) yapısı ve `__init__.py` dosyasının rolü
- İç içe (nested) alt paketler (`alchemy/grimoire`, `alchemy/transmutation`)
- Farklı import stillerinin karşılaştırılması (doğrudan modül, paket üzerinden, alt paket üzerinden erişim)
- Ad alanı (namespace) yönetimi ve modüller arası bağımlılıklar

### 🎯 Amaç:
Büyüyen bir proje için sürdürülebilir, iyi organize edilmiş modül/paket mimarisi kurabilmek.

---

## ⚔️ Python-Module-7 – Tasarım Desenleri (Design Patterns)

"Creature/Battle" temalı bu bölüm, OOP bilgisini gerçek tasarım desenleriyle birleştirir.

### 📌 İçerik:
- **Factory Pattern**: Soyut `CreatureFactory` üzerinden farklı yaratık ailelerinin üretilmesi
- **Mixin / Çoklu Kalıtım**: `HealCapability`, `TransformCapability` gibi yeteneklerin sınıflara eklenmesi
- **Strategy Pattern**: `BattleStrategy` arayüzü ile savaş davranışlarının (Normal, Aggressive, Defensive) çalışma zamanında değiştirilebilmesi
- Paketler arası (`ex0`, `ex1`, `ex2`) bileşenlerin bir araya getirilerek `battle.py` ve `tournament.py` senaryolarının kurgulanması
- Özel hata sınıfları ile (`StrategyError`) desen bazlı hata yönetimi

### 🎯 Amaç:
Yaygın tasarım desenlerini tanıyarak esnek, genişletilebilir ve bakımı kolay nesne yönelimli sistemler kurgulayabilmek.

---

## 🧰 Python-Module-8 – Sanal Ortamlar ve Bağımlılık Yönetimi

"Matrix" temalı bu bölüm, Python’u profesyonel bir geliştirme ortamında kullanmaya odaklanır.

### 📌 İçerik:
- `sys.prefix` / `sys.base_prefix` ile sanal ortam (virtual environment) tespiti
- `venv` oluşturma ve global ortamdan izole geliştirme
- `importlib` ve `importlib.metadata` ile bağımlılıkları dinamik olarak yükleme ve sürüm kontrolü
- `requirements.txt` ve `pyproject.toml` (Poetry) ile bağımlılık yönetimi (numpy, pandas, matplotlib)
- `.env` dosyaları ve `python-dotenv` ile ortam değişkenlerinin (environment variables) güvenli biçimde yönetilmesi
- `.gitignore` ile hassas/gereksiz dosyaların versiyon kontrolünden hariç tutulması

### 🎯 Amaç:
Gerçek dünya Python projelerinde bağımlılıkları, ortam değişkenlerini ve sanal ortamları profesyonel standartlara uygun şekilde yönetebilmek.

---

## 🧩 Öğrenilen Konseptler

Bu repo boyunca aşağıdaki temel yazılım kavramları uygulanmıştır:

- Fonksiyonel programlama
- Modüler kod yazımı
- Nesne yönelimli programlama (OOP): encapsulation, inheritance, polymorphism
- Hata ve istisna (exception) yönetimi, özel hata sınıfları
- Veri yapıları (list, set, dict, tuple) ve generator'lar
- Dosya (I/O) işlemleri ve context manager kullanımı
- Soyut sınıflar (Abstract Base Class) ile arayüz tasarımı
- Modül ve paket mimarisi
- Tasarım desenleri: Factory, Mixin, Strategy
- Sanal ortam ve bağımlılık yönetimi (venv, pip, Poetry, dotenv)
- Kod okunabilirliği ve düzeni
- Problem çözme ve algoritma geliştirme

---

## ⚙️ Kurulum

Projeyi çalıştırmak için:

```bash
git clone https://github.com/ozay-mehmet/42-Python-Projects.git
cd 42-Python-Projects
```

Her modül bağımsız çalıştırılabilir. İlgili modül/egzersiz klasörüne girip Python dosyasını doğrudan çalıştırmanız yeterlidir, örneğin:

```bash
cd Python-Module-0/ex0
python3 ft_hello_garden.py
```

Bağımlılık gerektiren modüller (örn. `Python-Module-8`) için ilgili klasördeki `requirements.txt` dosyasını kullanabilirsiniz:

```bash
pip install -r requirements.txt
```
