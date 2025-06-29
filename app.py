
import streamlit as st
import pandas as pd

st.set_page_config(page_title="วัสดุ | Material Form", layout="centered")

st.title("📦 แบบฟอร์มเก็บข้อมูลวัสดุ")

# รายชื่อจังหวัดในประเทศไทย
thai_provinces = [
    "กรุงเทพมหานคร", "กระบี่", "กาญจนบุรี", "กาฬสินธุ์", "กำแพงเพชร", "ขอนแก่น", "จันทบุรี",
    "ฉะเชิงเทรา", "ชลบุรี", "ชัยนาท", "ชัยภูมิ", "ชุมพร", "เชียงราย", "เชียงใหม่", "ตรัง", "ตราด",
    "ตาก", "นครนายก", "นครปฐม", "นครพนม", "นครราชสีมา", "นครศรีธรรมราช", "นครสวรรค์", "นนทบุรี",
    "นราธิวาส", "น่าน", "บึงกาฬ", "บุรีรัมย์", "ปทุมธานี", "ประจวบคีรีขันธ์", "ปราจีนบุรี", "ปัตตานี",
    "พระนครศรีอยุธยา", "พะเยา", "พังงา", "พัทลุง", "พิจิตร", "พิษณุโลก", "เพชรบุรี", "เพชรบูรณ์",
    "แพร่", "ภูเก็ต", "มหาสารคาม", "มุกดาหาร", "แม่ฮ่องสอน", "ยโสธร", "ยะลา", "ร้อยเอ็ด", "ระนอง",
    "ระยอง", "ราชบุรี", "ลพบุรี", "ลำปาง", "ลำพูน", "เลย", "ศรีสะเกษ", "สกลนคร", "สงขลา", "สตูล",
    "สมุทรปราการ", "สมุทรสงคราม", "สมุทรสาคร", "สระแก้ว", "สระบุรี", "สิงห์บุรี", "สุโขทัย",
    "สุพรรณบุรี", "สุราษฎร์ธานี", "สุรินทร์", "หนองคาย", "หนองบัวลำภู", "อ่างทอง", "อำนาจเจริญ",
    "อุดรธานี", "อุตรดิตถ์", "อุทัยธานี", "อุบลราชธานี"
]

# สร้างตัวแปรเก็บข้อมูล
if "materials" not in st.session_state:
    st.session_state.materials = []

# ฟอร์มป้อนข้อมูล
with st.form("material_form", clear_on_submit=True):
    name = st.text_input("ชื่อของวัสดุ")

    col1, col2, col3 = st.columns(3)
    with col1:
        width = st.number_input("ความกว้าง (mm)", min_value=0.0, step=0.1)
    with col2:
        depth = st.number_input("ความลึก (mm)", min_value=0.0, step=0.1)
    with col3:
        length = st.number_input("ความยาว (mm)", min_value=0.0, step=0.1)

    province = st.selectbox("จังหวัดที่ตั้งวัสดุ", thai_provinces)

    submit = st.form_submit_button("📥 บันทึกข้อมูลวัสดุ")

    if submit:
        st.session_state.materials.append({
            "ชื่อวัสดุ": name,
            "กว้าง (mm)": width,
            "ลึก (mm)": depth,
            "ยาว (mm)": length,
            "จังหวัด": province
        })
        st.success("✅ บันทึกข้อมูลวัสดุเรียบร้อยแล้ว!")

# แสดงข้อมูลวัสดุที่บันทึกไว้
if st.session_state.materials:
    st.markdown("---")
    st.subheader("📋 ข้อมูลวัสดุทั้งหมด")
    df = pd.DataFrame(st.session_state.materials)
    st.dataframe(df, use_container_width=True)
