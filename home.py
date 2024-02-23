from enum import Enum

import streamlit as st

from prepares.crop import show_crop_page
from prepares.filter import show_filter_page


class PageType(Enum):
    CROP = "crop"
    FILTER = "filter"


def main():
    st.sidebar.title("Choose prepare page")
    page = st.sidebar.selectbox(" ", [page.value for page in PageType])

    if page == PageType.CROP.value:
        show_crop_page()
    elif page == PageType.FILTER.value:
        show_filter_page()


if __name__ == "__main__":
    main()
