import streamlit as st
import pandas as pd

# ✅ Streamlit 페이지 설정
st.set_page_config(page_title="취업 지원 서비스", layout="centered")

# ✅ 타이틀
st.title("🚀 취업 지원 서비스")
st.write("빠르게 원하는 채용 공고를 검색하고 필터링하세요.")

# ✅ 🔹 직군 선택 및 검색 버튼 (깔끔하게 정리)
st.subheader("🔍 채용 공고 검색 및 필터링")

col1, col2 = st.columns([2, 1])
with col1:
    job_category = st.selectbox("💼 직군을 선택하세요:", ["백엔드 개발", "프론트엔드 개발", "데이터 엔지니어", "디자인"])
with col2:
    if st.button(f"📢 {job_category} 채용 검색"):
        st.write(f"🔗 [{job_category} 채용 공고 보기](#)")

# ✅ 🔹 필터링 UI (깔끔한 정리)
col1, col2, col3 = st.columns(3)
with col1:
    selected_role = st.multiselect("🎓 직무 선택", ["백엔드", "프론트엔드", "데이터 엔지니어", "디자인"], default=["백엔드"])
with col2:
    selected_location = st.multiselect("📍 지역 선택", ["서울", "경기", "부산"], default=["서울"])
with col3:
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
        "https://line.com",
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
