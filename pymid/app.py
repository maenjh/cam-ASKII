import streamlit as st
import cv2
import numpy as np
import time

# --- ASCII 변환 관련 설정 ---
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    (h, w) = image.shape
    aspect_ratio = h / float(w)
    new_height = int(aspect_ratio * new_width * 0.55)
    return cv2.resize(image, (new_width, new_height))

def gray_to_ascii(image):
    intensity_matrix = (image / 255.0 * (len(ASCII_CHARS) - 1)).astype(int)
    ascii_matrix = np.array(list(ASCII_CHARS))[intensity_matrix]
    ascii_lines = ["".join(row) for row in ascii_matrix]
    return "\n".join(ascii_lines)

# --- Streamlit UI ---
st.set_page_config(layout="wide")
st.title("🎥 실시간 웹캠 → ASCII 아트 변환기")
st.write("왼쪽엔 원본 카메라 영상, 오른쪽엔 동일 크기의 ASCII 변환 영상이 표시됩니다.")

# 실행 상태 저장
if 'run_ascii' not in st.session_state:
    st.session_state.run_ascii = False

col1, col2, _ = st.columns([1, 1, 5])

with col1:
    if st.button("🚀 Start", type="primary", use_container_width=True):
        st.session_state.run_ascii = True
with col2:
    if st.button("🛑 Stop", use_container_width=True):
        st.session_state.run_ascii = False
        st.rerun()

# 출력 영역 (왼쪽: 영상, 오른쪽: ASCII)
left_col, right_col = st.columns(2)
with left_col:
    st.subheader("📷 원본 영상")
    cam_placeholder = st.empty()
with right_col:
    st.subheader("🔡 ASCII 아트")
    ascii_placeholder = st.empty()

# 글자 크기와 해상도 조절 슬라이더
st.sidebar.title("⚙️ 설정")
ascii_width = st.sidebar.slider("ASCII 너비", 80, 200, 140, step=10)
font_size = st.sidebar.slider("폰트 크기(px)", 8, 20, 11, step=1)
bg_color = st.sidebar.color_picker("배경색", "#f8f9fa")
text_color = st.sidebar.color_picker("문자색", "#000000")

# --- 실행 루프 ---
if st.session_state.run_ascii:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("❌ 웹캠을 열 수 없습니다. 카메라 권한을 확인해주세요.")
    else:
        while st.session_state.run_ascii:
            ret, frame = cap.read()
            if not ret:
                st.warning("⚠️ 웹캠에서 프레임을 가져올 수 없습니다.")
                break

            # 원본 영상 출력
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

            # ASCII 변환
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized_gray = resize_image(gray, new_width=ascii_width)
            ascii_art = gray_to_ascii(resized_gray)

            # HTML 렌더링 (반응형 높이 & 폰트 크기 적용)
            html_ascii = f"""
            <div style="
                font-family: monospace;
                white-space: pre;
                font-size: {font_size}px;
                line-height: 80%;
                background-color: {bg_color};
                color: {text_color};
                width: 100%;
                height: auto;
                overflow: hidden;
            ">
                {ascii_art}
            </div>
            """
            ascii_placeholder.markdown(html_ascii, unsafe_allow_html=True)
            time.sleep(0.03)

        cap.release()
else:
    st.info("현재 정지 상태입니다. 'Start' 버튼을 눌러 시작하세요.")
