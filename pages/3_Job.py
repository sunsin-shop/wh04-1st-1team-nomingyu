import streamlit as st
import pandas as pd

# ✅ Streamlit 페이지 설정
st.set_page_config(page_title="취업 지원 서비스", layout="centered")

# ✅ 타이틀
st.title("🚀 취업 지원 서비스")
st.write("빠르게 원하는 채용 공고를 검색하고 필터링하세요.")

# ✅ 🔹 직군별 URL 및 이미지 매핑 (공고 이동 URL 포함)
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

# ✅ 직군 선택 (이미지 + URL 이동 포함)
st.subheader("🔍 채용 공고 검색 및 필터링")

# ✅ 직군 선택 박스
job_category = st.selectbox("💼 직군을 선택하세요:", list(job_data.keys()))

# ✅ 직군 선택 후 이미지 표시 (줄바꿈 없이 정렬)
st.image(job_data[job_category]["image"], width=750)

# ✅ 검색 버튼 (채용 공고 이동 URL 포함)
if st.button(f"📢 {job_category} 채용 검색"):
    st.markdown(f"🔗 [{job_category} 채용 공고 보기]({job_data[job_category]['url']})", unsafe_allow_html=True)

# ✅ 🔹 필터링 UI (직군 선택 아래 정리)
st.subheader("🎯 채용 공고 필터링")
selected_role = st.multiselect("🎓 직무 선택", ["백엔드", "프론트엔드", "데이터 엔지니어", "디자인"], default=["백엔드"])
selected_location = st.multiselect("📍 지역 선택", ["서울", "경기", "부산"], default=["서울"])
selected_experience = st.multiselect("💼 경력 선택", ["신입", "경력"], default=["신입"])

# ✅ 샘플 데이터
data = {
    "회사명": ["삼성전자", "카카오", "네이버", "라인", "쿠팡"],
    "직무": ["백엔드", "프론트엔드", "데이터 엔지니어", "백엔드", "디자인"],
    "지역": ["서울", "경기", "서울", "부산", "서울"],
    "경력": ["신입", "경력", "신입", "경력", "신입"],
    "공고 링크": [
        "https://samsung.com",
        "https://kakao.com",
        "https://naver.com",
        "https://www.line.me/ko/",
        "https://coupang.com"
    ]
}
df = pd.DataFrame(data)

# ✅ 필터링 적용
filtered_df = df[
    (df["직무"].isin(selected_role)) &
    (df["지역"].isin(selected_location)) &
    (df["경력"].isin(selected_experience))
]

# ✅ 필터링된 데이터 출력
st.subheader("📊 필터링된 채용 공고")
st.dataframe(filtered_df)

# ✅ 공고 링크 추가
if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        st.markdown(f"🔗 [{row['회사명']} 채용 공고]({row['공고 링크']})")
