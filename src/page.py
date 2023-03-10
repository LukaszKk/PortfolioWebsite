import streamlit as st
import pandas as pd
from utils import IMAGES, PHOTO, TITLE, SELF_DESCRIPTION, APPS_TITLE, DATA


class Page:
    def __init__(self):
        st.set_page_config(layout="wide")
        self.self_description()
        self.apps_description()

    @staticmethod
    def self_description():
        col1, col2 = st.columns(2)

        with col1:
            st.image(PHOTO)

        with col2:
            st.title(TITLE)
            st.write(SELF_DESCRIPTION)

    @staticmethod
    def apps_description():
        st.write(APPS_TITLE)

        col3, _, col4 = st.columns([1.5, 0.5, 1.5])

        df = pd.read_csv(DATA, sep=";")
        with col3:
            for index, row in df[::2].iterrows():
                st.header(row["title"])
                st.write(row["description"])
                st.image(rf"{IMAGES}/{row['image']}")
                st.write(f"[Source Code]({row['url']})")

        with col4:
            for index, row in df[1::2].iterrows():
                st.header(row["title"])
                st.write(row["description"])
                st.image(rf"{IMAGES}/{row['image']}")
                st.write(f"[Source Code]({row['url']})")
