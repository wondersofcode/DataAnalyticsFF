# 🎬 Kino Sənayesi: Verilənlərin Təhlili və Analitika Paneli

Bu layihə Data Analitika fənni üzrə hazırlanmış **"Kino İndustriyasında Büdcə və IMDb Balı Arasındakı Asılılıq"** mövzusunda İnteraktiv Dashboard-dur (İdarəetmə Paneli).

## 👨‍💻 Layihə Tədqiqatçıları
* **Tunar Eyyublu**
* **Mayılova Ləman**

## 🎯 Layihənin Məqsədi
Kino studiyalarının və investorların *"Daha çox pul xərcləmək həmişə daha keyfiyyətli (yüksək reytinqli) film deməkdirmi?"* sualına riyazi və vizual sübutlarla cavab vermək. Layihə vasitəsilə 4800-dən çox filmin data təhlili aparılaraq, büdcə və izləyici məmnuniyyəti (IMDb balı) arasındakı asılılıq korrelyasiyası ölçülmüşdür.

## 🛠 İstifade Olunan Texnologiya və Arxitektura
* **Dil:** Python 3.10+
* **Veb Çərçivə (Framework):** Streamlit (Real-time interaktiv interfeys üçün)
* **Verilənlərin Təhlili (Data Manipulation):** Pandas, NumPy
* **Vizuallaşdırma (Data Visualization):** Plotly (İnteraktiv qrafiklər)
* **Data Mənbəyi:** Orijinal Kaggle TMDB 5000 Movie Dataset

## 📊 Texniki Xüsusiyyətlər
1. **İnteraktiv Filterləmə (Real-time):** İstifadəçi sol paneldən filmlərin çıxış ilini, büdcə aralığını və minimum IMDb reytinqini dəyişdirə bilər. Qrafiklər və riyazi hesablamalar heç bir səhifə yenilənməsinə ehtiyac olmadan dərhal (live) yenilənir.
2. **Scatter Plot Vizuallaşdırması:** Hər bir nöqtə bir filmi təmsil edir. Üzərinə gəldikdə filmin adı, büdcəsi və balı görünür. Rənglər reytinq dərəcəsinə görə dinamik tənzimlənmişdir.
3. **Pearson Korrelyasiyası:** Arxa planda Python vasitəsilə avtomatik olaraq iki dəyişən (Büdcə və Bal) arasındakı Pearson Korrelyasiya Əmsalı hesablanır və qərar olaraq ekrana çıxarılır.

## 📌 Yekun Nəticə
Təhlillər göstərir ki, büdcə və IMDb balı arasında **çox zəif asılılıq** var. Milyardlıq büdcəsi olan filmlər (məsələn, bəzi blokbasterlər) çox aşağı reytinq ala bildiyi halda, kiçik büdcəli filmlər izləyicilərin rəğbətini qazana bilir. Bu da sübut edir ki, böyük büdcə yüksək keyfiyyətə və izləyici rəğbətinə qəti zəmanət vermir.

---
© 2026 Data Analitika Laboratoriyası
