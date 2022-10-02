import streamlit as st
import os

st.write("Download")
for x in os.listdir('./'):
    if x.endswith(".mp3"):
        with open(x, "rb") as file:
                btn = st.download_button(
                        label=x,
                        data=file,
                        file_name=x,
                    )
    if x.endswith(".webm"):
        with open(x, "rb") as file:
                btn = st.download_button(
                        label=x,
                        data=file,
                        file_name=x,
                    )
    if x.endswith(".mp4"):
        with open(x, "rb") as file:
                btn = st.download_button(
                        label=x,
                        data=file,
                        file_name=x,
                    )
    if x.endswith(".3gpp"):
        with open(x, "rb") as file:
                btn = st.download_button(
                        label=x,
                        data=file,
                        file_name=x,
                    )