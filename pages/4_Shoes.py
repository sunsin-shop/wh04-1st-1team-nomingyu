import streamlit as st
import pandas as pd
import csv
import os
import json
import datetime
#from streamlit_calendar import calendar

st.set_page_config(page_title="Shoes Analysis", page_icon = "🔍", layout="wide")
#st.page_link("Main.py", label="Back to Main", icon="🏠")
st.title("Shoes Analysis")

st.markdown("""
    <style>
        div[data-baseweb="select"] {
            width: 400px !important;
        }
        div[data-baseweb="select"] > div {
            font-size: 18px !important;
        }
""", unsafe_allow_html=True)

st.text_input("검색 할 신발의 이름을 입력하세요", placeholder= "ex: jordan 1")
alig_list=["내림차순","오름차순"]
st.selectbox("결과 출력물의 정렬 방식을 선택하세요", alig_list, index=None, placeholder="결과 출력물의 정렬 방식을 선택하세요")

search_column_list =["거래량","출시 가격","평균 거래가격","최고 거래가격","최저 거래가격"]

st.selectbox("정렬 기준으로 사용할 내용을 선택하세요",search_column_list, index=None, placeholder="정렬 기준으로 사용할 내용을 선택하세요")

search_keyword = st.button("조회하기")


image_urls = [
    "https://github.com/user-attachments/assets/765f8b42-3af3-4070-83ea-83ab9227f9bb",
    "https://github.com/user-attachments/assets/246186d2-9569-410c-a959-5ea844447251"
]
if search_keyword:
    st.image(image_urls, caption=["일별 최고가 최저가", "일별 가격 추이"])

st.text_input("보유하거나 관심있는 신발의 이름을 입력하세요", placeholder= "ex: jordan 1, air max")

shoe_Keyword = st.button("분석하기",key="analysis_btn")   

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

st.title("가족 일정 입력")

with st.form("schedule_form"):
    event_name = st.text_input("이벤트 이름")
    event_date = st.date_input("날짜 선택", datetime.date.today())
    start_time = st.time_input("시작 시간", datetime.time(9, 0))
    end_time = st.time_input("종료 시간", datetime.time(10, 0))

    submit = st.form_submit_button("일정 추가")
    
    
if submit:
    st.success(f"일정이 추가되었습니다: {event_name}")