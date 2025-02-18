import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 제목 설정
st.title("지도 API 예제")
st.write("Streamlit과 Folium을 이용한 지도 페이지입니다.")

# 서울의 중심 좌표 설정
seoul_coords = [37.5665, 126.9780]

# Folium 지도 생성 (서울 중심, 초기 줌 레벨 12)
m = folium.Map(location=seoul_coords, zoom_start=12)

# 서울 위치에 마커 추가
folium.Marker(
    location=seoul_coords,
    popup="서울",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(m)

# Streamlit에서 Folium 지도 표시
st_folium(m, width=700, height=500)
