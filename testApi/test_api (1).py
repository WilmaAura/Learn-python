import requests

url = "https://risetkami-risetkami.hf.space/predict_text"

payload = {"text": "saya tidak mau berangkat kuliah"}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())


import cv2
import requests

# ==== CONFIG ====
API_URL = "https://risetkami-risetkami.hf.space/predict_face"   # ubah ke URL space HF nanti
IMAGE_PATH = "/mnt/windows/BelajarOtodidak/30_days_of_python/testApi/cowok1.jpeg"  # path gambar lokal

# ==== LOAD IMAGE DENGAN OPENCV ====
img = cv2.imread(IMAGE_PATH)

if img is None:
    raise FileNotFoundError(f"File tidak ditemukan: {IMAGE_PATH}")

# OPSIONAL: encode jadi bytes JPG sebelum kirim
_, img_encoded = cv2.imencode('.jpg', img)

# ==== REQUEST ====
files = {
    "file": (IMAGE_PATH, img_encoded.tobytes(), "image/jpeg")
}

response = requests.post(API_URL, files=files)

# ==== CETAK HASIL ====
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.text)
