import streamlit as st
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH TRANG
# ============================================================

st.set_page_config(
    page_title="Trà Sữa - Tính Bill",
    page_icon="🧋",
    layout="centered"
)

# ============================================================
# THÔNG TIN QUÁN
# ============================================================

TEN_QUAN = "TRÀ SỮA NGỌT NGÀO"
DIA_CHI = "15/27 Ngô Gia Tự"

# ============================================================
# GIÁ TRÀ SỮA
# ============================================================

MENU = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa socola": 28000,
    "Trà sữa matcha": 30000,
    "Trà sữa dâu": 28000,
    "Trà sữa đào": 28000,
    "Trà sữa khoai môn": 30000,
    "Trà sữa thái xanh": 28000,
    "Trà sữa thái đỏ": 28000,
}

# ============================================================
# GIÁ TOPPING
# ============================================================

TOPPINGS = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Thạch dừa": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 8000,
}

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #fff8f3;
    }

    .title {
        text-align: center;
        color: #8b4513;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .address {
        text-align: center;
        color: #666666;
        font-size: 17px;
        margin-bottom: 20px;
    }

    .bill {
        background-color: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.12);
        border: 1px solid #ead8cc;
    }

    .bill-title {
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        color: #8b4513;
    }

    .total {
        text-align: right;
        font-size: 24px;
        font-weight: bold;
        color: #d35400;
        margin-top: 15px;
    }

    .info {
        font-size: 16px;
        line-height: 1.7;
    }

    .mon-title {
        background-color: #fff0e6;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
        color: #8b4513;
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# LOGO
# ============================================================

logo_path = Path("logo3.jpg")

if logo_path.exists():
    st.image(str(logo_path), use_container_width=True)
else:
    st.warning(
        "Chưa tìm thấy logo3.jpg. Hãy đặt file logo3.jpg cùng thư mục với app.py."
    )

# ============================================================
# TIÊU ĐỀ
# ============================================================

st.markdown(
    f'<div class="title">🧋 {TEN_QUAN}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="address">📍 {DIA_CHI}</div>',
    unsafe_allow_html=True
)

st.divider()

# ============================================================
# THÔNG TIN KHÁCH HÀNG
# ============================================================

st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# ============================================================
# SỐ LƯỢNG MÓN
# ============================================================

st.subheader("🧋 Chọn món")

so_mon = st.number_input(
    "Số loại món muốn đặt",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

# ============================================================
# DANH SÁCH MÓN
# ============================================================

danh_sach_mon = []

for i in range(int(so_mon)):

    st.markdown(
        f'<div class="mon-title">🧋 MÓN {i + 1}</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([3, 1])

    with col1:
        loai_tra_sua = st.selectbox(
            "Loại trà sữa",
            list(MENU.keys()),
            key=f"loai_{i}"
        )

    with col2:
        so_luong = st.number_input(
            "Số lượng",
            min_value=1,
            max_value=50,
            value=1,
            step=1,
            key=f"soluong_{i}"
        )

    col3, col4 = st.columns(2)

    with col3:
        muc_duong = st.selectbox(
            "🍬 Mức độ đường",
            ["100%", "70%", "0%"],
            key=f"duong_{i}"
        )

    with col4:
        muc_da = st.selectbox(
            "🧊 Mức độ đá",
            ["100%", "70%", "0%"],
            key=f"da_{i}"
        )

    topping = st.multiselect(
        "🍮 Topping",
        list(TOPPINGS.keys()),
        key=f"topping_{i}"
    )

    # Tính tiền topping cho 1 ly
    gia_topping_mot_ly = sum(
        TOPPINGS[item] for item in topping
    )

    # Giá 1 ly
    gia_tra_sua = MENU[loai_tra_sua]

    gia_mot_ly = (
        gia_tra_sua +
        gia_topping_mot_ly
    )

    # Thành tiền
    thanh_tien = gia_mot_ly * so_luong

    danh_sach_mon.append({
        "loai": loai_tra_sua,
        "so_luong": so_luong,
        "duong": muc_duong,
        "da": muc_da,
        "topping": topping,
        "gia_tra_sua": gia_tra_sua,
        "gia_topping": gia_topping_mot_ly,
        "gia_mot_ly": gia_mot_ly,
        "thanh_tien": thanh_tien
    })

# ============================================================
# TÍNH TỔNG TIỀN
# ============================================================

tong_tien = sum(
    mon["thanh_tien"]
    for mon in danh_sach_mon
)

tong_so_ly = sum(
    mon["so_luong"]
    for mon in danh_sach_mon
)

# ============================================================
# HIỂN THỊ HÓA ĐƠN
# ============================================================

st.divider()

st.subheader("🧾 HÓA ĐƠN")

html_bill = f"""
<div class="bill">

<div class="bill-title">
🧋 {TEN_QUAN}
</div>

<div style="text-align:center;">
{DIA_CHI}
</div>

<hr>

<div class="info">

<b>Khách hàng:</b>
{ten_khach if ten_khach else "Chưa nhập tên"}

<br>

<b>Tổng số loại món:</b>
{len(danh_sach_mon)}

<br>

<b>Tổng số ly:</b>
{tong_so_
