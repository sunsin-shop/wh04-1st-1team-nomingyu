# OTT 구독 관리 서비스

import pandas as pd
import streamlit as st
from datetime import date

st.title("🎬 OTT 구독 관리")

# OTT 리스트 선택
ott_list = ["Netflix", "Wavve", "Tving", "Coupang play", "Apple TV", "Youtube premium", "Watcha", "Disney +"]
ott_choice = st.selectbox("구독 중인 OTT 플랫폼을 선택하세요", ott_list)

# 결제일 및 금액 입력
payment_date = st.date_input("최초 결제일을 선택하세요", date.today())
subscription_fee = st.number_input("월 구독료 (₩)", min_value=0, step=100)

# 저장 

if "subscriptions" not in st.session_state:
    st.session_state["subscriptions"] = pd.DataFrame(columns=["OTT", "결제일", "구독료"])

if st.button("구독 추가"):
    new_data = pd.DataFrame([[ott_choice, payment_date, subscription_fee, payment_date.day]], columns=["OTT", "최초 결제일", "구독료", "결제일"])
    st.session_state["subscriptions"] = pd.concat([st.session_state["subscriptions"], new_data], ignore_index=True)
    st.success(f"매월 {ott_choice}에  {payment_date.day}일  {subscription_fee:,}원이 결제됩니다.")

if not st.session_state["subscriptions"].empty:
    st.subheader("📊 내 구독 현황")
    st.dataframe(st.session_state["subscriptions"])

    # 총 구독료 계산
    total_cost = st.session_state["subscriptions"]["구독료"].sum()
    st.metric(label="총 월 구독료", value=f"₩{total_cost:,}")

    # 구독료 시각화
    st.bar_chart(st.session_state["subscriptions"].set_index("OTT")["구독료"])