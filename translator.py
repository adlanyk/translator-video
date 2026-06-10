import subprocess
import whisper
from deep_translator import GoogleTranslator
import os
import sys

# === KONFIGURASI ===
video_path = "What is Identity Theft_.mp4"  # Ganti dengan nama file video kamu
output_path = "What is Identity Theft_final_video_with_subtitle.mp4"
srt_path = "subtitle_indonesia.srt"

print("1. Cek file video...")
if not os.path.exists(video_path):
    print(f"ERROR: File {video_path} tidak ditemukan!")
    sys.exit()

# === STEP 1: Extract transkrip dengan Whisper (dapat timestamp) ===
print("2. Mengenali suara Inggris dan membuat subtitle...")
model = whisper.load_model("base")  # atau "tiny" untuk lebih cepat
result = model.transcribe(video_path, word_timestamps=True)

# === STEP 2: Buat file SRT dari hasil transkrip ===
def write_srt(segments, output_file, target_lang="id"):
    """
    Membuat file .srt dari segments Whisper
    Lalu translate isinya ke Bahasa Indonesia
    """
    translator = GoogleTranslator(source='en', target=target_lang)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(segments, start=1):
            # Format timestamp: HH:MM:SS,mmm --> HH:MM:SS,mmm
            start = segment['start']
            end = segment['end']
            
            start_h = int(start // 3600)
            start_m = int((start % 3600) // 60)
            start_s = int(start % 60)
            start_ms = int((start % 1) * 1000)
            
            end_h = int(end // 3600)
            end_m = int((end % 3600) // 60)
            end_s = int(end % 60)
            end_ms = int((end % 1) * 1000)
            
            # Tulis timestamp
            f.write(f"{i}\n")
            f.write(f"{start_h:02d}:{start_m:02d}:{start_s:02d},{start_ms:03d} --> {end_h:02d}:{end_m:02d}:{end_s:02d},{end_ms:03d}\n")
            
            # Translate teks asli ke Indonesia
            teks_asli = segment['text'].strip()
            try:
                teks_indonesia = translator.translate(teks_asli)
            except:
                # Fallback kalau error
                teks_indonesia = teks_asli
            
            f.write(f"{teks_indonesia}\n\n")
            print(f"   Segment {i}: {teks_asli[:50]}... → {teks_indonesia[:50]}...")

print("3. Menerjemahkan subtitle ke Indonesia...")
write_srt(result['segments'], srt_path, "id")
print(f"   File SRT tersimpan: {srt_path}")

# === STEP 3: Burn subtitle ke video (opsional) ===
print("4. Menambahkan subtitle ke video...")
try:
    # Cara 1: Burn subtitle permanen ke video
    subprocess.run([
        "ffmpeg", "-i", video_path,
        "-vf", f"subtitles={srt_path}",
        "-c:a", "copy",  # audio tetap asli, tidak diubah
        "-y", output_path
    ], check=True)
    print(f"✅ SUKSES! Video dengan subtitle: {output_path}")
    
except subprocess.CalledProcessError as e:
    print(f"ERROR burning subtitle: {e}")
    print("\nAlternatif: Gunakan VLC atau pemutar video lain untuk memuat file .srt")
    
print("\n=== SELESAI ===")
print(f"File subtitle: {srt_path}")
print(f"Video final: {output_path}")
input("Tekan Enter untuk keluar...")