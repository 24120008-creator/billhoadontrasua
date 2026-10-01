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

# Giá topping
TOPPINGS = {
    "Không thêm topping": 0,
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

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HÌNH NỀN / LOGO
# ============================================================

logo_path = Path("logo3.png")

if logo_path.exists():
    st.image(str(logo_path), use_container_width=True)
else:
    st.warning(
        "Chưa tìm thấy logo3.png. Hãy đặt file logo3.png cùng thư mục với app.py."
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
# CHỌN TRÀ SỮA
# ============================================================

st.subheader("🧋 Chọn món")

loai_tra_sua = st.selectbox(
    "Loại trà sữa",
    list(MENU.keys())
)

gia_tra_sua = MENU[loai_tra_sua]

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

# ============================================================
# ĐƯỜNG VÀ ĐÁ
# ============================================================

col1, col2 = st.columns(2)

with col1:
    muc_duong = st.selectbox(
        "🍬 Mức độ đường",
        ["100%", "70%", "0%"]
    )

with col2:
    muc_da = st.selectbox(
        "🧊 Mức độ đá",
        ["100%", "70%", "0%"]
    )

# ============================================================
# TOPPING
# ============================================================

st.subheader("🍮 Topping")

topping = st.multiselect(
    "Chọn topping",
    list(TOPPINGS.keys())
)

# Nếu chọn "Không thêm topping" cùng topping khác
if "Không thêm topping" in topping and len(topping) > 1:
    topping = [
        item for item in topping
        if item != "Không thêm topping"
    ]

# ============================================================
# TÍNH TIỀN
# ============================================================

gia_topping_mot_ly = sum(
    TOPPINGS[item] for item in topping
)

gia_mot_ly = gia_tra_sua + gia_topping_mot_ly

tong_tien = gia_mot_ly * so_luong

# ============================================================
# HIỂN THỊ KẾT QUẢ
# ============================================================

st.divider()

st.subheader("🧾 Thông tin hóa đơn")

st.markdown(
    f"""
    <div class="bill">

    <div class="bill-title">
        🧋 {TEN_QUAN}
    </div>

    <div style="text-align:center;">
        {DIA_CHI}
    </div>

    <hr>

    <div class="info">
    <b>Khách hàng:</b> {ten_khach if ten_khach else "Chưa nhập tên"}<br>
    <b>Món:</b> {loai_tra_sua}<br>
    <b>Số lượng:</b> {so_luong}<br>
    <b>Đường:</b> {muc_duong}<br>
    <b>Đá:</b> {muc_da}<br>
    <b>Topping:</b> {", ".join(topping) if topping else "Không có"}<br>
    <b>Đơn giá trà sữa:</b> {gia_tra_sua:,} VNĐ<br>
    <b>Tiền topping / ly:</b> {gia_topping_mot_ly:,} VNĐ<br>
    <b>Đơn giá / ly:</b> {gia_mot_ly:,} VNĐ
    </div>

    <hr>

    <div class="total">
        TỔNG TIỀN: {tong_tien:,} VNĐ
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TẠO NỘI DUNG HÓA ĐƠN
# ============================================================

thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

noi_dung_hoa_don = f"""
==================================================
             {TEN_QUAN}
        Địa chỉ: {DIA_CHI}
==================================================

                 HÓA ĐƠN BÁN HÀNG

Thời gian: {thoi_gian}
Khách hàng: {ten_khach if ten_khach else "Khách lẻ"}

--------------------------------------------------
MÓN HÀNG
--------------------------------------------------

Tên món       : {loai_tra_sua}
Số lượng      : {so_luong}
Đơn giá       : {gia_tra_sua:,} VNĐ

Mức đường     : {muc_duong}
Mức đá        : {muc_da}

Topping:
"""

if topping:
    for item in topping:
        noi_dung_hoa_don += (
            f"  - {item}: {TOPPINGS[item]:,} VNĐ / ly\n"
        )
else:
    noi_dung_hoa_don += "  - Không có topping\n"

noi_dung_hoa_don += f"""
--------------------------------------------------
Tạm tính / ly  : {gia_mot_ly:,} VNĐ
Số lượng        : {so_luong}
--------------------------------------------------

TỔNG THANH TOÁN: {tong_tien:,} VNĐ

==================================================
              CẢM ƠN QUÝ KHÁCH!
          HẸN GẶP LẠI LẦN SAU 🧋
==================================================
"""

# ============================================================
# NÚT THANH TOÁN
# ============================================================

st.divider()

if st.button(
    "💳 THANH TOÁN & XUẤT HÓA ĐƠN",
    use_container_width=True,
    type="primary"
):

    if not ten_khach.strip():
        ten_hien_thi = "Khach_le"
    else:
        ten_hien_thi = ten_khach.strip()

    # Loại bỏ ký tự đặc biệt khỏi tên file
    ten_file = "".join(
        c for c in ten_hien_thi
        if c.isalnum() or c in (" ", "_", "-")
    ).replace(" ", "_")

    filename = f"HoaDon_{ten_file}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    st.success("✅ Thanh toán thành công!")

    st.download_button(
        label="📥 TẢI FILE HÓA ĐƠN",
        data=noi_dung_hoa_don,
        file_name=filename,
        mime="text/plain",
        use_container_width=True
    )

    st.balloons()

# ============================================================
# CHÂN TRANG
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#888;">
        🧋 Cảm ơn quý khách đã ủng hộ!<br>
        Chúc quý khách một ngày vui vẻ ❤️
    </div>
    """,
    unsafe_allow_html=True
)
