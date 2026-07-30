import cv2

def detect_edges(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Помилка відкриття обробленого зображення.")
        return None

    edges = cv2.Canny(image, 50, 150)

    output_path = "output/edges.png"
    cv2.imwrite(output_path, edges)

    print("Контури знайдено.")
    print(f"Файл збережено: {output_path}")

    return output_path
