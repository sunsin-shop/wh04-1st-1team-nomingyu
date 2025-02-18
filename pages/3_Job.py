# 취업 지원 서비스

import streamlit as st


# Streamlit 설정
st.set_page_config(page_title="원티드 채용 공고 크롤러", layout="wide")

st.title("🚀 원티드 채용 공고 크롤링")
st.write("Streamlit 기반으로 원티드 채용 공고를 실시간으로 크롤링합니다.")

# ✅ Streamlit에서 CSS 스타일 추가 (셀렉트 박스 크기 조정)
st.markdown("""
    <style>
        /* selectbox 전체 크기 조정 */
        div[data-baseweb="select"] {
            width: 400px !important;  /* 원하는 크기로 변경 */
        }
        
        /* selectbox 내부 텍스트 크기 조정 */
        div[data-baseweb="select"] > div {
            font-size: 18px !important;  /* 글자 크기 조정 */
        }
    </style>
""", unsafe_allow_html=True)

# ✅ 직군별 URL 매핑
job_urls = {
    "백엔드 개발": "https://www.wanted.co.kr/search?query=%EB%B0%B1%EC%97%94%EB%93%9C&tab=overview",
    "프론트엔드 개발": "https://www.wanted.co.kr/search?query=%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&tab=overview",
    "데이터 엔지니어": "https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&tab=overview",
    "디자인": "https://www.wanted.co.kr/search?query=%EB%94%94%EC%9E%90%EC%9D%B8&tab=overview"
}
job_data = {
    "백엔드 개발": {
        "image": "https://github.com/user-attachments/assets/1929d3c5-8e87-4c40-bec6-c62f2cfcd627",  # 업로드한 이미지 URL로 변경
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
    list(job_urls.keys())  # 딕셔너리의 키(직군명)만 리스트로 변환
)

# ✅ 버튼 클릭 시 해당 직군의 사이트 링크를 마크다운으로 표시
if st.button(f"{job_category} 채용 확인"):
    job_url = job_urls[job_category]
    st.markdown(f"""
### 📌 {job_category} 채용 공고
🔗 [**{job_category} 채용 공고 사이트 이동**]({job_data[job_category]['url']})

![{job_category} 관련 이미지]({job_data[job_category]["image"]})

""")
