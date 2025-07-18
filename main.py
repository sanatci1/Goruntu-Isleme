import cv2
import matplotlib.pyplot as plt

# 1. Görüntüyü yükle
image_path = "C:/Users\Karaimha/ornek.jpg"  # Dosya adını buraya yaz
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img is None:
    print(f"❌ Görüntü yüklenemedi: {image_path}")
    exit()

# 2. Temel bilgileri yazdır
h, w, c = img.shape
print(f" Boyut: {w} x {h}")
print(f" Kanal sayısı: {c}")
print(f" Veri tipi: {img.dtype}")

# 3. Gri versiyonu oluştur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(" Gri boyut:", gray.shape)
print(" İlk 5x5 piksel:\n", gray[:5, :5])

# 4. Görüntüleri matplotlib ile yan yana göster
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(f"Renkli\n{img.shape}, {img.dtype}")
plt.axis(False)

plt.subplot(1, 2, 2)
plt.imshow(gray, cmap="gray")
plt.title(f"Gri\n{gray.shape}, {gray.dtype}")
plt.axis(False)

plt.tight_layout()
plt.show()

# 5. OpenCV ile görüntüyü göster ve 's' tuşuyla kaydet
cv2.imshow("Display - Renkli Görüntü", img)
k = cv2.waitKey(0)

if k == ord('s'):
    cv2.imwrite("starry_night_saved.png", img)
    print("💾 Görüntü kaydedildi: starry_night_saved.png")

cv2.destroyAllWindows()
