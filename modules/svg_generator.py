import cv2

def generate_svg(edge_image_path):
    image = cv2.imread(edge_image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Не вдалося відкрити файл контурів.")
        return

    contours, _ = cv2.findContours(
        image,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    svg = []

    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg">')

    for contour in contours:

        if len(contour) < 2:
            continue

        points = []

        for point in contour:
            x, y = point[0]
            points.append(f"{x},{y}")

        svg.append(
            f'<polyline points="{" ".join(points)}" '
            'fill="none" stroke="black" stroke-width="1"/>'
        )

    svg.append("</svg>")

    with open("output/result.svg", "w") as file:
        file.write("\n".join(svg))

    print("SVG створено: output/result.svg")
