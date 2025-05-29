import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config.config import Config
import logging
import streamlit as st
import st_const
from PIL import Image
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

logger = logging.getLogger(__name__)
im = Image.open("img/sample.ico")
ROLES = [None, "Admin"]
st.session_state.role = None
st.set_page_config(page_title="STREAMLIT SAMPLE", 
                   layout="wide", 
                   page_icon=im)
st.markdown(st_const.HIDE_ST_STYLE, unsafe_allow_html=True)
st.logo(
    "img/large_logo.png",
    size="large",
    icon_image="img/sample_logo.svg",
)

def main():
    # ページ定義
    top_page = st.Page(
        page="page_contents/page_top.py", title="Top", icon=":material/home:", default=True
    )
    admin_page = st.Page(
        page="page_contents/page_admin.py", title="管理者画面", icon=":material/open_with:"
    )

    # ナビゲーションの設定
    nav_dict = {"Menu": [top_page]}
    if st.session_state.role == "Admin":
        nav_dict["Admin. Menu"] = [admin_page]
    pg = st.navigation(nav_dict)
    pg.run()


def run_authenticator():
    with open("./config/st_config.yml") as file:
        config = yaml.safe_load(file)

    authenticator = stauth.Authenticate(
        credentials=config["credentials"],
        cookie_name=config["cookie"]["name"],
        cookie_key=config["cookie"]["key"],
        cookie_expiry_days=config["cookie"]["expiry_days"],
    )
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    status = st.session_state.get("authentication_status")
    if status:
        user_info = config["credentials"]["usernames"].get(st.session_state['username'])
        if user_info:
            st.session_state.role = user_info.get("role")
        # ログアウトボタンの追加
        authenticator.logout("ログアウト", "main")
        main()
    elif status is False:
        st.error("Username/password is incorrect")
    elif status is None:
        st.warning("Please enter your username and password")

if __name__ == "__main__":
    run_authenticator()