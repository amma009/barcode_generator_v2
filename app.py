import streamlit as st

from barcode_utils import generate_qr, generate_code128
from label_composer import compose_label
from pdf_engine import generate_pdf
from config import LABEL_PRESETS, PAPER_PRESETS
from utils import pil_to_bytes


st.set_page_config(layout="wide")

st.title("Label Generator")

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.header("Controls")

code = st.sidebar.text_input("Kode")

desc = st.sidebar.text_input("Description")

barcode_type = st.sidebar.selectbox(
    "Barcode Type",
    ["Code128", "QR"]
)

preset = st.sidebar.selectbox(
    "Label Size",
    list(LABEL_PRESETS.keys())
)

paper = st.sidebar.selectbox(
    "Paper",
    list(PAPER_PRESETS.keys())
)

generate = st.sidebar.button("Generate")

# ======================================================
# GENERATE LABEL
# ======================================================

if generate and code:

    if barcode_type == "QR":
        bc = generate_qr(code)
    else:
        bc = generate_code128(code)

    label_img = compose_label(bc, desc)

    st.session_state["label"] = label_img

# ======================================================
# PREVIEW
# ======================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("Label Preview")

    if "label" in st.session_state:

        st.image(pil_to_bytes(st.session_state["label"]))

with col2:

    st.subheader("PDF Export")

    if "label" in st.session_state:

        label_mm = LABEL_PRESETS[preset]

        paper_mm = PAPER_PRESETS[paper]

        pdf = generate_pdf(
            st.session_state["label"],
            label_mm,
            paper_mm
        )

        st.download_button(
            "Download PDF",
            data=pdf,
            file_name=f"{code}.pdf",
            mime="application/pdf"
        )
