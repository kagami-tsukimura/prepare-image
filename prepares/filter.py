from datetime import datetime

import streamlit as st
from PIL import Image

from modules.prepare_temp import Preparation
from modules.save import save_image


def show_filter_page():
    """
    メイン処理。
    """
    file_path = st.file_uploader("Choose an image")

    if file_path:
        preparator = Preparation()
        img = Image.open(file_path)
        st.image(img)

        # 前処理の選択
        preparation = st.selectbox(
            "Preparing by Transform",
            preparator.TRANS_FILTERS,
        )

        # GaussianBlurにはカーネルサイズ、標準偏差を設定
        if preparation == preparator.TRANS_FILTER["GaussianBlur"]:
            kernel_size = st.slider(
                "kernel_size", min_value=1, max_value=9, value=3, step=2
            )
            sigma_min, sigma_max = st.slider("sigma", min_value=0.1, value=(0.1, 2.0))
        else:
            kernel_size, sigma_min, sigma_max = None, None, None

        transform = preparator.setting_filter_prepare(
            preparation, kernel_size, sigma_min, sigma_max
        )
        st.subheader("Result")

        prepare_img = transform(img)
        st.image(prepare_img)

        # Create horizontal layout for buttons
        save_img, save_img_another = st.columns(2)

        if save_img.button("Save image"):
            save_image(prepare_img, file_path.name)

        if save_img_another.button("Save image by another name"):
            date = datetime.now()
            another_file_path = f"{date.strftime('%Y%m%d%H%M%S')}.png"
            save_image(prepare_img, another_file_path)
