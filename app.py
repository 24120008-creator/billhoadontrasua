import streamlit as st
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH TRANG
# ============================================================

st.set_page_config(
    page_title="Trà Sữa Ngọt Ngào",
    page_icon="🧋",
    layout="centered"
)

# ============================================================
# THÔNG TIN QUÁN
# ============================================================

TEN_QUAN = "TRÀ SỮA NGỌT NGÀO"
DIA_CHI = "15/27 Ngô Gia Tự"

# ============================================================
# MENU
# ============================================================

MENU = {
    "Trà sữa truyền thống": 20000,
    "Trà sữa matcha": 25000,
    "Trà sữa socola": 25000,
    "Trà sữa dâu": 25000,
    "Trà sữa đào": 25000,
    "Trà sữa chanh dây": 25000
}

# ============================================================
# TOPPING
# ============================================================

TOPPINGS = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch dừa": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 8000
}

# ============================================================
# GIÁ SIZE
# ============================================================

SIZE_PRICE = {
    "S": 0,
    "M": 5000,
    "L": 10000
}

# ============================================================
# CSS GIAO DIỆN
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
    }

    .address {
        text-align: center;
        font-size: 16px;
    }

    .total-box {
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        border: 2px solid #ddd;
    }

    .bill-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TIÊU ĐỀ
# ============================================================

st.markdown(
    '<div class="main-title">🧋 TRÀ SỮA NGỌT NGÀO</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="address">📍 {DIA_CHI}</div>',
    unsafe_allow_html=True
)

# ============================================================
# HIỂN THỊ LOGO NẾU CÓ
# ============================================================

logo_path = Path("logo3.png")

if logo_path.exists():
    st.image(
        str(logo_path),
        width=180
    )

st.divider()

# ============================================================
# THÔNG TIN KHÁCH HÀNG
# ============================================================

st.subheader("👤 THÔNG TIN KHÁCH HÀNG")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# ============================================================
# CHỌN MÓN
# ============================================================

st.subheader("🧋 CHỌN TRÀ SỮA")

ten_mon = st.selectbox(
    "Loại trà sữa",
    list(MENU.keys())
)

gia_mon = MENU[ten_mon]

st.info(
    f"💰 Giá cơ bản: {gia_mon:,} VNĐ"
)

# ============================================================
# CHỌN SIZE
# ============================================================

st.subheader("📏 CHỌN SIZE")

size = st.radio(
    "Kích thước ly",
    ["S", "M", "L"],
    horizontal=True
)

gia_size = SIZE_PRICE[size]

if size == "S":
    st.write("🥤 Size S - Không phụ thu")

elif size == "M":
    st.write("🥤 Size M - Phụ thu 5.000 VNĐ")

else:
    st.write("🥤 Size L - Phụ thu 10.000 VNĐ")

# ============================================================
# SỐ LƯỢNG
# ============================================================

so_luong = st.number_input(
    "🔢 Số lượng",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

# ============================================================
# TOPPING
# ============================================================

st.subheader("🍮 CHỌN TOPPING")

topping_chon = st.multiselect(
    "Bạn muốn thêm topping nào?",
    list(TOPPINGS.keys())
)

gia_topping = 0

for topping in topping_chon:
    gia_topping += TOPPINGS[topping]

# ============================================================
# MỨC ĐƯỜNG
# ============================================================

st.subheader("🍬 MỨC ĐỘ ĐƯỜNG")

duong = st.radio(
    "Chọn mức đường",
    ["100%", "70%", "0%"],
    horizontal=True
)

# ============================================================
#
