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
