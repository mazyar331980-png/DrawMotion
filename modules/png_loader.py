from PIL import Image
import os

def load_image(folder="input/images"):
    if not os.path.exists(folder):
        print(f"Папка '{folder}' не існує.")
        return None

    files = [f for f in os.listdir(folder)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not files:
        print("У папці немає PNG або JPG.")
        return None

    file_path = os.path.join(folder, files[0])

    image = Image.open(file_path)

    print(f"Файл: {files[0]}")
    print(f"Розмір: {image.width} x {image.height}")

    return image
