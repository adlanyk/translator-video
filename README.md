# 🎬 Video Subtitle Translator

> **English Video → Indonesian Subtitle** secara otomatis menggunakan AI

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-purple.svg)](https://github.com/openai/whisper)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Tentang Project

Tools sederhana untuk menambahkan **subtitle Bahasa Indonesia** ke video berbahasa Inggris secara otomatis.

### 🎯 Cocok Untuk

| Pengguna | Kebutuhan |
|----------|-----------|
| Content Creator | Subtitle cepat untuk konten |
| Pendidik | Video edukasi dari sumber internasional |
| Umum | Memahami video Inggris lebih mudah |

---

## ⚙️ Cara Kerja

| Step | Proses | Tools |
|:----:|--------|-------|
| 1 | Mengenali suara Inggris | OpenAI Whisper |
| 2 | Menerjemahkan ke Indonesia | Google Translate |
| 3 | Menempel subtitle ke video | FFmpeg |

---

## 🚀 Instalasi & Penggunaan

### 1. Install Dependencies

```bash
# Install FFmpeg (WAJIB)
# Windows: download dari ffmpeg.org
# macOS : brew install ffmpeg
# Linux : sudo apt install ffmpeg

# Install library Python
pip install openai-whisper deep-translator

# Ganti nama file video sesuai kebutuhan
video_path = "video_inggris.mp4"

# Eksekusi script
python translator.py

project-folder/
│
├── translator.py              # Script utama
├── video_inggris.mp4          # Video sumber (taruh di sini)
├── subtitle_indonesia.srt     # Hasil subtitle
├── final_video.mp4            # Video jadi
│
├── README.md                  # Dokumentasi

---

 🔧 Customisasi 

Model Whisper (Kecepatan vs Akurasi)
model = whisper.load_model("tiny")   # ⚡ Cepat, kurang akurat
model = whisper.load_model("base")   # 👍 Standar (rekomendasi)
model = whisper.load_model("small")  # 📈 Lebih akurat, lebih lambat