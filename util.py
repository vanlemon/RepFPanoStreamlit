import streamlit as st

import cv2


def st_image_file(arg_st, image_file, **kwargs):
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    arg_st.image(img, channels="BGR", **kwargs)


def get_progress():
    _bar = st.progress(0)
    _value = 0

    def progress(inc_value):
        import time
        time.sleep(0.01)

        nonlocal _value
        _value = _value + inc_value / 100

        if _value >= 0.99:  # 可能会有 float 误差不足 1.0，同时避免溢出 1.0
            _bar.progress(1.0)
            st.balloons()
        else:
            _bar.progress(_value)

    return progress
