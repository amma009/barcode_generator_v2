import io
from PIL import ImageFont

def load_font(size=16):
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

def pil_to_bytes(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.getvalue()

def safe_text_height(font, text="A"):
    try:
        bbox = font.getbbox(text)
        return bbox[3] - bbox[1]
    except:
        return font.getsize(text)[1]
