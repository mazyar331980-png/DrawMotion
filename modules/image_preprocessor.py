import cv2

def preprocess(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Помилка відкриття зображення.")
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    result_path = "output/preprocessed.png"

    cv2.imwrite(result_path, blur)

    print("Попередня обробка завершена.")
    print(f"Файл збережено: {result_path}")

    return result_path
