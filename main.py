from modules.png_loader import load_image
from modules.image_preprocessor import preprocess
import os

print("=" * 40)
print("      DrawMotion Engine v0.2")
print("=" * 40)

image = load_image()

if image:
    print("✅ Зображення успішно завантажено.")

    folder = "input/images"
    files = [f for f in os.listdir(folder)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    image_path = os.path.join(folder, files[0])

    preprocess(image_path)

else:
    print("❌ Не вдалося завантажити зображення.")
