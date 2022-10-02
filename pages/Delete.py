import streamlit as st
import os

st.write("Delete")
for x in os.listdir('./'):
    if x.endswith(".mp3"):
        with open(x, "rb") as file:
                if st.button(x):
                    os.remove(x)
    
    if x.endswith(".webm"):
        with open(x, "rb") as file:
                if st.button(x):
                    os.remove(x)
    if x.endswith(".mp4"):
        with open(x, "rb") as file:
                if st.button(x):
                    os.remove(x)
    if x.endswith(".3gpp"):
        with open(x, "rb") as file:
                if st.button(x):
                    os.remove(x)