import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader


def generate_pdf(label_img, label_mm, paper_mm):

    lw, lh = label_mm
    pw, ph = paper_mm

    lw_pt = lw * mm
    lh_pt = lh * mm

    pw_pt = pw * mm
    ph_pt = ph * mm

    buf = io.BytesIO()

    pdf = canvas.Canvas(buf, pagesize=(pw_pt, ph_pt))

    img_buf = io.BytesIO()

    label_img.save(img_buf, "PNG")

    img_buf.seek(0)

    img_reader = ImageReader(img_buf)

    cols = int(pw / lw)
    rows = int(ph / lh)

    for r in range(rows):
        for c in range(cols):

            x = c * lw_pt
            y = ph_pt - ((r + 1) * lh_pt)

            pdf.drawImage(
                img_reader,
                x,
                y,
                lw_pt,
                lh_pt
            )

    pdf.save()

    buf.seek(0)

    return buf
