def cf_integration(handle: str):
    import requests
    from datetime import datetime

    def get_date(x, f="%d.%m.%Y"):
        return datetime.strptime(x.get("date"), f)

    if handle is None:
        return list()

    response = requests.get(f"https://codeforces.com/api/user.rating?handle={handle}")
    current_status = requests.get(f"https://codeforces.com/api/user.info?handles={handle}&checkHistoricHandles=false")

    data = response.json()

    if data["status"] == "OK":
        rating_changes = data["result"]
        if len(rating_changes) == 0:
            return list()

        for change in rating_changes:
            change['date'] = datetime.utcfromtimestamp(change["ratingUpdateTimeSeconds"]).strftime('%d.%m.%Y')
            change['contest_name'] = change["contestName"]
            change['rank'] = change["rank"]
            change['current_rate'] = change["newRating"]
            change['plus_rate'] = abs(int(change["newRating"]) - int(change["oldRating"]))

        sort_dates = sorted(rating_changes, key=get_date, reverse=True)
        avatar = current_status.json()['result'][0]['avatar']
        sort_dates[0]['avatar'] = avatar

        return sort_dates


def add_text_to_image(
        image_path, text, output_path,
        font_path='Manrope-SemiBold.ttf',
        font_size=64, text_color=(255, 255, 255),
        position=(400, 847)):
    # Открыть изображение
    from PIL import Image, ImageDraw, ImageFont
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    # Загрузить шрифт
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    # Добавить текст на изображение
    draw.text(position, text, fill=text_color, font=font)

    # Сохранить изображение с текстом
    image.save(output_path)


def generate_diplomo(name, surname, date):
    image_path = "Frame 59.jpg"
    output_path = "participant diploma.jpg"
    text = name
    font_patch = "Manrope-SemiBold.ttf"
    font_size = 64
    text_color = (255, 255, 255)
    position = (400, 780)

    add_text_to_image(image_path, text, output_path, font_patch, font_size, text_color, position)

    image_path = "participant diploma.jpg"
    output_path = "participant diploma.jpg"
    text = surname
    font_patch = "Manrope-SemiBold.ttf"
    font_size = 64
    text_color = (255, 255, 255)
    position = (500, 845)

    add_text_to_image(image_path, text, output_path, font_patch, font_size, text_color, position)

    image_path = "participant diploma.jpg"
    output_path = "participant diploma.jpg"
    text = date
    font_patch = "Manrope-SemiBold.ttf"
    font_size = 36
    text_color = (255, 255, 255)
    position = (1925, 1065)

    add_text_to_image(image_path, text, output_path, font_patch, font_size, text_color, position)


if __name__ == "__main__":
    generate_diplomo("Ilja", "Scherbakov", 2024)
    pass
