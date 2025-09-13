import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Streamlit 페이지 설정
st.set_page_config(
    page_title="서문준 html",
    page_icon="🎵",
    layout="wide"
)

# 현재 디렉토리와 htmls 폴더 경로
current_dir = Path(__file__).parent
htmls_dir = current_dir / "htmls"

# htmls 폴더 안의 모든 .html 파일 가져오기
html_files = list(htmls_dir.glob("*.html"))

if not html_files:
    st.error("오류: htmls 폴더에 HTML 파일이 없습니다.")
else:
    # 파일 이름 리스트 만들기
    file_names = [f.name for f in html_files]

    # 사이드바에서 HTML 선택
    selected_file = st.sidebar.selectbox("열 HTML 파일을 선택하세요:", file_names)

    # 선택한 HTML 파일 경로
    html_file_path = htmls_dir / selected_file

    # HTML 내용 읽어서 출력
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    components.html(html_content, height=1200, scrolling=True)

# 페이지 하단 안내
st.markdown("---")
st.markdown("### 💡 Streamlit 앱 사용 팁")
st.markdown("- 사이드바에서 원하는 HTML 파일을 선택하면 표시됩니다.")
st.markdown("- `htmls` 폴더 안에 새로운 HTML 파일을 넣으면 자동으로 목록에 추가됩니다.")
