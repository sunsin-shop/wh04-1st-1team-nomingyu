import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime, timedelta
import time
import pytz
import uuid

# 로직 관련 함수
def convert_datetime(date):
    dt = datetime.fromisoformat(date).astimezone(pytz.timezone("Asia/Seoul"))
    formatted_date = dt.strftime("%Y-%m-%d %p %I시 %M분").replace("AM", "오전").replace("PM", "오후")
    return formatted_date

st.set_page_config(page_title="📅 일정 관리 캘린더", layout="wide")
st.title("📅 일정 관리 캘린더")

# 한국 시간
KST = pytz.timezone("Asia/Seoul")
now = datetime.now(KST)

# 세션 상태에 이벤트 및 선택한 시간 저장
if "events" not in st.session_state:
    st.session_state.events = [
        {
            "id": str(uuid.uuid4()),
            "title": "프로젝트",
            "start": datetime(2025, 2, 17, 9, 0, 0).isoformat(),
            "end": datetime(2025, 2, 19, 18, 0, 0).isoformat(),
            "color": "green"
        },
        {
            "id": str(uuid.uuid4()),
            "title": "소개팅",
            "start": datetime(2025, 2, 21, 18, 30, 0).isoformat(),
            "end": datetime(2025, 2, 21, 22, 0, 0).isoformat(),
            "color": "red"
        }
    ]
if "start_time" not in st.session_state:
    st.session_state.start_time = now.time()
if "end_time" not in st.session_state:
    st.session_state.end_time = now + timedelta(hours=1)

# 캘린더 옵션
options = {
    "initialView": "dayGridMonth",
    "eventDisplay": "block",
    "slotLabelFormat": {"hour": "2-digit", "minute": "2-digit", "hour12": False},
    "eventTimeFormat": {"hour": "2-digit", "minute": "2-digit", "hour12": False}
}

# 캘린더 표시 (월별)
cal = calendar(events=st.session_state.events, options=options)

# 캘린더에서 클릭한 이벤트 가져오기
st.subheader("📌 선택한 일정")
selected_event = cal.get("eventClick")

if selected_event:
    event_id = selected_event['event']['id']
    found_event = next(e for e in st.session_state.events)
    
    st.write(f"**제목:** {found_event['title']}")
    st.write(f"**시작:** {convert_datetime(found_event['start'])}")
    st.write(f"**종료:** {convert_datetime(found_event['end'])}")

# 새 일정 추가
st.subheader("➕ 일정 추가")

new_title = st.text_input("일정 제목")
start_date = st.date_input("시작 날짜", now.date())
end_date = st.date_input("종료 날짜", now.date())

start_time = st.time_input("시작 시간", st.session_state.start_time)
end_time = st.time_input("종료 시간", st.session_state.end_time)

if start_time != st.session_state.start_time:
    st.session_state.start_time = start_time
if end_time != st.session_state.end_time:
    st.session_state.end_time = end_time

color = st.color_picker("색상 선택", "#ff5733")

if st.button("일정 추가"):
    if new_title:
        new_event = {
            "id": str(uuid.uuid4()),
            "title": new_title,
            "start": datetime.combine(start_date, st.session_state.start_time).isoformat(),
            "end": datetime.combine(end_date, st.session_state.end_time).isoformat(),
            "color": color
        }
        st.session_state.events.append(new_event)
        st.success("✅ 일정 추가가 완료되었습니다!")
        time.sleep(1)
        st.rerun()
    else:
        st.warning("⚠️ 제목을 입력해 주세요.")