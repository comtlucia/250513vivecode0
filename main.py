import streamlit as st

st.set_page_config(page_title="🌟 나를 닮은 직업 찾기", page_icon="🧭", layout="centered")

# 🎯 화려한 메인 타이틀
st.markdown("""
# 🌟 "내 성향으로 미래를 그려봐!" 🌟  
### MBTI로 보는 ✨맞춤형 진로 로드맵✨  
> 내가 어떤 사람인지 알면, 어울리는 일이 보이기 시작해요.  
""")

st.markdown("---")

mbti_types = [
    "INTJ", "INFP", "ENTP", "ISFJ", "ENFP"
]

# ✨ 성향별 말투와 추천 정보
mbti_data = {
    "INTJ": {
        "style": "🧠 음… 당신은 전략적이고 냉철한 INTJ 타입이군요. 복잡한 걸 좋아하고, 조용히 완벽하게 해내는 타입이에요.",
        "jobs": [
            {"name": "AI 개발자 🤖", "reason": "🧩 체계적인 사고로 알고리즘을 설계하는 데 강해요."},
            {"name": "데이터 과학자 📊", "reason": "📈 방대한 데이터 속 패턴을 읽는 통찰력이 뛰어나요."},
            {"name": "시스템 엔지니어 🛠️", "reason": "🔧 시스템의 구조와 안정성을 설계하는 데 적합해요."}
        ]
    },
    "INFP": {
        "style": "🌸 와, 당신은 감성 충만한 INFP! 말은 적지만 마음속엔 따뜻한 가치와 상상이 가득하죠.",
        "jobs": [
            {"name": "시인 ✍️", "reason": "🌷 세상의 감정을 섬세하게 담아낼 수 있어요."},
            {"name": "일러스트레이터 🎨", "reason": "🖌️ 머릿속 세계를 그림으로 펼치는 데 탁월해요."},
            {"name": "심리상담가 💬", "reason": "💖 타인의 마음을 깊이 이해하고 공감할 줄 알아요."}
        ]
    },
    "ENTP": {
        "style": "💡 아이디어 뿜뿜! 당신은 어디서든 활기를 주는 ENTP예요. 말도 잘하고 생각도 톡톡 튀죠!",
        "jobs": [
            {"name": "광고 기획자 📣", "reason": "🎯 창의적이고 도발적인 메시지를 만드는 데 딱이에요."},
            {"name": "스타트업 창업가 🚀", "reason": "🔥 모험과 변화를 즐기며 판을 뒤엎는 걸 좋아하잖아요!"},
            {"name": "방송인 🎙️", "reason": "🎤 사람들과 소통하고 주목받는 걸 좋아하니까요."}
        ]
    },
    "ISFJ": {
        "style": "💖 따뜻하고 묵묵한 헌신가, 바로 ISFJ! 겉으론 조용하지만 속은 누구보다 책임감 강해요.",
        "jobs": [
            {"name": "간호사 👩‍⚕️", "reason": "🩺 섬세하고 헌신적인 돌봄이 필요한 직업이죠."},
            {"name": "사회복지사 🧓", "reason": "🌱 약자들을 돌보는 데에서 큰 보람을 느껴요."},
            {"name": "교직원 🏫", "reason": "📘 규칙적인 환경 속에서 누군가를 돕는 일에 잘 어울려요."}
        ]
    },
    "ENFP": {
        "style": "🌈 당신은 자유로운 영혼, ENFP! 열정과 호기심으로 가득해서 항상 새로운 걸 탐색하죠.",
        "jobs": [
            {"name": "유튜버 🎥", "reason": "📷 끊임없이 새로운 콘텐츠를 만들고 표현하는 걸 즐기니까요."},
            {"name": "콘서트 기획자 🎤", "reason": "🎉 흥과 기획력이 넘치는 당신에게 찰떡이에요."},
            {"name": "무용가 💃", "reason": "💃 표현력과 에너지로 무대를 사로잡을 수 있어요."}
        ]
    }
}

# 🌟 사용자 선택
selected_mbti = st.selectbox("📌 당신의 MBTI를 골라보세요!", mbti_types)

# 🎁 결과 출력
if selected_mbti:
    profile = mbti_data[selected_mbti]

    st.markdown("---")
    st.subheader(f"💬 성향 분석")
    st.markdown(f"**{profile['style']}**")

    st.markdown("## 🎯 추천 진로")
    for job in profile["jobs"]:
        st.markdown(f"### {job['name']}")
        st.markdown(f"- {job['reason']}")

    st.markdown("---")
    st.success("🌟 진로는 정답이 아니라 방향이에요. 당신다운 길을 스스로 열어가 보세요!")
