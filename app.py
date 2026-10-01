# ============================================================
# HÀM CHATBOT
# ============================================================

def chatbot_tra_loi(cau_hoi):

    cau_hoi = cau_hoi.lower().strip()

    # ========================================================
    # CHÀO HỎI
    # ========================================================

    if (
        "xin chào" in cau_hoi
        or cau_hoi == "chào"
        or "hello" in cau_hoi
        or cau_hoi == "hi"
        or "alo" in cau_hoi
    ):
        return (
            "Xin chào bạn 👋🧋\n\n"
            "Mình có thể tư vấn món, giá tiền, "
            "size, topping, đường, đá và địa chỉ quán nhé!"
        )

    # ========================================================
    # ĐỊA CHỈ
    # ========================================================

    if (
        "địa chỉ" in cau_hoi
        or "ở đâu" in cau_hoi
        or "địa điểm" in cau_hoi
    ):
        return (
            f"📍 Quán {TEN_QUAN} ở địa chỉ:\n"
            f"{DIA_CHI}"
        )

    # ========================================================
    # MENU
    # ========================================================

    if (
        "menu" in cau_hoi
        or "có món gì" in cau_hoi
        or "món gì" in cau_hoi
        or "trà sữa gì" in cau_hoi
    ):

        tra_loi = "🧋 CÁC MÓN TRÀ SỮA:\n\n"

        for ten_mon, gia in MENU.items():
            tra_loi += (
                f"• {ten_mon}: "
                f"{gia:,} VNĐ/ly\n"
            )

        return tra_loi

    # ========================================================
    # SIZE
    # ========================================================

    if (
        "size" in cau_hoi
        or "cỡ" in cau_hoi
    ):
        return (
            "📏 QUÁN CÓ 3 SIZE:\n\n"
            "• Size S: Không phụ thu\n"
            "• Size M: +5.000 VNĐ\n"
            "• Size L: +10.000 VNĐ\n\n"
            "Bạn có thể chọn size phù hợp với nhu cầu nhé! 🧋"
        )

    # ========================================================
    # SIZE S
    # ========================================================

    if (
        "size s" in cau_hoi
        or "cỡ s" in cau_hoi
    ):
        return (
            "📏 Size S\n\n"
            "Giá size S: Không phụ thu."
        )

    # ========================================================
    # SIZE M
    # ========================================================

    if (
        "size m" in cau_hoi
        or "cỡ m" in cau_hoi
    ):
        return (
            "📏 Size M\n\n"
            "Phụ thu: 5.000 VNĐ."
        )

    # ========================================================
    # SIZE L
    # ========================================================

    if (
        "size l" in cau_hoi
        or "cỡ l" in cau_hoi
    ):
        return (
            "📏 Size L\n\n"
            "Phụ thu: 10.000 VNĐ."
        )

    # ========================================================
    # TOPPING
    # ========================================================

    if (
        "topping" in cau_hoi
        or "thêm gì" in cau_hoi
        or "có topping gì" in cau_hoi
    ):

        tra_loi = "🍮 CÁC LOẠI TOPPING:\n\n"

        for ten_topping, gia in TOPPINGS.items():

            tra_loi += (
                f"• {ten_topping}: "
                f"{gia:,} VNĐ\n"
            )

        return tra_loi

    # ========================================================
    # HỎI GIÁ MỘT MÓN
    # ========================================================

    for ten_mon, gia in MENU.items():

        if ten_mon.lower() in cau_hoi:

            return (
                f"🧋 {ten_mon}\n\n"
                f"Giá size S: {gia:,} VNĐ/ly\n"
                f"Size M: +5.000 VNĐ\n"
                f"Size L: +10.000 VNĐ"
            )

    # ========================================================
    # HỎI GIÁ TOPPING
    # ========================================================

    for ten_topping, gia in TOPPINGS.items():

        if ten_topping.lower() in cau_hoi:

            return (
                f"🍮 {ten_topping}\n\n"
                f"Giá: {gia:,} VNĐ/ly."
            )

    # ========================================================
    # MÓN RẺ NHẤT
    # ========================================================

    if (
        "rẻ nhất" in cau_hoi
        or "món rẻ" in cau_hoi
        or "giá rẻ nhất" in cau_hoi
    ):

        gia_re_nhat = min(MENU.values())

        mon_re_nhat = []

        for ten_mon, gia in MENU.items():

            if gia == gia_re_nhat:
                mon_re_nhat.append(ten_mon)

        tra_loi = "💰 MÓN RẺ NHẤT:\n\n"

        for ten_mon in mon_re_nhat:
            tra_loi += f"• {ten_mon}\n"

        tra_loi += (
            f"\nGiá: {gia_re_nhat:,} VNĐ/ly size S."
        )

        return tra_loi

    # ========================================================
    # MÓN ĐẮT NHẤT
    # ========================================================

    if (
        "đắt nhất" in cau_hoi
        or "mắc nhất" in cau_hoi
    ):

        gia_cao_nhat = max(MENU.values())

        mon_cao_nhat = []

        for ten_mon, gia in MENU.items():

            if gia == gia_cao_nhat:
                mon_cao_nhat.append(ten_mon)

        tra_loi = "💰 MÓN CÓ GIÁ CAO NHẤT:\n\n"

        for ten_mon in mon_cao_nhat:
            tra_loi += f"• {ten_mon}\n"

        tra_loi += (
            f"\nGiá: {gia_cao_nhat:,} VNĐ/ly size S."
        )

        return tra_loi

    # ========================================================
    # TƯ VẤN ĐƯỜNG
    # ========================================================

    if (
        "ít ngọt" in cau_hoi
        or "ít đường" in cau_hoi
        or "giảm ngọt" in cau_hoi
    ):

        return (
            "🍬 Nếu bạn thích uống ít ngọt, "
            "mình gợi ý chọn đường 70% "
            "hoặc 0% tùy khẩu vị nhé!"
        )

    if (
        "nhiều đường" in cau_hoi
        or "ngọt hơn" in cau_hoi
    ):

        return (
            "🍬 Nếu bạn thích vị ngọt rõ hơn, "
            "có thể chọn mức đường 100% nhé!"
        )

    # ========================================================
    # TƯ VẤN ĐÁ
    # ========================================================

    if (
        "ít đá" in cau_hoi
        or "ít lạnh" in cau_hoi
    ):

        return (
            "🧊 Bạn có thể chọn đá 70% "
            "hoặc 0% nếu không muốn uống quá lạnh."
        )

    if "nhiều đá" in cau_hoi:

        return (
            "🧊 Nếu bạn thích uống lạnh hơn, "
            "có thể chọn mức đá 100% nhé!"
        )

    # ========================================================
    # CẢM ƠN
    # ========================================================

    if (
        "cảm ơn" in cau_hoi
        or "thank" in cau_hoi
    ):

        return (
            f"🥰 Không có gì ạ!\n\n"
            f"Cảm ơn bạn đã ủng hộ {TEN_QUAN} 🧋❤️"
        )

    # ========================================================
    # CÂU HỎI KHÔNG XÁC ĐỊNH
    # ========================================================

    return (
        "🤖 Mình chưa hiểu câu hỏi này lắm 😅\n\n"
        "Bạn có thể hỏi như:\n"
        "• Quán có những món gì?\n"
        "• Trà sữa matcha bao nhiêu?\n"
        "• Có những topping nào?\n"
        "• Trân châu đen bao nhiêu?\n"
        "• Có những size nào?\n"
        "• Size M thêm bao nhiêu tiền?\n"
        "• Size L thêm bao nhiêu tiền?\n"
        "• Món nào rẻ nhất?\n"
        "• Quán ở đâu?\n"
        "• Tôi muốn uống ít ngọt.\n"
        "• Tôi muốn ít đá."
      )
