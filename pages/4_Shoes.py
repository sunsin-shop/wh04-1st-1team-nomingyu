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
    "https://private-user-images.githubusercontent.com/194044465/414082749-4b18c2b7-44b1-4d83-bba4-ee2b851a70e8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk4NDk5ODksIm5iZiI6MTczOTg0OTY4OSwicGF0aCI6Ii8xOTQwNDQ0NjUvNDE0MDgyNzQ5LTRiMThjMmI3LTQ0YjEtNGQ4My1iYmE0LWVlMmI4NTFhNzBlOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxOFQwMzM0NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02YmY4ZjU2MmExNWQ1NGVkMTEyODhlMTdkOTU2NjQ5YzQyODAzYmM3NmE5MDE2NDMwZGQ1MDVhODdmZGQ3MWU2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.cR0UH9flXyxw7wd7NL9jE39isiEeEpbuV_evGf8CT0U",
    "https://private-user-images.githubusercontent.com/194044465/414082717-70940fc8-f068-4c5d-bb9a-40017c0dd4fb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk4NDk5ODksIm5iZiI6MTczOTg0OTY4OSwicGF0aCI6Ii8xOTQwNDQ0NjUvNDE0MDgyNzE3LTcwOTQwZmM4LWYwNjgtNGM1ZC1iYjlhLTQwMDE3YzBkZDRmYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxOFQwMzM0NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMmQ1Y2ZlOGQyZTBkOTYzZGZkMmI1NDhlODE1ZGNkNzhiNjA5NzEwOWIxZGVjOTY0OTcxY2IzODZjYmQ0ZjE0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.7B8Nhm-9XAME6seC6d5EP0XQisHVqC2I5RmZb9Iuaww"
]
if search_keyword:
    st.image(image_urls, caption=["일별 최고가 최저가", "일별 가격 추이"])
    

if shoe_Keyword:
    st.subheader("취향 분석 기반 신발 추천 ")
    st.image("https://private-user-images.githubusercontent.com/194044465/414085006-99360866-906c-45bf-8888-984f81d090d5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk4NTA1NTYsIm5iZiI6MTczOTg1MDI1NiwicGF0aCI6Ii8xOTQwNDQ0NjUvNDE0MDg1MDA2LTk5MzYwODY2LTkwNmMtNDViZi04ODg4LTk4NGY4MWQwOTBkNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxOFQwMzQ0MTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNGUxMWM3OTA1ZWZkYjQ4NGRmOTUyNjU3OGU1MTRhZTc3MjQ3NmZiNTYwMDRmYTZkYTEzMDZkODVkNWM0NjkyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.hkl-hJXOnlylLKB0U8pFXC79djAq8jyWyGpDxZ6GtrY")
    data = {
            "출시일": ["2024-02-21"],
            "상품명": ["Air Foamposite One Galaxy"],
            "판매가 (₩)": ["269,000"],
            "판매처": ["nike.com, SNKRS APP, SNKRS 홍대, Kasina, Worksout, Kith"],
            "발매방법":["DRAW"]
            }

    df = pd.DataFrame(data)
    st.table(df)