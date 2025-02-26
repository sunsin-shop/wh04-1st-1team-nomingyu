# 🚀 PlanMate

**Team Name**: 민규없는 민규팀
**Version**: 0.2.0v  
**Web Link**:  [Smart Assistant](https://nomingyu.streamlit.app/) /
 **Requirements and Scenarios**: [Wiki](https://github.com/sunsin-shop/wh04-1st-1team-nomingyu/wiki)
 
> **PlanMate**는 개인 맞춤형 스케줄 관리 서비스입니다.  
> OTT 구독 일정, 취업 일정, 신발 가격 추이, 교통 정보 등을 관리하고,  
> 사용자 맞춤형 알림과 캘린더 기능을 제공합니다.

📅 **누구를 위한 서비스인가?**  
- 취업 준비생 (🚆 교통 및 취업 일정 관리)  
- 신발 및 OTT 서비스에 관심 있는 사용자 (👟 관심 가격 추적, 🎬 구독 관리)  
- 일정을 통합 관리하고 싶은 사용자 (⚡ 스마트 알림)  

📌 **현재 개발 상태:**
- ✅ 기본 UI 및 데이터 구조 설계 중
- 🚧 주요 기능 MVP 단계 개발 진행 중

<br>

## 요구사항 및 시나리오

- [Docs](https://github.com/sunsin-shop/wh04-1st-1team-nomingyu/wiki)

<br>

## **👥 Members**
### **민규 없는 민규팀**
|이름|깃허브|
|---|---|
|권오준|[vhzkclq0705](https://github.com/vhzkclq0705)|
|강현룡|[stundrg](https://github.com/stundrg)|
|전희진|[heejin131](https://github.com/heejin131)|
|서민혁|[wminhyuk](https://github.com/wminhyuk)|
|안재영|[Jacob-53](https://github.com/Jacob-53)|

<br>

## **🌟 Features**  
### 🎬 OTT 구독 관리  
- 사용자의 OTT 구독 일정 및 비용을 자동 추적  
- `다가오는 결제일 & 총 구독비`를 알림 제공  

### 💼 취업 일정 관리  
- 관심 있는 `취업 공고`, `서류 발표일`, `면접 일정` 정리  
- 자동 리마인드 및 체크리스트 제공  

### 🚆 교통 혼잡 회피 및 최적 경로 추천  
- 특정 요일·시간대별 `교통 정체 예측`  
- 실시간 데이터를 기반으로 `대체 경로 제안`  

### 🚀 이동시간 맞춤 콘텐츠 추천  
- 예상 `이동시간(e.g. 50분)에 최적화된 영상` 추천  
- 사용자 취향 기반 콘텐츠 큐레이션  

### 👟 관심 신발 가격 추이 분석  
- 관심 신발의 `가격 변동 및 판매량 추적`  
- `최저가 시점 예측` 및 `가격 알림` 기능 제공  

### ⚡ 실시간 알림 & 스마트 피드백  
- **쇼핑** → 관심 상품 최저가 발생 시 알림 (🛒 "지금 신발을 사면 10% 할인 가능!")  
- **교통** → 혼잡 시 대체 경로 추천 (🚆 "환승 가능성이 낮아요. 다른 경로 추천드립니다.")  

<br>

## **🛠 Architecture**

### **📊 데이터 모델링 (예정)**
📌 *현재 데이터 모델이 안정되지 않았지만, 핵심 데이터 구조를 정의할 예정.*  

### **🖥 Pages**
```
Main - 메인 페이지
/pages
├── Transport - 교통 정보
├── OTT - OTT 플랫폼
├── Job - 취업 정보
└── Shoes - 신발 가격 추이
```

<br>

## **⚙️ Development Guide (개발 환경 설정)**  
```bash
# 1️⃣ PDM 가상환경 활성화
$ source .venv/bin/activate

# 2️⃣ 프로젝트 패키지 설치
$ pdm install

# 3️⃣ 로컬 서버 실행 (Streamlit)
$ pdm run streamlit run main.py

# 새로운 기능을 개발할 때
$ git checkout -b <버전>/feature-<기능명>

# 변경 사항 추가 & 커밋
$ git add .
$ git commit -a

# 원격 저장소로 푸시
$ git push
```

<br>

## **Local Test (로컬 환경 테스트)**
```bash
# merge된 브랜치로 이동
$ git checkout <브랜치명> # ex) 0.1/develop

# 브랜치 내용 가져오기
$ git pull origin <브랜치명> # ex) 0.1/develop

# 로컬 환경 실행
$ streamlit run Main.py
```
