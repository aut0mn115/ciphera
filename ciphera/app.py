import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Streamlit 페이지 설정
st.set_page_config(
    page_title="서문준 html",
    page_icon="🎵",
    layout="wide"
)

# HTML 파일 경로 설정
# 현재 스크립트(app.py)가 있는 디렉토리를 기준으로 htmls/index.html 파일을 찾습니다.
current_dir = Path(__file__).parent
html_file_path = current_dir / "htmls" / "숫자_약수_맞추기_게임.html"

# HTML 파일이 존재하는지 확인
if not html_file_path.exists():
    st.error(f"오류: HTML 파일을 찾을 수 없습니다. 경로를 확인해주세요: {html_file_path}")
else:
    # HTML 파일 내용을 읽어와서 Streamlit에 표시
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit에 HTML 컴포넌트 삽입
    # height 파라미터를 사용해 페이지 전체 높이를 유동적으로 조절합니다.
    components.html(html_content, height=1200, scrolling=True)

# 페이지 하단에 추가 정보 표시 (선택 사항)
st.markdown("---")
st.markdown("### 💡 Streamlit 앱 사용 팁")
st.markdown("- `htmls` 폴더 안에 있는 `index.html` 파일의 내용을 수정하면 앱에 바로 반영됩니다.")
st.markdown("- 더 많은 Streamlit 컴포넌트를 사용해 이 앱을 확장할 수 있습니다.")

