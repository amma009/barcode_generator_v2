from PIL import Image, ImageDraw
from utils import load_font, safe_text_height


def compose_label(barcode_img, description, font_size=14, spacing=5):

    font = load_font(font_size)

    bc = barcode_img.copy().convert("RGB")

    bw, bh = bc.size

    canvas_w = max(bw, 400)
    canvas_h = bh + 60

    img = Image.new("RGB", (canvas_w, canvas_h), "white")

    draw = ImageDraw.Draw(img)

    img.paste(bc, ((canvas_w - bw)//2, 10))

    if description:

        text_w = draw.textlength(description, font=font)
        text_h = safe_text_height(font)

        x = (canvas_w - text_w) / 2
        y = bh + spacing + 10

        draw.text((x, y), description, font=font, fill="black")

    return img
