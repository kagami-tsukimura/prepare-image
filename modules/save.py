import os

import streamlit as st


def save_image(prepare_img, save_path):
    """
    画像を保存する。
    """
    OUTPUT_PATH = "./output"
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    try:
        prepare_img.save(f"{OUTPUT_PATH}/{save_path}")
        st.toast(f"Save Done!: {save_path}", icon="🎉")
    except Exception as e:
        st.write(f"Failed to save images: {e}")
