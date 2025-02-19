# OTT 구독 관리 서비스
import pandas as pd
import streamlit as st
from datetime import date, timedelta

st.title("🎬 OTT 구독 관리")

# OTT 리스트 선택
ott_list = ["Netflix", "Wavve", "Tving", "Coupang play", "Apple TV", "Youtube premium", "Watcha", "Disney +"]
ott_choice = st.selectbox("구독 중인 OTT 플랫폼을 선택하세요", ott_list)

# 결제일 및 금액 입력
payment_date = st.date_input("최초 결제일을 선택하세요", date.today())
subscription_fee = st.number_input("월 구독료 (₩)", min_value=1000, step=100)

# 저장(구독 추가)
if "subscriptions" not in st.session_state:
    st.session_state["subscriptions"] = pd.DataFrame(columns=["OTT", "최초 결제일", "구독료", "월별 자동결제일"])

if st.button("구독 추가"):  
    if ott_choice in st.session_state["subscriptions"]["OTT"].unique():
        st.error(f"{ott_choice}는 이미 등록된 구독입니다.")
    else:
        new_data = pd.DataFrame([[ott_choice, payment_date, subscription_fee, payment_date.day]], columns=["OTT", "최초 결제일", "구독료", "월별 자동결제일"])
        st.session_state["subscriptions"] = pd.concat([st.session_state["subscriptions"], new_data], ignore_index=True)
        st.success(f"매월 {payment_date.day}일에  {ott_choice}  구독비  {subscription_fee:,}원이 결제됩니다.")

#구독현황
if not st.session_state["subscriptions"].empty:
    st.subheader("📊 내 구독 현황")
    st.dataframe(st.session_state["subscriptions"])

    # 총 구독료 계산
    total_cost = st.session_state["subscriptions"]["구독료"].sum()
    st.metric(label="총 월 구독료", value=f"₩{total_cost:,}")

    # 구독료 시각화
    st.bar_chart(st.session_state["subscriptions"].set_index("OTT")["구독료"])

# 메인 캘린더에 저장
    if st.button("📆 캘린더 반영"):
        if st.session_state["subscriptions"].empty:
            st.error(f"등록한 구독 서비스가 없습니다. [구독추가]를 선행해주세요.")
        else:
            cnt=st.session_state["subscriptions"]["OTT"].count()
            st.success(f"총 {cnt}건의 구독 현황이 캘린더에 반영되었습니다. Main페이지에서 확인해주세요.")

# 알림받기
    if st.button("🔔결제일 알림받기"):
        if st.session_state["subscriptions"].empty:
            st.error(f"등록한 구독 서비스가 없습니다. [구독추가]를 선행해주세요.")
        else:
            try:
                for _, row in st.session_state["subscriptions"].iterrows():
                    st.success(f"매월 {row['월별 자동결제일']}일에 {row['OTT']} 결제 알림이 발송됩니다.")
            except Exception as e:
                st.error(f"알림을 생성하는 중 오류가 발생했습니다: {e}")