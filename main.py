from modules.png_loader import load_image

print("=" * 40)
print("      DrawMotion Engine v0.1")
print("=" * 40)

image = load_image()

if image:
    print("✅ Зображення успішно завантажено.")
else:
    print("❌ Не вдалося завантажити зображення.")
