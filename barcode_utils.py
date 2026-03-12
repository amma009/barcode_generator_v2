import qrcode
import io
from PIL import Image
import barcode
from barcode.writer import ImageWriter


def generate_qr(data: str):

    qr = qrcode.QRCode(
        box_size=10,
        border=2
    )

    qr.add_data(data)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")


def generate_code128(data: str):

    CODE128 = barcode.get_barcode_class("code128")

    options = {
        "module_width":0.2,
        "module_height":15,
        "font_size":0,
        "text_distance":1
    }

    c128 = CODE128(data, writer=ImageWriter())

    buffer = io.BytesIO()

    c128.write(buffer, options)

    buffer.seek(0)

    return Image.open(buffer)
