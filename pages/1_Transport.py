import streamlit as st
import pandas as pd
import folium
import math
import random
from streamlit_folium import st_folium
#import folium
#from streamlit_folium import st_folium

# 교통 페이지입니다.
st.set_page_config(page_title="Transport Navigation ", page_icon = "🚊🚍🚏")

# 페이지 제목 설정
st.title("Transport Navigation 🚊🚍🚏")

st.write("교통경로 추천 및 환승정보 제공")

# 미리 정의한 장소들 (예: 서울의 주요 위치)
places1 = {
    "집": {"lat": 37.6732, "lon": 127.0538},
    "노량진역": {"lat": 37.5128, "lon": 126.9412},
    "서울 시청": {"lat": 37.5665, "lon": 126.9780},
    "경복궁": {"lat": 37.5796, "lon": 126.9770},
    "N서울타워": {"lat": 37.5512, "lon": 126.9882},
    "인천공항": {"lat": 37.4602, "lon": 126.4407},
}
places2 = {
    "노량진역": {"lat": 37.5128, "lon": 126.9412},
    "집": {"lat": 37.6732, "lon": 127.0538},
    "서울 시청": {"lat": 37.5665, "lon": 126.9780},
    "경복궁": {"lat": 37.5796, "lon": 126.9770},
    "N서울타워": {"lat": 37.5512, "lon": 126.9882},
    "인천공항": {"lat": 37.4602, "lon": 126.4407},
}

# --- 즐겨찾기 불러오기 버튼 (페이지 상단) ---
if st.button("즐겨찾기 불러오기"):
    if "favorite_departure" in st.session_state and "favorite_destination" in st.session_state:
        fav_dep = st.session_state.favorite_departure
        fav_dest = st.session_state.favorite_destination
        st.success(f"즐겨찾기가 불러와졌습니다! 출발지: {fav_dep}, 도착지: {fav_dest}")
    else:
        st.warning("저장된 즐겨찾기가 없습니다!")

# 출발지와 도착지 입력 탭 생성
tab1, tab2 = st.tabs(["출발지", "도착지"])

with tab1:
    departure = st.selectbox("출발지를 선택하세요", list(places1.keys()))
with tab2:
    destination = st.selectbox("도착지를 선택하세요", list(places2.keys()))

# 선택한 장소의 좌표 가져오기
dep = places1[departure]
dest = places2[destination]

# 지도 중심 좌표 (두 지점의 중간값)
center_lat = (dep["lat"] + dest["lat"]) / 2
center_lon = (dep["lon"] + dest["lon"]) / 2

# Folium 지도 객체 생성
m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# 출발지 마커 추가 (녹색 아이콘)
folium.Marker(
    location=[dep["lat"], dep["lon"]],
    popup=f"출발지: {departure}",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

# 도착지 마커 추가 (빨간색 아이콘)
folium.Marker(
    location=[dest["lat"], dest["lon"]],
    popup=f"도착지: {destination}",
    icon=folium.Icon(color="red", icon="flag")
).add_to(m)

# 출발지와 도착지를 연결하는 선 그리기
folium.PolyLine(
    locations=[[dep["lat"], dep["lon"]], [dest["lat"], dest["lon"]]],
    color="blue",
    weight=3,
    opacity=0.7
).add_to(m)

# Folium 지도를 Streamlit 앱에 출력
st_folium(m, width=700)

# Haversine 공식을 사용하여 두 좌표 간 직선 거리 계산 함수
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # 지구 반지름 (킬로미터)
    # 위도와 경도를 라디안 단위로 변환
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# 두 지점 사이의 직선 거리 계산
distance = haversine(dep["lat"], dep["lon"], dest["lat"], dest["lon"])

# 계산된 직선 거리 출력
# st.write(f"경로의 직선 거리: {distance:.2f} km")

# 총 소요 시간 계산: 10km 당 40분
total_minutes = (distance / 10) * 40
hours = int(total_minutes // 60)
minutes = int(total_minutes % 60)
estimated_time = f"{hours}시간 {minutes}분"

# 환승 성공 확률: 50~100% 사이의 난수 생성
transfer_success_rate = random.randint(50, 100)

# --- 즐겨찾기 추가 버튼 (페이지 하단) ---
if st.button("즐겨찾기 추가"):
    st.session_state.favorite_departure = departure
    st.session_state.favorite_destination = destination
    st.success(f"즐겨찾기가 저장되었습니다! 출발지: {departure}, 도착지: {destination}")

# session_state에 'reroute' 플래그가 없으면 초기화
if "reroute" not in st.session_state:
    st.session_state.reroute = False


# 도착 예정 시간

with st.expander("경로 안내"):
    # 환승 성공 확률이 90% 미만이면 경고 메시지와 "다시 안내" 버튼 출력 (expander 내부)
    if transfer_success_rate < 90 and not st.session_state.reroute:
        st.warning("환승 실패 위험이 높습니다. 원하신다면 좀 더 안전한 경로를 추천해드리겠습니다.")
        if st.button("다시 안내"):
            st.session_state.reroute = True
    # 다시 안내 버튼이 눌렸다면, 표시할 환승 성공 확률은 100%로 변경
    displayed_rate = 100 if st.session_state.reroute else transfer_success_rate
                    
    st.markdown(
        f"""
        **총 소요 시간**: {estimated_time}        
        **이동 거리**: {distance:.2f}km  
        **환승**: 1회  
        **환승 성공 확률**: {displayed_rate}%  
        **카드 요금**: 1,800원  

        1. **{departure}**  
        2. **수락산역 4번 출구까지 걷기** *(14분)*  
        3. **수락산역 승차** *(서울지하철 7호선: 상계 → 가산디지털단지)*  
           - 44분, 27개 역 이동  
        4. **고속터미널역 승차** *(김포공항행)*  
           - 8분, 2개 역 이동  
        5. **{destination} 하차** 
        """
    )



st.page_link("Main.py", label="Back to Main", icon="🏠")