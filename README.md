# 🏴‍☠️ NuxSeptor v5.0
**Automated Web Vulnerability Infiltrator**

NuxSeptor adalah tool security auditor yang fokus pada kecepatan dan transparansi saat menelusuri celah keamanan web. Tool ini menggunakan *Predator Engine* untuk mendeteksi kerentanan **XSS** dan **SQL Injection** langsung ke akar lorong parameter web. Dirancang khusus buat lo yang butuh tool audit simpel tapi punya pergerakan yang agresif.

## ⚡ Kenapa Harus NuxSeptor?
* **Live Predator Trace:** Monitor pergerakan engine secara real-time saat melakukan injeksi payload. Gak ada aksi yang disembunyiin.
* **Hybrid Injection Logic:** Menggabungkan teknik *Error-Based* dan *Reflected Logic* untuk akurasi temuan yang lebih tajam.
* **Autonomous Discovery:** Engine otomatis memetakan path dan parameter potensial pada target.
* **Terminal Clean:** Fokus pada data. Sekali *run*, terminal akan dibersihkan dari noise untuk menampilkan log audit yang rapi.
* **Mobile Optimized:** Sangat ringan dan stabil untuk dijalankan di lingkungan Termux.

---

## 🛠️ Panduan Instalasi (Semua Platform)

Pilih perintah di bawah ini sesuai dengan Operating System yang lo pake:

### 📱 Android (Termux)
```bash
pkg update && pkg upgrade
pkg install python git -y
git clone https://github.com/dalangvps/NuxSeptor-
cd NuxSeptor-
pip install requests colorama
python nux.py -u <url> --sut
```
### 💻 Kali Linux
```bash
sudo apt update && sudo apt install python3 python3-pip git -y
git clone https://github.com/dalangvps/NuxSeptor-
cd NuxSeptor
pip3 install requests colorama
python nux.py -u <url> --sut
```
# WARNING
Gunakan tools ini dengan bijak. Jika lu menggunakan tidak ada izin dari operator web gua terus lu berurusan dengan polisi gua gak tanggung jawab, Safe ethical
