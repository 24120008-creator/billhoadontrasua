import streamlit as st
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH
# ============================================================

st.set_page_config(
    page_title="Trà Sữa Ngọt Ngào",
    page_icon="🧋",
    layout="centered"
)

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
    "Trà sữa chanh dây": 25000,
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
    "Kem cheese": 8000,
}

# ============================================================
# GIÁ SIZE
# ============================================================

SIZE_PHU_THU = {
    "S": 0,
    "M": 5000,
    "L": 10000
}

# ============================================================
# TIÊU ĐỀ
# ============================================================

st.title("🧋 TRÀ SỮA NGỌT NGÀO")

st.write(
    "📍 Địa chỉ: "
    + DIA_CHI
)

# ============================================================
# LOGO
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

st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# ============================================================
# CHỌN MÓN
# ============================================================

st.subheader("🧋 Chọn món")

ten_mon = st.selectbox(
    "Loại trà sữa",
    list(MENU.keys())
)

gia_mon = MENU[ten_mon]

st.write(
    f"💰 Giá cơ bản: **{gia_mon:,} VNĐ**"
)

# ============================================================
# CHỌN SIZE
# ============================================================

st.subheader("📏 Chọn size")

size = st.radio(
    "Size trà sữa",
    ["S", "M", "L"],
    horizontal=True
)

phu_thu_size = SIZE_PHU_THU[size]

if phu_thu_size == 0:
    st.write("Size S: **Không phụ thu**")
else:
    st.write(
        f"Size {size}: **+{phu_thu_size:,} VNĐ**"
    )

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

st.subheader("🍮 Chọn topping")

danh_sach_topping = st.multiselect(
    "Bạn muốn thêm topping nào?",
    list(TOPPINGS.keys())
)

tong_tien_topping = sum(
    TOPPINGS[topping]
    for topping in danh_sach_topping
)

# ============================================================
# ĐƯỜNG
# ============================================================

st.subheader("🍬 Mức độ đường")

muc_duong = st.radio(
    "Chọn mức đường",
    ["100%", "70%", "0%"],
    horizontal=True
)

# ============================================================
# ĐÁ
# ============================================================

st.subheader("🧊 Mức độ đá")

muc_da = st.radio(
    "Chọn mức đá",
    ["100%", "70%", "0%"],
    horizontal=True
)

# ============================================================
# TÍNH TIỀN
# ============================================================

gia_mot_ly = (
    gia_mon
    + phu_thu_size
    + tong_tien_topping
)

tong_tien = gia_mot_ly * so_luong

# ============================================================
# HIỂN THỊ TẠM TÍNH
# ============================================================

st.divider()

st.subheader("🧾 HÓA ĐƠN TẠM TÍNH")

st.write(
    f"👤 Khách hàng: **{ten_khach if ten_khach else 'Chưa nhập tên'}**"
)

st.write(f"🧋 Món: **{ten_mon}**")
st.write(f"📏 Size: **{size}**")
st.write(f"🔢 Số lượng: **{so_luong}**")
st.write(f"🍬 Đường: **{muc_duong}**")
st.write(f"🧊 Đá: **{muc_da}**")

if danh_sach_topping:
    st.write(
        "🍮 Topping: **"
        + ", ".join(danh_sach_topping)
        + "**"
    )
else:
    st.write("🍮 Topping: **Không có**")

st.write(
    f"💵 Giá 1 ly: **{gia_mot_ly:,} VNĐ**"
)

st.write(
    f"## 💰 Tổng tiền: {tong_tien:,} VNĐ"
)

# ============================================================
# NÚT THANH TOÁN
# ============================================================

st.divider()

if st.button(
    "💳 THANH TOÁN",
    use_container_width=True
):

    if not ten_khach.strip():

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng trước khi thanh toán!"
        )

    else:

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )

        st.success(
            "✅ Thanh toán thành công!"
        )

        st.markdown("---")

        st.markdown(
            f"""
### 🧋 {TEN_QUAN}

📍 {DIA_CHI}

---

**Khách hàng:** {ten_khach}

**Thời gian:** {thoi_gian}

**Món:** {ten_mon}

**Size:** {size}

**Số lượng:** {so_luong}

**Đường:** {muc_duong}

**Đá:** {muc_da}

**Topping:** {
    ", ".join(danh_sach_topping)
    if danh_sach_topping
    else "Không có"
}

---

### 💰 TỔNG THANH TOÁN: {tong_tien:,} VNĐ

❤️ Cảm ơn quý khách đã ủng hộ {TEN_QUAN}!
"""
        )

# ============================================================
# CHATBOT
# ============================================================

st.divider()

st.subheader("🤖 CHATBOT TRÀ SỮA NGỌT NGÀO")

st.write(
    "Xin chào! 👋 Mình là chatbot của TRÀ SỮA NGỌT NGÀO."
)

st.write(
    "Bạn có thể hỏi mình về món, giá tiền, size, "
    "topping, đường, đá hoặc địa chỉ quán nhé! 🧋"
)

# ============================================================
# LƯU LỊCH SỬ CHAT
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# ============================================================
# HÀM CHATBOT
# ============================================================

def chatbot_tra_loi(cau_hoi):

    cau_hoi = cau_hoi.lower().strip()

    # --------------------------------------------------------
    # CHÀO HỎI
    # --------------------------------------------------------

    if any(
        x in cau_hoi
        for x in [
            "xin chào",
            "chào",
            "hello",
            "hi",
            "alo"
        ]
    ):

        return (
            "Xin chào bạn 👋🧋\n\n"
            "Mình có thể tư vấn món, giá trà sữa, "
            "size, topping, mức đường, mức đá "
            "và thông tin quán cho bạn nhé!"
        )

    # --------------------------------------------------------
    # ĐỊA CHỈ
    # --------------------------------------------------------

    if (
        "địa chỉ" in cau_hoi
        or "ở đâu" in cau_hoi
        or "địa điểm" in cau_hoi
    ):

        return (
            f"📍 Quán {TEN_QUAN} "
            f"ở địa chỉ: {DIA_CHI}"
        )

    # --------------------------------------------------------
    # MENU
    # --------------------------------------------------------

    if (
        "menu" in cau_hoi
        or "có món gì" in cau_hoi
        or "món gì" in cau_hoi
        or "trà sữa gì" in cau_hoi
    ):

        tra_loi = "🧋 Các món trà sữa hiện có:\n\n"

        for ten_mon_menu, gia in MENU.items():

            tra_loi += (
                f"• {ten_mon_menu}: "
                f"{gia:,} VNĐ\n"
            )

        return tra_loi

    # --------------------------------------------------------
    # SIZE
    # --------------------------------------------------------

    if (
        "size" in cau_hoi
        or "cỡ" in cau_hoi
    ):

        return (
            "📏 Quán có 3 size:\n\n"
            "• Size S: Không phụ thu\n"
            "• Size M: +5.000 VNĐ\n"
            "• Size L: +10.000 VNĐ\n\n"
            "Bạn có thể chọn size phù hợp với nhu cầu nhé! 🧋"
        )

    # --------------------------------------------------------
    # SIZE S
    # --------------------------------------------------------

    if (
        "size s" in cau_hoi
        or "cỡ s" in cau_hoi
    ):

        return (
            "📏 Size S: Không phụ thu.\n"
            "Phù hợp nếu bạn muốn một ly nhỏ vừa đủ nhé! 🧋"
        )

    # --------------------------------------------------------
    # SIZE M
    # --------------------------------------------------------

    if (
        "size m" in cau_hoi
        or "cỡ m" in cau_hoi
    ):

        return (
            "📏 Size M: Phụ thu 5.000 VNĐ.\n"
            "Đây là size vừa, phù hợp cho nhu cầu uống thông thường. 🧋"
        )

    # --------------------------------------------------------
    # SIZE L
    # --------------------------------------------------------

    if (
        "size l" in cau_hoi
        or "cỡ l" in cau_hoi
    ):

        return (
            "📏 Size L: Phụ thu 10.000 VNĐ.\n"
            "Đây là size lớn, phù hợp nếu bạn muốn uống nhiều hơn. 🧋"
        )

    # --------------------------------------------------------
    # TOPPING
    # --------------------------------------------------------

    if (
        "topping" in cau_hoi
        or "thêm gì" in cau_hoi
    ):

        tra_loi = "🍮 Các loại topping:\n\n"

        for ten_topping, gia in TOPPINGS.items():

            tra_loi += (
                f"• {ten_topping}: "
                f"{gia:,} VNĐ\n"
            )

        return tra_loi

    # --------------------------------------------------------
    # GIÁ MỘT MÓN
    # --------------------------------------------------------

    for ten_mon_menu, gia in MENU.items():

        if ten_mon_menu.lower() in cau_hoi:

            return (
                f"🧋 {ten_mon_menu} có giá "
                f"{gia:,} VNĐ/ly size S.\n\n"
                "Size M phụ thu 5.000 VNĐ.\n"
                "Size L phụ thu 10.000 VNĐ."
            )

    # --------------------------------------------------------
    # GIÁ TOPPING
    # --------------------------------------------------------

    for ten_topping, gia in TOPPINGS.items():

        if ten_topping.lower() in cau_hoi:

            return (
                f"🍮 {ten_topping
