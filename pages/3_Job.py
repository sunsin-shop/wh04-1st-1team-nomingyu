import streamlit as st
import pandas as pd

# Streamlit 설정
st.set_page_config(page_title="취업 지원 서비스", layout="centered")

st.title("🚀 취업 지원 서비스")
st.write("Streamlit 기반으로 원티드 채용 공고를 실시간으로 확인하고 필터링할 수 있습니다.")

# # ✅ Streamlit에서 CSS 스타일 추가 (셀렉트 박스 크기 조정)
# st.markdown("""
#     <style>
#         div[data-baseweb="select"] {
#             width: 400px !important;
#         }
#         div[data-baseweb="select"] > div {
#             font-size: 18px !important;
#         }

# """, unsafe_allow_html=True)

# ✅ 직군별 URL 및 이미지 매핑
job_data = {
    "백엔드 개발": {
        "image": "https://github.com/user-attachments/assets/1929d3c5-8e87-4c40-bec6-c62f2cfcd627",
        "url": "https://www.wanted.co.kr/search?query=%EB%B0%B1%EC%97%94%EB%93%9C&tab=overview"
    },
    "프론트엔드 개발": {
        "image": "https://github.com/user-attachments/assets/caac5c8f-c4d3-45ea-b597-ef9fcbe2117f",
        "url": "https://www.wanted.co.kr/search?query=%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&tab=overview"
    },
    "데이터 엔지니어": {
        "image": "https://github.com/user-attachments/assets/4f40c265-930a-4edb-8248-7096638ff852",
        "url": "https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&tab=overview"
    },
    "디자인": {
        "image": "https://github.com/user-attachments/assets/688f1644-c40e-4103-8985-50b23ffd317a",
        "url": "https://www.wanted.co.kr/search?query=%EB%94%94%EC%9E%90%EC%9D%B8&tab=overview"
    }
}

# ✅ 사용자 입력 받기 (직군 선택)
job_category = st.selectbox(
    "원하는 직군을 선택하세요:",
    list(job_data.keys())
)

# ✅ 버튼 클릭 시 해당 직군의 사이트 링크를 마크다운으로 표시
if st.button(f"{job_category} 채용 확인"):
    st.markdown(f"""
    ### 📌 {job_category} 채용 공고
    🔗 [**{job_category} 채용 공고 사이트 이동**]({job_data[job_category]['url']})
    ![{job_category} 관련 이미지]({job_data[job_category]["image"]})
    """)

# ✅ 채용 공고 데이터 생성 (예제 데이터)
data = {
    "회사명": ["삼성전자", "카카오", "네이버", "라인", "쿠팡"],
    "직무": ["백엔드", "프론트엔드", "데이터 엔지니어", "백엔드", "디자인"],
    "지역": ["서울", "경기", "서울", "부산", "서울"],
    "경력": ["신입", "경력", "신입", "경력", "신입"],
    "필수 기술": ["Python, Django", "React, Vue", "SQL, Python", "Java, Spring", "Figma, UI/UX"],
    "공고 링크": [
        "https://samsung.com",
        "https://kakao.com",
        "https://naver.com",
        "https://line.com",
        "https://coupang.com"
    ]
}

df = pd.DataFrame(data)

st.subheader("🔍 채용 공고 필터링")
# ✅ 필터링 UI 추가 (직무, 지역, 경력)
selected_role = st.multiselect("직무 선택", df["직무"].unique(), default=df["직무"].unique())
selected_location = st.multiselect("지역 선택", df["지역"].unique(), default=df["지역"].unique())
selected_experience = st.multiselect("경력", df["경력"].unique(), default=df["경력"].unique())

# ✅ 필터링 적용
filtered_df = df[
    (df["직무"].isin(selected_role)) &
    (df["지역"].isin(selected_location)) &
    (df["경력"].isin(selected_experience))
]

# ✅ 필터링된 데이터 출력
st.write("### 필터링된 채용 공고")
st.dataframe(filtered_df)

# ✅ 공고 링크 추가
for index, row in filtered_df.iterrows():
    st.markdown(f"[{row['회사명']} 채용 공고]({row['공고 링크']})")
