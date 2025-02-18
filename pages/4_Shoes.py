import streamlit as st
import pandas as pd


st.set_page_config(page_title="Shoes Analysis", page_icon = "🔍")
#st.page_link("Main.py", label="Back to Main", icon="🏠")
st.title("Shoes Analysis")


st.text_input("검색 할 신발의 이름을 입력하세요", placeholder= "ex: jordan 1")
search_keyword = st.button("조회하기")

st.text_input("보유하거나 관심있는 신발의 이름을 입력하세요", placeholder= "ex: jordan 1, air max")
shoe_Keyword = st.button("분석하기",key="analysis_btn")
image_urls = [
    "https://github.com/user-attachments/assets/2c8a7f7d-46ea-432b-818e-ca8fd8a36013",
    "https://github.com/user-attachments/assets/246186d2-9569-410c-a959-5ea844447251"
]
if search_keyword:
    st.image(image_urls, caption=["일별 최고가 최저가", "일별 가격 추이"])
    

if shoe_Keyword:
    st.subheader("취향 분석 기반 신발 추천 ")
    st.image("https://github.com/user-attachments/assets/3489bc82-8d11-4b0b-8941-8cc37a91544c")
    data = {
            "출시일": ["2024-02-21"],
            "상품명": ["Air Foamposite One Galaxy"],
            "판매가 (₩)": ["269,000"],
            "판매처": ["nike.com, SNKRS APP, SNKRS 홍대, Kasina, Worksout, Kith"],
            "발매방법":["DRAW"]
            }

    df = pd.DataFrame(data)
    st.table(df)