import requests
import os

# ==========================================
# 1. PREDIKSI TEKS (KODE LAMA SUDAH OKE)
# ==========================================
print("--- Menjalankan Prediksi Teks ---")
url_text = "https://risetkami-risetkami.hf.space/predict_text"
payload_text = {"text": "saya tidak mau berangkat kuliah"}
headers_text = {"Content-Type": "application/json"}

try:
    response_text = requests.post(url_text, json=payload_text, headers=headers_text)
    print("Hasil Teks:", response_text.json())
except Exception as e:
    print("Terjadi kesalahan pada teks:", e)

print("\n" + "="*40 + "\n")

# ==========================================
# 2. PREDIKSI GAMBAR (VERSI REVISI)
# ==========================================
print("--- Menjalankan Prediksi Gambar ---")
url_face = "https://risetkami-risetkami.hf.space/predict_face"
IMAGE_PATH = "/mnt/windows/BelajarOtodidak/30_days_of_python/testApi/coba1.jpg"

# Cek apakah file benar-benar ada sebelum kirim
if not os.path.exists(IMAGE_PATH):
    print(f"Error: File tidak ditemukan di {IMAGE_PATH}")
else:
    # Membuka file dalam mode 'rb' (read binary)
    with open(IMAGE_PATH, 'rb') as img_file:
        # Kita ambil nama filenya saja (misal: coba1.jpg)
        file_name = os.path.basename(IMAGE_PATH)
        
        # Format pengiriman file yang benar
        files = {
            "file": (file_name, img_file, "image/jpeg")
        }

        try:
            response_face = requests.post(url_face, files=files)
            
            if response_face.status_code == 200:
                print("Hasil Gambar:", response_face.json())
            else:
                print(f"Error Server ({response_face.status_code}):", response_face.text)
        except Exception as e:
            print("Terjadi kesalahan koneksi:", e)