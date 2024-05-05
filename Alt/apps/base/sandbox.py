from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image_path_, text_, output_path_,
                      font_path="Manrope-SemiBold.ttf", font_size_=64,
                      text_color_=(255, 255, 255), position_=(400, 847)):
    # Открыть изображение
    image = Image.open(image_path_)
    draw = ImageDraw.Draw(image)

    # Загрузить шрифт
    if font_path:
        font = ImageFont.truetype(font_path, font_size_)
    else:
        font = ImageFont.load_default()

    # Добавить текст на изображение
    draw.text(position_, text_, fill=text_color_, font=font)

    # Сохранить изображение с текстом
    image.save(output_path_)


# Пример использования
# ИМЯ
image_path = "Frame 59.jpg"
output_path = "participant diploma.jpg"
text = "Гыгы"  # сюда имя
font_patch = "Manrope-SemiBold.ttf"
font_size = 64
text_color = (255, 255, 255)
position = (400, 780)

add_text_to_image(image_path, text, output_path, font_patch, font_size, text_color, position)

# ФАМИЛИЯ
image_path = "participant diploma.jpg"
output_path = "participant diploma.jpg"
text = "Гыгы"  # СЮДА ФАМИЛИЮ
font_patch = "Manrope-SemiBold.ttf"
font_size = 64
text_color = (255, 255, 255)
position = (500, 845)

add_text_to_image(image_path, text, output_path, font_patch, font_size, text_color, position)

# ДАТА
image_path = "participant diploma.jpg"
output_path = "participant diploma.jpg"
text = "16.04.2024"  # СЮДА ДАТА
font_patch = "Manrope-SemiBold.ttf"
font_size = 36
text_color = (255, 255, 255)
position = (1925, 1065)

add_text_to_image(image_path, text, output_path, font_patch, font_size, text_color, position)
