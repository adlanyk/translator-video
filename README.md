# 🎬 Video Subtitle Translator

**English Video → Indonesian Subtitle** secara otomatis menggunakan AI.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Apa ini?

Tools sederhana untuk menambahkan **subtitle Bahasa Indonesia** ke video berbahasa Inggris secara otomatis.

**Cocok untuk:**
- Content creator yang butuh subtitle cepat
- Video edukasi dari sumber internasional
- Siapa saja yang ingin memahami video Inggris lebih mudah

---

## ⚡ Cara Kerja

| Step | Proses | Tools |
|------|--------|-------|
| 1 | Mengenali suara Inggris | OpenAI Whisper |
| 2 | Translate ke Indonesia | Google Translate |
| 3 | Tempel subtitle ke video | FFmpeg |

---

## 🚀 Cara Pakai

### 1. Install yang diperlukan

```bash
# Install FFmpeg (wajib)
# Windows: download dari ffmpeg.org
# Mac: brew install ffmpeg
# Linux: sudo apt install ffmpeg

# Install library Python
pip install openai-whisper deep-translator
# Ganti nama file video kamu
video_path = "video_inggris.mp4"

# Jalankan
python translator.py

subtitle_indonesia.srt - File subtitle (bisa dipakai sendiri)

final_video_with_subtitle.mp4 - Video dengan subtitle permanen

## 📁 Struktur Project
├── translator.py          # Script utama
├── video_inggris.mp4      # Video sumber (taruh di sini)
├── subtitle_indonesia.srt # Hasil subtitle
└── final_video.mp4        # Video jadi

## 🔧 Customisasi
model = whisper.load_model("tiny")   # Cepat, kurang akurat
model = whisper.load_model("base")   # Standar (rekomendasi)
model = whisper.load_model("small")  # Lebih akurat, lebih lambat

## Ganti Bahasa Target
# Indonesia, Inggris, Spanyol, Jepang, dll
write_srt(segments, srt_path, target_lang="id")
