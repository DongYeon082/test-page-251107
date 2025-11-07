import random
import streamlit as st

st.set_page_config(page_title="동전 던지기", page_icon="🪙")

st.title("🪙 동전 던지기")
st.write("동전을 던져 결과를 확인하세요. 원하는 횟수를 선택하고 '던지기' 버튼을 눌러보세요.")

if "history" not in st.session_state:
    st.session_state.history = []

left, right = st.columns([3, 1])

with left:
    flips = st.number_input("몇 번 던질까요?", min_value=1, max_value=200, value=1, step=1)
    do_flip = st.button("던지기")

with right:
    if st.button("초기화"):
        st.session_state.history = []
        # Streamlit은 버튼 상호작용 시 자동으로 리렌더링되므로
        # 명시적인 rerun 호출은 불필요하며 일부 버전에서 존재하지 않을 수 있습니다.
        # 이전 동작을 유지하려면 아래 안전 호출을 사용할 수 있습니다:
        # rerun = getattr(st, "experimental_rerun", None)
        # if callable(rerun):
        #     rerun()

def _emoji(result: str) -> str:
    return "🙂" if result == "앞면" else "🌀"

if do_flip:
    results = []
    for _ in range(flips):
        r = random.choice(["앞면", "뒷면"])
        results.append(r)
        st.session_state.history.append(r)

    heads = results.count("앞면")
    tails = results.count("뒷면")

    st.success(f"이번 결과 — 앞면: {heads}  뒷면: {tails}")

    # 결과를 아이콘과 함께 보여주기 (간단한 레이아웃)
    cols = st.columns(min(10, flips))
    for i, r in enumerate(results):
        cols[i % len(cols)].write(f"{_emoji(r)} {r}")

if st.session_state.history:
    st.markdown("---")
    total = len(st.session_state.history)
    heads_total = st.session_state.history.count("앞면")
    tails_total = st.session_state.history.count("뒷면")

    st.header("전체 통계")
    st.write(f"총 던진 횟수: {total}")
    st.write(f"앞면: {heads_total} ({heads_total/total:.1%})  |  뒷면: {tails_total} ({tails_total/total:.1%})")

    st.bar_chart({"앞면": [heads_total], "뒷면": [tails_total]})

    if st.checkbox("히스토리 보기"):
        st.write(st.session_state.history)

else:
    st.info("아직 던진 기록이 없습니다. '던지기' 버튼을 눌러보세요.")

