from modules.png_loader import load_image
from modules.image_preprocessor import preprocess
from modules.edge_detector import detect_edges
from modules.svg_generator import generate_svg
import os

print("=" * 40)
print("      DrawMotion Engine v0.4")
print("=" * 40)

image = load_image()

if image:
    print("✅ Зображення успішно завантажено.")

    folder = "input/images"
    files = [f for f in os.listdir(folder)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    image_path = os.path.join(folder, files[0])

    preprocessed = preprocess(image_path)

    if preprocessed:
        edges = detect_edges(preprocessed)

        if edges:
            generate_svg(edges)

else:
    print("❌ Не вдалося завантажити зображення.")
