import streamlit as st
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH
# ============================================================

st.set_page_config(
    page_title="Trà Sữa - Tính Bill",
    page_icon="🧋",
    layout="centered"
)

TEN_QUAN = "TRÀ SỮA NGỌT NGÀO"
DIA_CHI = "15/27 Ngô Gia Tự"

# ============================================================
# MENU
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

st.markdown("""
<style>

.main {
    background-color: #fff8f3;
}

.title {
    text-align: center;
    color: #8b4513;
    font-size: 36px;
    font-weight: bold;
}

.address {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 20px;
}

.bill {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #ead8cc;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.12);
}

.bill-title {
    text-align: center;
    color: #8b4513;
    font-size: 25px;
    font-weight: bold;
}

.total {
    text-align: right;
    color: #d35400;
    font-size: 24px;
    font-weight: bold;
}

.mon-box {
    background-color: #fff0e6;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# LOGO
# ============================================================

logo_path = Path("logo3.jpg")

if logo_path.exists():
    st.image(str(logo_path), use_container_width=True)
else:
    st.warning("Chưa tìm thấy logo3.jpg")

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
# KHÁCH HÀNG
# ============================================================

st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# ============================================================
# CHỌN SỐ MÓN
# ============================================================

st.subheader("🧋 Chọn món")

so_mon = st.number_input(
    "Số loại món",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

# Danh sách lưu món
danh_sach_mon = []

# ============================================================
# NHẬP TỪNG MÓN
# ============================================================

for i in range(int(so_mon)):

    st.markdown(
        f'<div class="mon-box"><b>🧋 MÓN {i + 1}</b></div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([3, 1])

    with col1:
        loai_tra_sua = st.selectbox(
            "Loại trà sữa",
            list(MENU.keys()),
            key=f"loai_tra_sua_{i}"
        )

    with col2:
        so_luong = st.number_input(
            "Số lượng",
            min_value=1,
            max_value=50,
            value=1,
            step=1,
            key=f"so_luong_{i}"
        )

    col3, col4 = st.columns(2)

    with col3:
        muc_duong = st.selectbox(
            "🍬 Mức đường",
            ["100%", "70%", "0%"],
            key=f"muc_duong_{i}"
        )

    with col4:
        muc_da = st.selectbox(
            "🧊 Mức đá",
            ["100%", "70%", "0%"],
            key=f"muc_da_{i}"
        )

    topping = st.multiselect(
        "🍮 Topping",
        list(TOPPINGS.keys()),
        key=f"topping_{i}"
    )

    # --------------------------------------------------------
    # TÍNH TIỀN MÓN
    # --------------------------------------------------------

    gia_tra_sua = MENU[loai_tra_sua]

    gia_topping = 0

    for item in topping:
        gia_topping += TOPPINGS[item]

    gia_mot_ly = gia_tra_sua + gia_topping

    thanh_tien = gia_mot_ly * so_luong

    # Lưu món
    danh_sach_mon.append({
        "loai": loai_tra_sua,
        "so_luong": so_luong,
        "duong": muc_duong,
        "da": muc_da,
        "topping": topping,
        "gia_tra_sua": gia_tra_sua,
        "gia_topping": gia_topping,
        "gia_mot_ly": gia_mot_ly,
        "thanh_tien": thanh_tien
    })

# ============================================================
# TỔNG TIỀN
# ============================================================

tong_tien = 0
tong_so_ly = 0

for mon in danh_sach_mon:
    tong_tien += mon["thanh_tien"]
    tong_so_ly += mon["so_luong"]

# ============================================================
# HIỂN THỊ BILL
# ============================================================

st.divider()

st.subheader("🧾 HÓA ĐƠN")

st.markdown(
    f"""
    <div class="bill">

    <div class="bill-title">
        🧋 {TEN_QUAN}
    </div>

    <p style="text-align:center;">
        {DIA_CHI}
    </p>

    <hr>

    <b>Khách hàng:</b>
    {ten_khach if ten_khach else "Khách lẻ"}

    <br><br>

    <b>Tổng số loại món:</b> {len(danh_sach_mon)}

    <br>

    <b>Tổng số ly:</b> {tong_so_ly}

    <hr>
    """,
    unsafe_allow_html=True
)

# ============================================================
# CHI TIẾT BILL
# ============================================================

for i, mon in enumerate(danh_sach_mon):

    topping_text = ", ".join(mon["topping"])

    if not topping_text:
        topping_text = "Không có"

    st.markdown(
        f"""
        <div class="mon-box">

        <b>🧋 MÓN {i + 1}: {mon["loai"]}</b>

        <br><br>

        Số lượng: {mon["so_luong"]}<br>

        Đường: {mon["duong"]}<br>

        Đá: {mon["da"]}<br>

        Topping: {topping_text}<br>

        Đơn giá trà sữa: {mon["gia_tra_sua"]:,} VNĐ<br>

        Tiền topping / ly: {mon["gia_topping"]:,} VNĐ<br>

        Đơn giá / ly: {mon["gia_mot_ly"]:,} VNĐ<br>

        <b>Thành tiền: {mon["thanh_tien"]:,} VNĐ</b>

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <div class="total">
        TỔNG TIỀN: {tong_tien:,} VNĐ
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TẠO FILE HÓA ĐƠN
# ============================================================

thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

noi_dung_hoa_don = ""

noi_dung_hoa_don += "=" * 50 + "\n"
noi_dung_hoa_don += f"{TEN_QUAN:^50}\n"
noi_dung_hoa_don += f"Địa chỉ: {DIA_CHI:^38}\n"
noi_dung_hoa_don += "=" * 50 + "\n\n"

noi_dung_hoa_don += "HÓA ĐƠN BÁN HÀNG\n\n"

noi_dung_hoa_don += f"Thời gian: {thoi_gian}\n"

noi_dung_hoa_don += (
    f"Khách hàng: "
    f"{ten_khach if ten_khach else 'Khách lẻ'}\n"
)

noi_dung_hoa_don += "\n" + "-" * 50 + "\n"

for i, mon in enumerate(danh_sach_mon):

    noi_dung_hoa_don += f"\nMÓN {i + 1}\n"

    noi_dung_hoa_don += f"Tên món: {mon['loai']}\n"

    noi_dung_hoa_don += f"Số lượng: {mon['so_luong']}\n"

    noi_dung_hoa_don += f"Đường: {mon['duong']}\n"

    noi_dung_hoa_don += f"Đá: {mon['da']}\n"

    if mon["topping"]:
        topping_text = ", ".join(mon["topping"])
    else:
        topping_text = "Không có"

    noi_dung_hoa_don += (
        f"Topping: {topping_text}\n"
    )

    noi_dung_hoa_don += (
        f"Đơn giá / ly: "
        f"{mon['gia_mot_ly']:,} VNĐ\n"
    )

    noi_dung_hoa_don += (
        f"Thành tiền: "
        f"{mon['thanh_tien']:,} VNĐ\n"
    )

    noi_dung_hoa_don += "-" * 50 + "\n"

noi_dung_hoa_don += f"\nTỔNG SỐ LY: {tong_so_ly}\n"

noi_dung_hoa_don += (
    f"TỔNG THANH TOÁN: "
    f"{tong_tien:,} VNĐ\n"
)

noi_dung_hoa_don += "\n" + "=" * 50 + "\n"

noi_dung_hoa_don += "CẢM ƠN QUÝ KHÁCH!\n"

noi_dung_hoa_don += "HẸN GẶP LẠI LẦN SAU 🧋\n"

noi_dung_hoa_don += "=" * 50

# ============================================================
# THANH TOÁN
# ============================================================

st.divider()

if st.button(
    "💳 THANH TOÁN & XUẤT HÓA ĐƠN",
    use_container_width=True,
    type="primary"
):

    if ten_khach.strip():
        ten_hien_thi = ten_khach.strip()
    else:
        ten_hien_thi = "Khach_le"

    ten_file = ""

    for c in ten_hien_thi:
        if c.isalnum() or c in (" ", "_", "-"):
            ten_file += c

    ten_file = ten_file.replace(" ", "_")

    filename = (
        f"HoaDon_{ten_file}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    st.success(
        f"✅ Thanh toán thành công! "
        f"Tổng tiền: {tong_tien:,} VNĐ"
    )

    st.download_button(
        "📥 TẢI FILE HÓA ĐƠN",
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
