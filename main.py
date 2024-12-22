import streamlit as st
import random

st.title("Lên Thực Đơn Cho Các Bữa Ăn Trong Ngày 🍽️")

breakfast_items = ["Bánh cuốn", "Hủ tiếu", "Bánh bao", "Bánh ướt", "Bánh bèo", "Mì Quảng"]
main_dishes = ["Thịt kho tàu", "Cá chiên giòn", "Gà xào sả ớt", "Sườn ram", "Tôm hấp", "Mực nướng muối ớt"]
veggie_dishes = ["Canh bí đỏ", "Rau cải luộc", "Canh khoai mỡ", "Salad rau củ", "Canh cải thịt bằm"]

def suggest_random(choices, num):
    return random.sample(choices, num)

st.header("🍳 Bữa Sáng")
breakfast = st.multiselect("Chọn món cho bữa sáng:", breakfast_items)
if st.button("Gợi ý món cho bữa sáng"):
    breakfast = suggest_random(breakfast_items, 2)
    st.write("Gợi ý món: ", ", ".join(breakfast))

st.header("🍲 Bữa Trưa")
lunch_main_dishes = st.multiselect("Chọn 2 món mặn cho bữa trưa:", main_dishes, max_selections=2)
if st.button("Gợi ý món mặn cho bữa trưa"):
    lunch_main_dishes = suggest_random(main_dishes, 2)
    st.write("Gợi ý món mặn: ", ", ".join(lunch_main_dishes))

lunch_veggie_dish = st.multiselect("Chọn 1 món rau hoặc canh cho bữa trưa:", veggie_dishes, max_selections=1)
if st.button("Gợi ý món rau/canh cho bữa trưa"):
    lunch_veggie_dish = suggest_random(veggie_dishes, 1)
    st.write("Gợi ý món rau/canh: ", ", ".join(lunch_veggie_dish))

st.header("🍛 Bữa Tối")
dinner_main_dishes = st.multiselect("Chọn 2 món mặn cho bữa tối:", main_dishes, max_selections=2)
if st.button("Gợi ý món mặn cho bữa tối"):
    dinner_main_dishes = suggest_random(main_dishes, 2)
    st.write("Gợi ý món mặn: ", ", ".join(dinner_main_dishes))

dinner_veggie_dish = st.multiselect("Chọn 1 món rau hoặc canh cho bữa tối:", veggie_dishes, max_selections=1)
if st.button("Gợi ý món rau/canh cho bữa tối"):
    dinner_veggie_dish = suggest_random(veggie_dishes, 1)
    st.write("Gợi ý món rau/canh: ", ", ".join(dinner_veggie_dish))

st.subheader("📋 Thực Đơn Của Bạn")
if breakfast:
    st.write("**Bữa sáng:**", ", ".join(breakfast))
else:
    st.write("**Bữa sáng:** Chưa chọn món")

if lunch_main_dishes and lunch_veggie_dish:
    st.write("**Bữa trưa:**", ", ".join(lunch_main_dishes + lunch_veggie_dish))
else:
    st.write("**Bữa trưa:** Chưa chọn đủ món")

if dinner_main_dishes and dinner_veggie_dish:
    st.write("**Bữa tối:**", ", ".join(dinner_main_dishes + dinner_veggie_dish))
else:
    st.write("**Bữa tối:** Chưa chọn đủ món")
