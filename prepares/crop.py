from datetime import datetime

import streamlit as st
from matplotlib import pyplot as plt
from PIL import Image

from modules.prepare_temp import Preparation
from modules.save import save_image


def show_crop_page():
    """
    メイン処理。
    """
    file_path = st.file_uploader("画像を選択してください")

    if file_path:
        preparator = Preparation()
        img = Image.open(file_path)
        st.image(img)
        # 縦横の小さいサイズを前処理基準とする
        img_size = min(img.size)

        # 前処理の選択
        preparation = st.selectbox(
            "Preparing by Transform",
            preparator.TRANS_CROPS,
        )

        # 前処理の範囲調整
        scope = st.slider(
            "Prepare scope", min_value=1, max_value=img_size, value=img_size // 2
        )

        transform = preparator.setting_crop_prepare(preparation, scope)
        st.subheader("Result")

        images = transform(img)

        if isinstance(images, tuple):
            # 複数画像は2行に分割
            num_rows = 2
            num_cols = len(images) // 2
            # 1行目に表示する画像のインデックス
            first_row_inds = list(range(num_cols))

            fig, axes = plt.subplots(
                # 奇数なら1列追加(out of bounds対策)
                num_rows,
                (num_cols + 1 if num_cols % 2 == 0 else num_cols),
            )

            # ラベルと被らないように、x軸の幅調整
            plt.subplots_adjust(wspace=0.7)

            # 各軸に画像を表示
            for i, image in enumerate(images):
                if i in first_row_inds:
                    row = 0
                    col = i
                else:
                    row = 1
                    col = i - num_cols
                axes[row][col].imshow(image)

            st.pyplot(fig)
        else:
            prepare_img = transform(img)
            st.image(prepare_img)

            # ボタンの水平レイアウトを作成
            save_img, save_img_another = st.columns(2)

            if save_img.button("Save image"):
                save_image(prepare_img, file_path.name)

            if save_img_another.button("Save image by another name"):
                date = datetime.now()
                another_file_path = f"{date.strftime('%Y%m%d%H%M%S')}.png"
                save_image(prepare_img, another_file_path)
